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
    int index  = blockIdx.x * blockDim.x + threadIdx.x;
    int stride = blockDim.x * gridDim.x;
    for (int i = index; i < n; i+= stride)
        y[i] = x[i] + y[i];
}

int main(void)
{
    int N = 1<<20; // basically 1mil 
    printf("Number of elements: %d\n", N);

    float *x;
    float *y;

    cudaMallocManaged(&x, N*sizeof(float));
    cudaMallocManaged(&y, N*sizeof(float));

    for (int i = 0; i < N; i++)
    {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }
    // numbers in triple brackets will parameterize GPU usage for function call
    int blockSize = 256;
    int numBlocks = (N + blockSize - 1) / blockSize;
    add_gpu<<<numBlocks, blockSize>>>(N, x, y);

    cudaDeviceSynchronize();

    float maxError = 0.0f;
    for (int i = 0; i < N; i++)
        maxError = fmax(maxError, fabs(y[i] - 3.0f));

    printf("Max error: %f\n", maxError);

    cudaFree(x);
    cudaFree(y);

    return 0;
}
