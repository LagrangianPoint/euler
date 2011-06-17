#include <stdio.h>

unsigned long long countFactors(unsigned long long number) {
	unsigned long long i, nTotal = 1LL;
	if (number == 1LL) {
		return nTotal;
	}
	i = 2LL;
	while (i < (number / 2LL) + 1LL ) {
		if (number % i == 0LL) {
			nTotal += 1LL;
		}
		i += 1LL;
	}
	nTotal += 1LL;
	return nTotal;

}

int main(void) {
	unsigned long long i = 1LL, inc = 2LL, nFactors;
	printf("hello world\n");

	//printf("++++  %llu\n ", countFactors(28LL));
	while (1) {
		nFactors = countFactors(i);
		printf("++++ %llu:  %llu\n ",i ,nFactors);
		if (nFactors > 500LL) {
			printf("***********  %llu\n ", i);
			break;
		}
		i += inc;
		inc += 1LL;
	}


/*
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
*/
	return 0;
}
