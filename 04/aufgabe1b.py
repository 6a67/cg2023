import numpy as np
import aufgabe1a

s = 20

# half vector 1
h1 = (aufgabe1a.v + aufgabe1a.l1) / np.linalg.norm(aufgabe1a.v + aufgabe1a.l1)

print(f"h1:\n{h1}\n")

# half vector 2
h2 = (aufgabe1a.v + aufgabe1a.l2) / np.linalg.norm(aufgabe1a.v + aufgabe1a.l2)

print(f"h2:\n{h2}\n")

# ambient color 1
C_ambient1 = aufgabe1a.C_a

print(f"C_ambient1:\n{C_ambient1}\n")

# diffuse color 1
C_diffuse1 = aufgabe1a.C_diffuse1

print(f"C_diffuse1:\n{C_diffuse1}\n")

# specular color 1
C_specular1 = aufgabe1a.C_s * max(0, np.dot(h1, aufgabe1a.n) ** s)

print(f"C_specular1:\n{C_specular1}\n")

# color from first light source
C1 = (C_ambient1 + C_diffuse1 + C_specular1) * aufgabe1a.lightColor1

print(f"C1:\n{C1}\n")

# ambient color 2
C_ambient2 = aufgabe1a.C_a

print(f"C_ambient2:\n{C_ambient2}\n")

# diffuse color 2
C_diffuse2 = aufgabe1a.C_diffuse2

print(f"C_diffuse2:\n{C_diffuse2}\n")

# specular color 2
C_specular2 = aufgabe1a.C_s * max(0, np.dot(h2, aufgabe1a.n) ** s)

print(f"C_specular2:\n{C_specular2}\n")

# color from second light source
C2 = (C_ambient2 + C_diffuse2 + C_specular2) * aufgabe1a.lightColor2

print(f"C2:\n{C2}\n")

# final color
C = C1 + C2

C = np.array([C[0][0], C[1][1], C[2][2]])


print(f"Final result:\n{C}")