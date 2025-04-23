#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

#include "mult.h"

int main() {
	int64_t x;
	x = mult(7, 3);
	printf("%" PRId64 "\n", x);
	return 0;
}
