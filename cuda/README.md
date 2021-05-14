### NTT (Cuda C)

This directory contains our code for the NTT algorithm written using CUDA kernels. It supports vectors up to length 4096 and batch size up to 1024.
```bash
Usage: ./ntt [Vector Size] [Batch Size]
```
Within the `src` directory, you may run:

```bash
>>> make clean; make
>>> ./ntt 8 16
Original vector: [0,1,2,3,4,5,6,7,]
Final vector   : [28,863448385,483161238,970875918,1073750013,102874091,590588771,210301624,]
```

