'''
Author: Karthik Garimella
Date  : May 04, 2021

References:
1. Bit Reversal Lookup Tables
2. Right-to-left Binary Modular Exponentation

[1]: https://stackoverflow.com/questions/12681945/reversing-bits-of-python-integer
[2]: https://en.wikipedia.org/wiki/Modular_exponentiation#Right-to-left_binary_method
'''

import torch
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device for loading bit reversal tables..", device)
#LUT0  = torch.load("bit_reversal_tables/LUT0.pt").to(device);
#LUT1  = torch.load("bit_reversal_tables/LUT1.pt").to(device);
#LUT2  = torch.load("bit_reversal_tables/LUT2.pt").to(device);
#LUT3  = torch.load("bit_reversal_tables/LUT3.pt").to(device);
#LUT4  = torch.load("bit_reversal_tables/LUT4.pt").to(device);
#LUT5  = torch.load("bit_reversal_tables/LUT5.pt").to(device);
#LUT6  = torch.load("bit_reversal_tables/LUT6.pt").to(device);
#LUT7  = torch.load("bit_reversal_tables/LUT7.pt").to(device);
#LUT8  = torch.load("bit_reversal_tables/LUT8.pt").to(device);
#LUT9  = torch.load("bit_reversal_tables/LUT9.pt").to(device);
#LUT10 = torch.load("bit_reversal_tables/LUT10.pt").to(device);
#LUT11 = torch.load("bit_reversal_tables/LUT11.pt").to(device);
#LUT12 = torch.load("bit_reversal_tables/LUT12.pt").to(device);

def get_indices(array_size):
    if array_size == 1:
        return torch.load("bit_reversal_tables/LUT0.pt").to(device)
    elif array_size == 2:
        return torch.load("bit_reversal_tables/LUT1.pt").to(device)
    elif array_size == 4:
        return torch.load("bit_reversal_tables/LUT2.pt").to(device)
    elif array_size == 8:
        return torch.load("bit_reversal_tables/LUT3.pt").to(device)
    elif array_size == 16:
        return torch.load("bit_reversal_tables/LUT4.pt").to(device)
    elif array_size == 32:
        return torch.load("bit_reversal_tables/LUT5.pt").to(device)
    elif array_size == 64:
        return torch.load("bit_reversal_tables/LUT6.pt").to(device)
    elif array_size == 128:
        return torch.load("bit_reversal_tables/LUT7.pt").to(device)
    elif array_size == 256:
        return torch.load("bit_reversal_tables/LUT8.pt").to(device)
    elif array_size == 512:
        return torch.load("bit_reversal_tables/LUT9.pt").to(device)
    elif array_size == 1024:
        return torch.load("bit_reversal_tables/LUT10.pt").to(device)
    elif array_size == 2048:
        return  torch.load("bit_reversal_tables/LUT11.pt").to(device)
    elif array_size == 4096:
        return torch.load("bit_reversal_tables/LUT12.pt").to(device)


def bit_reverse(vec, n):
    """
    input vec    : Vector of numbers
    input n      : Length of vector
    output result: vector with each element in bit-reversed position

    Uses a bit-reversal lookup table
    """
    result = torch.zeros_like(vec)
    result[get_indices(n)] = vec
    return result 

def modulo(base, m):
    """
    returns base (mod m)
    """
    return torch.remainder(base,m)

def mod_exp(b,e,m):
    """
    returns base^{exp} (mod m)
    WARNING: operates on e in place
    Uses right-to-left binary method
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

