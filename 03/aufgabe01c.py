import numpy as np
import matplotlib.pyplot as plt

# barycentric coordinates of p (1, -7) in triangle a (0, 0), b (1, 5), c (-4, 4)


p = np.array([1, -7])
a = np.array([0, 0])
b = np.array([1, 5])
c = np.array([-4, 4])

# draw points a, b, c
plt.plot(a[0], a[1], 'ro')
plt.plot(b[0], b[1], 'ro')
plt.plot(c[0], c[1], 'ro')

# draw line between a and b
plt.plot([a[0], b[0]], [a[1], b[1]], 'r-')

# draw line between b and c
plt.plot([b[0], c[0]], [b[1], c[1]], 'r-')

# draw line between c and a
plt.plot([c[0], a[0]], [c[1], a[1]], 'r-')

# add label to points
plt.text(a[0], a[1], 'a')
plt.text(b[0], b[1], 'b')
plt.text(c[0], c[1], 'c')

# draw point p
plt.plot(p[0], p[1], 'bo')
plt.text(p[0], p[1], 'p')

# draw triangle pbc and fill it with color
plt.fill([p[0], b[0], c[0]], [p[1], b[1], c[1]], 'r', alpha=0.2)

# draw triangle pca and fill it with color
plt.fill([p[0], c[0], a[0]], [p[1], c[1], a[1]], 'g', alpha=0.2)

# draw triangle pab and fill it with color
plt.fill([p[0], a[0], b[0]], [p[1], a[1], b[1]], 'b', alpha=0.2)

# A(pbc)
determinPBC = np.linalg.det(np.array([b-p, c-p]))
areaPBC = 0.5 * np.linalg.norm(determinPBC)
print("A(pbc) = ", areaPBC)

# A(pca)
determinPCA = np.linalg.det(np.array([c-p, a-p]))
areaPCA = 0.5 * np.linalg.norm(determinPCA)
print("A(pca) = ", areaPCA)

print(c-p)
print(a-p)

# A(pab)
determinPAB = np.linalg.det(np.array([a-p, b-p]))
areaPAB = 0.5 * np.linalg.norm(determinPAB)
print("A(pab) = ", areaPAB)

plt.show()