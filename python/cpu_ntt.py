import sys
import sympy

p = 1073750017
r = sympy.ntheory.primitive_root(p)
if len(sys.argv) < 2:
    print("You must enter a size for the vector! Please make it a power of 2")
    exit()
n = int(sys.argv[1])
vec = [i for i in range(n)]
#vec = [28,863448385,483161238,970875918,1073750013,102874091,590588771,210301624]
out = sympy.ntt(vec, p)
print(out)
