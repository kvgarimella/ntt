#include <iostream>
#include <math.h>

// iterates over list of floats x and y
// adds x + y -> y
void add(int n, float *x, float *y)
{
    for (int i = 0; i < n; i++)
        y[i] = x[i] + y[i];
}

int main(void)
{
    int N = 32; 
    printf("Number of elements: %d\n", N);

    float *x = new float[N];
    float *y = new float[N];

    for (int i = 0; i < N; i++)
    {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    add(N, x, y);

    float maxError = 0.0f;
    for (int i = 0; i < N; i++)
        maxError = fmax(maxError, fabs(y[i] - 3.0f));

    printf("Max error: %f\n", maxError);

    delete [] x;
    delete [] y;


    return 0;
}
