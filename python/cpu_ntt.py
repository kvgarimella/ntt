import sys
import sympy

p = 1073750017
r = sympy.ntheory.primitive_root(p)
if len(sys.argv) < 2:
    print("You must enter a size for the vector! Please make it a power of 2")
    exit()
n = int(sys.argv[1])
vec = [i for i in range(n)]

out = sympy.ntt(vec, p)
print(out)
