import sys
import ntt
import math
import torch


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Performing NTT on.......................", device)

if len(sys.argv) < 3:
    print("You must enter a size for the vector and the number of vectors!")
    print("Please make the size of the vector to be a power of 2!")
    exit()

n = int(sys.argv[1])
d = int(sys.argv[2])

p = 1073750017
r = 5 
print(n,d)

vec = torch.arange(n, device=device)
vec = vec.repeat(d).reshape(d,n)
print(vec.shape)
#outvec  = ntt.in_place_ntt(vec, p, r)
#print(outvec)
