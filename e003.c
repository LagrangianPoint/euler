#include <stdio.h>
int main(void) {
	printf("hello world\n");
	unsigned long long factor, number = 1, tmpNumber;
	//number = 13195;
	number = 600851475143LL;
	tmpNumber = number;
	factor = 3;
	while(factor < number / 2 ) {
		if (tmpNumber % factor == 0) {
			printf("%llu\n", factor);
			tmpNumber = tmpNumber / factor;
			if (tmpNumber == 1) {
					break;
			}
		}
		factor += 2;
	}
	return 0;
}
