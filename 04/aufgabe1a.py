# phong lighting model
import numpy as np

eye = np.array([0, 0, 0])
light1 = np.array([0, 8, -24])
lightColor1 = np.array([0.5, 0, 0])
light2 = np.array([-16, 0, -16])
lightColor2 = np.array([0, 0.6, 0])

C_a = np.array([[0.2, 0, 0],
                [0, 0.2, 0],
                [0, 0, 0.2]])
C_d = np.array([[0.8, 0, 0],
                [0, 0.8, 0],
                [0, 0, 0.8]])
C_s = np.array([[0.4, 0, 0],
                [0, 0.4, 0],
                [0, 0, 0.4]])
s = 10

n = np.array([0, 0, 1])

x = np.array([0, 0, -32])

# view vector normalized
v = (eye - x) / np.linalg.norm(eye - x)

print(f"v:\n{v}\n")

# light vector 1 normalized
l1 = (light1 - x) / np.linalg.norm(light1 - x)

print(f"l1:\n{l1}\n")

# light vector 2 normalized
l2 = (light2 - x) / np.linalg.norm(light2 - x)

print(f"l2:\n{l2}\n")

# reflection vector 1
r1 = 2 * np.dot(n, l1) * n - l1

print(f"r1:\n{r1}\n")

# reflection vector 2
r2 = 2 * np.dot(n, l2) * n - l2

print(f"r2:\n{r2}\n")

# ambient color 1
C_ambient1 = C_a

print(f"C_ambient1:\n{C_ambient1}\n")

# diffuse color 1
C_diffuse1 = C_d * max(0, np.dot(l1, n))

print(f"C_diffuse1:\n{C_diffuse1}\n")

# specular color 1
C_specular1 = C_s * max(0, np.dot(v, r1) ** s)

print(f"C_specular1:\n{C_specular1}\n")

# color from first light source
C1 = (C_ambient1 + C_diffuse1 + C_specular1) * lightColor1

print(f"C1:\n{C1}\n")

# ambient color 2
C_ambient2 = C_a

print(f"C_ambient2:\n{C_ambient2}\n")

# diffuse color 2
C_diffuse2 = C_d * max(0, np.dot(l2, n))

print(f"C_diffuse2:\n{C_diffuse2}\n")

# specular color 2
C_specular2 = C_s * max(0, np.dot(v, r2) ** s)

print(f"C_specular2:\n{C_specular2}\n")

# color from second light source
C2 = (C_ambient2 + C_diffuse2 + C_specular2) * lightColor2

print(f"C2:\n{C2}\n")

# resulting color
C = C1 + C2

C = np.array([C[0][0], C[1][1], C[2][2]])

print(f"Final result:\n{C}")