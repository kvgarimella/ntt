import sympy

p = 1073750017
r = sympy.ntheory.primitive_root(p)

vec = [i for i in range(8)]

out = sympy.ntt(vec, p)
print(out)
