# NTT
This repo contains various implementations of NTT.

1. `cpp`     : cpu version in C++
2. `cuda`    : gpu version in Cuda  
3. `pytorch` : gpu (or cpu) version in PyTorch
4. `test`    : cpu version that calls the [sympy library](https://www.sympy.org/en/index.html)


## Authors:
1. Karthik Garimella
2. Jianqiao 'Cambridge' Mo
3. Nandan Jha

## Running on NYU Greene:
In order to run on **Greene**, run the following commands from a login node:
```bash
>>> sh request_gpu.sh
>>> . load_cuda.sh
```
