PROG = interop.elf
SRC  = mult.ir
ASM  = $(SRC:.ir=.s)
OBJ  = $(SRC:.ir=.o)
CSRC = interop.c

.PHONY: all clean

.PRECIOUS: %.s

all: $(PROG)

$(PROG): $(OBJ) ${CSRC}
	gcc $(CFLAGS) -o $@ $^	

%.o: %.s
	gcc $(CFLAGS) -c $<

%.s: %.ir
	codegen $< | tee $@

clean: clean-check
	rm -f $(OBJ) $(ASM) $(PROG)

TESTS = $(wildcard *.in)
TESTOUT = $(TESTS:.in=.out)
TESTERR = $(TESTS:.in=.err)
TESTEXIT = $(TESTS:.in=.exit)
TESTDIFF = $(TESTS:.in=.out.diff) $(TESTS:.in=.exit.diff)
TESTDIFFEXIT = $(TESTS:.in=.out.diffexit) $(TESTS:.in=.exit.diffexit)

.PHONY: check clean-check

.PRECIOUS: %.out

%.out: %.in ${PROG}
	-$(shell echo "./${PROG} < $< > $@ 2> $(@:.out=.err)"; ./${PROG} < $< > $@ 2> $(@:.out=.err))
	echo $(.SHELLSTATUS) > $(@:.out=.exit)

%.exit.diff: %.out
	$(shell diff $(<:.out=.exit.groundtruth) $(<:.out=.exit) > $@)
	echo $(.SHELLSTATUS) > $(@:.exit.diff=.exit.diffexit)

%.out.diff: %.out
	$(shell diff $(<:.out=.out.groundtruth) $< > $@)
	echo $(.SHELLSTATUS) > $(@:.out.diff=.out.diffexit)

check: $(TESTDIFF)

clean-check:
	rm -f $(TESTOUT) $(TESTERR) $(TESTEXIT) $(TESTDIFF) $(TESTDIFFEXIT)
