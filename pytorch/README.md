### NTT (PyTorch)

This directory contains our code for the NTT algorithm written using PyTorch. It supports vectors up to length 4096 and batch size up to 1024.
```bash
Usage: python main.py [Vector Size] [Batch Size]
```
Within the `src` directory, you may run:

```bash
>>> python main.py 8 16 
Device for loading bit reversal tables.. cuda
Performing NTT on....................... cuda
tensor([28,863448385,483161238,970875918,1073750013,102874091,
        590588771,210301624], device='cuda:0')
```

