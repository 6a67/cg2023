# phong shading
import numpy as np

# triangle vertices
c = np.array([1, 5, -7])
a = np.array([-4, 4, -7])
b = np.array([0, 0, -7])

# vertex normals
nC = np.array([0, 0, 1])
nA = np.array([-1, 0, 0])
nB = np.array([0, -1, 0])

# point
p = np.array([0, 3, -7])


# calculate barycentric coordinates, TODO: not 100% sure if this is correct

det_abc = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
A_abc = 0.5 * det_abc

det_pbc = (b[0] - p[0]) * (c[1] - p[1]) - (c[0] - p[0]) * (b[1] - p[1])
A_pbc = 0.5 * det_pbc

det_pca = (c[0] - p[0]) * (a[1] - p[1]) - (a[0] - p[0]) * (c[1] - p[1])
A_pca = 0.5 * det_pca

det_pab = (a[0] - p[0]) * (b[1] - p[1]) - (b[0] - p[0]) * (a[1] - p[1])
A_pab = 0.5 * det_pab

alpha = A_pbc / A_abc
beta = A_pca / A_abc
gamma = A_pab / A_abc


new_n = alpha * nA + beta * nB + gamma * nC

# plot triangle in 2d space
# import matplotlib.pyplot as plt
# plt.plot([a[0], b[0], c[0], a[0]], [a[1], b[1], c[1], a[1]])
# plt.plot(p[0], p[1], "o")
# plt.axis("equal")
# plt.show()

print(f"new_n:\n{new_n}\n")