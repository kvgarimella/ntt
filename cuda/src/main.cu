#include <cmath>		/* pow() */
#include <cstdint>		/* uint64_t */
#include <ctime>		/* time() */
#include <cstdlib>

#include <unistd.h>
#include <iostream>

#include "ntt.cu"
#include "utils.cu"


using namespace std;
#include <ctime>		/* time() */
#include <sys/time.h>
#include <stdlib.h>
#include <iostream>
#include <cstdint> 		

int main(int argc, char *argv[]){
  if (argc < 3)
  {
      printf("Usage: ./ntt [Vector Size] [Batch Size]\n");
      printf("You must enter a size for the vector and the number of vectors!\n");
      printf("Please make the vector a power of 2\n");
      return -1;
  }

  uint64_t n     = atoi(argv[1]);
  uint64_t batch = atoi(argv[2]);


  uint64_t p = 1073750017;
  uint64_t r = 5;
  bool t     = true;

  int size = n * batch*sizeof(uint64_t);
  uint64_t *vec;
  vec = (uint64_t *) malloc(size);
  for (int kk = 0; kk < batch; ++kk){
      for (int ii = 0; ii < n; ++ii)
          vec[kk*n + ii] = ii;
  }
  printf("Original vector: ");
  printVec(vec, n);

  uint64_t *result_gpu, *vec_gpu, *result_cpu;
  result_cpu = (uint64_t *) malloc(size);

  cudaMalloc((void**)&vec_gpu, size);
  cudaMemcpy(vec_gpu, vec, size, cudaMemcpyHostToDevice);


  result_gpu = bit_reverse_table(vec_gpu, n, batch);
  inPlaceNTT_DIT(result_gpu, n, p, r, t, batch); 


  cudaMemcpy(result_cpu, result_gpu, size, cudaMemcpyDeviceToHost);
  printf("Final vector   : ");
  printVec(result_cpu, n);

  cudaFree(result_gpu);
  cudaFree(vec_gpu);
  free(result_cpu);
  free(vec);

  return 0;

}

