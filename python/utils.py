'''
Inspiration from: # https://stackoverflow.com/questions/12681945/reversing-bits-of-python-integer
'''

import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device for loading bit reversal tables..", device)
LUT0  = torch.load("bit_reversal_tables/LUT0.pt").to(device);
LUT1  = torch.load("bit_reversal_tables/LUT1.pt").to(device);
LUT2  = torch.load("bit_reversal_tables/LUT2.pt").to(device);
LUT3  = torch.load("bit_reversal_tables/LUT3.pt").to(device);
LUT4  = torch.load("bit_reversal_tables/LUT4.pt").to(device);
LUT5  = torch.load("bit_reversal_tables/LUT5.pt").to(device);
LUT6  = torch.load("bit_reversal_tables/LUT6.pt").to(device);
LUT7  = torch.load("bit_reversal_tables/LUT7.pt").to(device);
LUT8  = torch.load("bit_reversal_tables/LUT8.pt").to(device);
LUT9  = torch.load("bit_reversal_tables/LUT9.pt").to(device);
LUT10 = torch.load("bit_reversal_tables/LUT10.pt").to(device);
LUT11 = torch.load("bit_reversal_tables/LUT11.pt").to(device);
LUT12 = torch.load("bit_reversal_tables/LUT12.pt").to(device);

def get_indices(array_size):
    if array_size == 1:
        return LUT0
    elif array_size == 2:
        return LUT1
    elif array_size == 4:
        return LUT2
    elif array_size == 8:
        return LUT3
    elif array_size == 16:
        return LUT4
    elif array_size == 32:
        return LUT5
    elif array_size == 64:
        return LUT6
    elif array_size == 128:
        return LUT7
    elif array_size == 256:
        return LUT8
    elif array_size == 512:
        return LUT9
    elif array_size == 1024:
        return LUT10
    elif array_size == 2048:
        return LUT11
    elif array_size == 4096:
        return LUT12


def bit_reverse(vec, n):
    result = torch.zeros_like(vec)
    result[get_indices(n)] = vec
    return result 

def modulo(base, m):
    """
    can use torch.remainder(base,m)
    """
    pass

def mod_exp(b,e,m):
    """
    Right-to-Left binary method
    https://en.wikipedia.org/wiki/Modular_exponentiation#Right-to-left_binary_method
    """
    r = torch.ones_like(b)
    b = torch.remainder(b,m)
    gtz = e > 0
    while torch.any(gtz):
        condition = (e[gtz] & 1).type(torch.bool).to(device)
        r[gtz] = torch.where(condition,torch.remainder(r[gtz]*b[gtz],m),r[gtz])
        e[gtz]>>=1
        b[gtz] = torch.remainder(b[gtz]**2, m)
        gtz = e > 0
    return r

def in_place_ntt(vec, p, r):
    LENVEC  = len(vec)
    HALFLEN = LENVEC // 2
    r       = torch.tensor([r]).to(device)
    LG2     = int(torch.log2(torch.tensor([LENVEC])))

    
    result  = bit_reverse(vec, LENVEC)
    for i in range(1,LG2+1):
        m  = torch.tensor([2**i])
        k_ = (p-1)//m
        a  = mod_exp(r, k_, p).repeat(HALFLEN)

        ks = torch.arange(2**(i-1))
        ks = ks.repeat(HALFLEN//len(ks))
        ks_exp = torch.clone(ks)

        js = torch.arange(0,LENVEC,2**i)
        js = js.repeat_interleave(HALFLEN // len(js))

        factor1 = result[js+ks]
        factor2 = torch.remainder(mod_exp(a,ks_exp,p)*result[js+ks+m//2],p)
        result[js+ks]      = torch.remainder(factor1+factor2,p)
        result[js+ks+m//2] = torch.remainder(factor1-factor2,p)
    return result
