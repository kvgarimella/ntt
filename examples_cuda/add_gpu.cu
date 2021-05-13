#include <iostream>
#include <math.h>

// iterates over list of floats x and y
// adds x + y -> y
void add(int n, float *x, float *y)
{
    for (int i = 0; i < n; i++)
        y[i] = x[i] + y[i];
}

__global__
void add_gpu(int n, float *x, float *y)
{
    int idx = blockIdx.x * blockDim.x + threadIdx.x; 
    if (idx < n)
    {
        y[idx] = x[idx] + y[idx];
    }
}

int main(void)
{
    int N = 32; // basically 1mil 
    printf("Number of elements: %d\n", N);

    float *x;
    float *y;
    x = (float *) malloc(N * sizeof(float));
    y = (float *) malloc(N * sizeof(float));

    for (int i = 0; i < N; i++)
    {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    float *x_gpu, *y_gpu;
    cudaMalloc((void **) &x_gpu, N * sizeof(float));
    cudaMalloc((void **) &y_gpu, N * sizeof(float));
    cudaMemcpy(x_gpu, x, N*sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(y_gpu, y, N*sizeof(float), cudaMemcpyHostToDevice);



    // numbers in triple brackets will parameterize GPU usage for function call
    // lets change <<<1,1>>> to <<<1,256>>> i.e. increase thread to 256
    // must be a multiple of 32
    add_gpu<<<2,16>>>(N, x_gpu, y_gpu);
    //add(N, x, y);

    cudaMemcpy(y, y_gpu, N*sizeof(float), cudaMemcpyDeviceToHost);
    float maxError = 0.0f;
    for (int i = 0; i < N; i++)
        maxError = fmax(maxError, fabs(y[i] - 3.0f));

    printf("Max error: %f\n", maxError);
    for (int i = 0; i < N; i++)
        printf("%f, ", y[i]);
    printf("\n");

    cudaFree(x_gpu);
    cudaFree(y_gpu);
    free(x);
    free(y);

    return 0;
}
