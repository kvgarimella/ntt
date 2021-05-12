import sys
import ntt
import torch


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Performing NTT on.......................", device)

if len(sys.argv) < 2:
    print("You must enter a size for the vector! Please make it a power of 2")
    exit()

n = int(sys.argv[1])
p = 1073750017
r = 5 


vec     = torch.arange(n, device=device)
outvec  = ntt.in_place_ntt(vec, p, r)
print(outvec)
