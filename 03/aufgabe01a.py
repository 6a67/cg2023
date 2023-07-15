# calculate frustum matrix with fovx of 90° and fovy of 60°
# near plane n is 21 and far plane f is 6000

import numpy as np
import math
import fractions

fovx = 90
fovy = 60
n = 21
f = 6000

# calculate the width and height of the near plane
h = n * math.tan(math.radians(fovy) / 2)
r = n * math.tan(math.radians(fovx) / 2)

# calculate the projection matrix
frustum = np.array([
    [n / r, 0, 0, 0],
    [0, n / h, 0, 0],
    [0, 0, -(f + n) / (f - n), -2 * f * n / (f - n)],
    [0, 0, -1, 0]
])

# print the result with fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
print(frustum)

# print bottom left corner of the near plane
# center of plane is (0,0,n)
# bottom left is then (-r,-h,n)
print("bottom left corner of the near plane: (-r,-h,n)")
print("r: " + str(-r))
print("h: " + str(-h))
print("n: " + str(n))

near_bottom_left = np.array([-r, -h, n, 1])

# print bottom top right corner of the far plane
# center of plane is (0,0,-f)

# calculate the width and height of the far plane
h = f * math.tan(math.radians(fovy) / 2)
r = f * math.tan(math.radians(fovx) / 2)

# top right is then (r,h,f)
print("top right corner of the far plane: (r,h,f)")
print("r: " + str(r))
print("h: " + str(h))
print("f: " + str(f))

far_top_right = np.array([r, h, f, 1])

# apply frustum matrix to the points
near_bottom_left = np.dot(frustum, near_bottom_left)
far_top_right = np.dot(frustum, far_top_right)

# dehomogenize the points
near_bottom_left = near_bottom_left / near_bottom_left[3]
far_top_right = far_top_right / far_top_right[3]

# print the result
print("bottom left corner of the near plane after applying the frustum matrix:")
print(near_bottom_left)

print("top right corner of the far plane after applying the frustum matrix:")
print(far_top_right)


