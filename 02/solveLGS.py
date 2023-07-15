import z3

# create variables v1, v2, and v3
v1 = z3.Int('v1')
v2 = z3.Int('v2')
v3 = z3.Int('v3')

# create the equation to be solved
eq = - v1**2 - v1 - v2**2 - v3**2 + 8*v2 + 7*v3 == 0

# create a solver object and add the equation
s = z3.Solver()
s.add(eq)

# check all possible solutions
while s.check() == z3.sat:
    m = s.model()
    print(f"""\\begin{"{pmatrix}"}
    {m[v1]} \\\\ {m[v2]} \\\\ {m[v3]}
\\end{"{pmatrix}"},""")
    # print(m)
    s.add(z3.Or(v1 != m[v1], v2 != m[v2], v3 != m[v3]))

