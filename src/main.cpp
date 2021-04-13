#include <cmath>		/* pow() */
#include <cstdint>		/* uint64_t */
#include <ctime>		/* time() */

#include <unistd.h>
#include <iostream>

#include "../include/ntt.h"	/* naiveNTT(), outOfPlaceNTT_DIT() */
#include "../include/utils.h"	/* printVec() */

using namespace std;

int main(int argc, char *argv[]){
  uint64_t n = 8; // originally was 4096, must be a power of 2
  uint64_t p = 68719403009;
  uint64_t r = 36048964756;
  bool t = true;

  uint64_t vec[n];

  for (int i = 0; i < n; i++){
    vec[i] = i;
  }
  printVec(vec, n);

  uint64_t *outVec = inPlaceNTT_DIT(vec,n,p,r,t);

	printVec(outVec, n);

	return 0;

}
