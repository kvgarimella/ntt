import torch
from utils import *
device = "cuda" if torch.cuda.is_available() else "cpu"

def in_place_ntt(vec, p, r):
    """
    input vec    : vector of numbers to perform NTT on
    input p      : prime
    input r      : primitive root of prime p -> sympy.primitive_root(p)
    output result: the number theoretic transformed vector
    """
    LENVEC  = len(vec)
    HALFLEN = LENVEC // 2
    r       = torch.tensor([r],device=device)
    LG2     = int(torch.log2(torch.tensor([float(LENVEC)])))
    ms      = 2**torch.arange(1,LG2+1,device=device)


    result  = bit_reverse(vec, LENVEC)
    for i in range(1,LG2+1):
        m  = ms[i-1]
        k_ = (p-1)//m
        a  = mod_exp(r, k_, p).repeat(HALFLEN)

        ks = torch.arange(2**(i-1),device=device)
        ks = ks.repeat(HALFLEN//len(ks))
        ks_exp = torch.clone(ks)

        js = torch.arange(0,LENVEC,2**i,device=device)
        js = js.repeat_interleave(HALFLEN // len(js))

        factor1 = result[js+ks]
        factor2 = torch.remainder(mod_exp(a,ks_exp,p)[...,None]*result[js+ks+m//2],p)
        result[js+ks]      = torch.remainder(factor1+factor2,p)
        result[js+ks+m//2] = torch.remainder(factor1-factor2,p)
    return result

