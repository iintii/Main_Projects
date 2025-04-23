#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

int print_int(int64_t x) {
	printf("%" PRId64 "\n", x);
	return 0;
}
