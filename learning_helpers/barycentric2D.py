import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# define points
p = np.array([1, 1])
a = np.array([0, 0])
b = np.array([2, 0])
c = np.array([1, 2])

#############################################

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

# A(abc)
determinABC = np.linalg.det(np.array([b-a, c-a]))
areaABC = 0.5 * determinABC
print("A(abc) = ", Fraction(areaABC).limit_denominator())

# A(pbc)
determinPBC = np.linalg.det(np.array([b-p, c-p]))
areaPBC = 0.5 * determinPBC
print("A(pbc) = ", Fraction(areaPBC).limit_denominator())

# A(pca)
determinPCA = np.linalg.det(np.array([c-p, a-p]))
areaPCA = 0.5 * determinPCA
print("A(pca) = ", Fraction(areaPCA).limit_denominator())

# A(pab)
determinPAB = np.linalg.det(np.array([a-p, b-p]))
areaPAB = 0.5 * determinPAB
print("A(pab) = ", Fraction(areaPAB).limit_denominator())

print("="*20)


print("alpha = ", Fraction(areaPBC/areaABC).limit_denominator())
print("beta = ", Fraction(areaPCA/areaABC).limit_denominator())
print("gamma = ", Fraction(areaPAB/areaABC).limit_denominator())

plt.show()