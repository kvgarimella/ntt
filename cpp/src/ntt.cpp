#include <cmath>		/* log2(), pow() */
#include <cstdint>		/* uint64_t */
#include <cstdlib> 		/* malloc() */
#include <iostream>

#include "../include/utils.h"	/* bit_reverse(), modExp(), modulo() */
#include "../include/ntt.h" 	//INCLUDE HEADER FILE
#define DEBUG 1
/**
 * Perform an in-place iterative breadth-first decimation-in-time Cooley-Tukey NTT on an input vector and return the result
 *
 * @param vec 	The input vector to be transformed
 * @param n	The size of the input vector
 * @param p	The prime to be used as the modulus of the transformation
 * @param r	The primitive root of the prime
 * @param rev	Whether to perform bit reversal on the input vector
 * @return 	The transformed vector
 */
uint64_t *inPlaceNTT_DIT(uint64_t *vec, uint64_t n, uint64_t p, uint64_t r, bool rev){

	uint64_t *result;
	uint64_t m, k_, a, factor1, factor2;

	result = (uint64_t *) malloc(n*sizeof(uint64_t));

	if(rev){
		result = bit_reverse(vec, n);
	}else{
		for(uint64_t i = 0; i < n; i++){	
			result[i] = vec[i];
		}
	}

	for(uint64_t i = 1; i <= log2(n); i++){ 
        if (DEBUG)
        {
            printf("In Loop: ");
            printVec(result, n);
        }

		m = pow(2,i);
		k_ = (p - 1)/m;
		a = modExp(r,k_,p);
                if (DEBUG)
                {
                    printf("modExps: %llu, %llu, %llu\n", r, k_, p);
                    printf("a: %llu\n", a);
                }

		for(uint64_t j = 0; j < n; j+=m){

			for(uint64_t k = 0; k < m/2; k++){

				factor1 = result[j + k];
				factor2 = modulo(modExp(a,k,p)*result[j + k + m/2],p);

			
				result[j + k] 		= modulo(factor1 + factor2, p);
				result[j + k+m/2] 	= modulo(factor1 - factor2, p);
                                if (DEBUG) 
                                {
                                    std::cout << "Factors: " << factor1 << ", " << factor2 << std::endl;
                                    std::cout << "i, j, k: " << i << ", " << j << ", " << k << std::endl;
                                    std::cout << "Working on indices: " << j + k<< ", " << j + k + m/2 << std::endl;
                                    std::cout << result[j+k] << ", " << result[j + k + m/2] << std::endl;
                                }

			}
		}

	}

	return result;

}
