import z3

l = z3.Real('l')
k = z3.Real('k')

eq1 = 11 == l * 18 + k * -3
eq2 = -8 == l * -14 + k * 4

s = z3.Solver()
s.add(eq1)
s.add(eq2)

if s.check() == z3.sat:
    m = s.model()
    l = m[l]
    k = m[k]

    print("Formula: {} * a + {} * b".format(l, k))
    print("With a = (18, -14) and b = (-3, 4)")