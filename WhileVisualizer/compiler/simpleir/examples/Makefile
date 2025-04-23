# from https://stackoverflow.com/questions/17834582/run-make-in-each-subdirectory

TOPTARGETS := all clean check clean-check

EXAMPLES = $(wildcard */.)

.PHONY: $(TOPTARGETS) $(EXAMPLES) 

$(TOPTARGETS): $(EXAMPLES)

$(EXAMPLES):
	$(MAKE) -C $@ $(MAKECMDGOALS)
