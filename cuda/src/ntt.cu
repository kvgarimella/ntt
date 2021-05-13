__device__ uint64_t modulo(int64_t base, int64_t m){
	int64_t result = base % m;

	return (result >= 0) ? result : result + m;
}

uint64_t modulo_cpu(int64_t base, int64_t m){
	int64_t result = base % m;

	return (result >= 0) ? result : result + m;
}

__device__ uint64_t modExp(uint64_t base, uint64_t exp, uint64_t m){

	uint64_t result = 1;
	
	while(exp > 0){

		if(exp % 2){

			result = modulo(result*base, m);

		}

		exp = exp >> 1;
		base = modulo(base*base,m);
	}

	return result;
}
uint64_t modExp_cpu(uint64_t base, uint64_t exp, uint64_t m){

	uint64_t result = 1;
	
	while(exp > 0){

		if(exp % 2){

			result = modulo_cpu(result*base, m);

		}

		exp = exp >> 1;
		base = modulo_cpu(base*base,m);
	}

	return result;
}


__global__ void inner_loop(uint64_t *result, uint64_t n, uint64_t p, uint64_t m, uint64_t a, uint64_t batch){
    uint64_t factor1, factor2;

    int idx = threadIdx.x;
    int j = m*blockIdx.x;
    int k = blockIdx.y;
    if ((j + k + m/2 + idx*n) < n*batch){ 

				factor1 = result[j + k + idx * n];
				factor2 = modulo(modExp(a,k,p)*result[j + k + m/2 + idx * n],p);

			
				result[j + k + idx * n] 		= modulo(factor1 + factor2, p);
				result[j + k+m/2 + idx * n] 	= modulo(factor1 - factor2, p);
   } 

}

__host__ void inPlaceNTT_DIT(uint64_t *result, uint64_t n, uint64_t p, uint64_t r, bool rev, uint64_t batch){

	uint64_t m, k_, a;
	for(uint64_t i = 1; i <= log2(n); i++){ 

		m = pow(2,i);
		k_ = (p - 1)/m;
		a = modExp_cpu(r,k_,p);
        dim3 blocks(n/m, m/2, 1);
        dim3 threads(batch, 1, 1);
        inner_loop<<<blocks, threads>>>(result,n,p,m,a,batch); 
	}
}


