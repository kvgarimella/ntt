'''
Inspiration from: # https://stackoverflow.com/questions/12681945/reversing-bits-of-python-integer
'''

import torch
LUT0  = torch.load("bit_reversal_tables/LUT0.pt")
LUT1  = torch.load("bit_reversal_tables/LUT1.pt")
LUT2  = torch.load("bit_reversal_tables/LUT2.pt")
LUT3  = torch.load("bit_reversal_tables/LUT3.pt")
LUT4  = torch.load("bit_reversal_tables/LUT4.pt")
LUT5  = torch.load("bit_reversal_tables/LUT5.pt")
LUT6  = torch.load("bit_reversal_tables/LUT6.pt")
LUT7  = torch.load("bit_reversal_tables/LUT7.pt")
LUT8  = torch.load("bit_reversal_tables/LUT8.pt")
LUT9  = torch.load("bit_reversal_tables/LUT9.pt")
LUT10 = torch.load("bit_reversal_tables/LUT10.pt")
LUT11 = torch.load("bit_reversal_tables/LUT11.pt")
LUT12 = torch.load("bit_reversal_tables/LUT12.pt")

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
    result = base % m
    if result >= 0:
        return result
    return result + m

def mod_exp(base, exp, m):
    result = 1
    while (exp > 0):
        if (exp % 2):
            result = modulo(result * base, m)
        exp = exp >> 1
        base = modulo(base*base, m)
    return result
