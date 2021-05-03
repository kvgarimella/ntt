#include <cmath>		/* pow() */
#include <cstdint>		/* uint64_t */
#include <ctime>		/* time() */
#include <cstdlib>

#include <unistd.h>
#include <iostream>

#include "../include/ntt.h"	/* naiveNTT(), outOfPlaceNTT_DIT() */
#include "../include/utils.h"	/* printVec() */

using namespace std;

int main(int argc, char *argv[]){
  if (argc < 2)
  {
      printf("You must enter a size for the vector! Please make it a power of 2\n");
      return -1;
  }
  uint64_t n = atoi(argv[1]);
  //uint64_t n = 8; // originally was 4096, must be a power of 2
  uint64_t p = 1073750017;
  uint64_t r = 5;
  bool t = true;
  clock_t t_start, t_end;
  t_start = clock();
  double seconds;

  uint64_t vec[n];

  for (int i = 0; i < n; i++){
    vec[i] = i;
  }
  printVec(vec, n);

  uint64_t *outVec = inPlaceNTT_DIT(vec,n,p,r,t);
  printVec(outVec, n);
  t_end = clock();
  seconds = (double)(t_end - t_start) / CLOCKS_PER_SEC;
  printf("Time: %f\n", seconds);
  return 0;

}
