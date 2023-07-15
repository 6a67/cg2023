import matplotlib.pyplot as plt

# Define the dimensions of the pixel raster
width = 40
height = 20

# Create an empty pixel raster
pixels = [[0 for y in range(height)] for x in range(width)]

# Define the two endpoints of the line
x0, y0 = 24, -9
x1, y1 = 27, 1

# Use Bresenham's algorithm to calculate the points on the line
dx = abs(x1 - x0)
dy = abs(y1 - y0)
sx = 1 if x0 < x1 else -1
sy = 1 if y0 < y1 else -1
err = dx - dy
x, y = x0, y0
points = [(x, y)]
while x != x1 or y != y1:
    e2 = 2 * err
    if e2 > -dy:
        err -= dy
        x += sx
    if e2 < dx:
        err += dx
        y += sy
    points.append((x, y))

# Set the pixel values on the line to 1
for x, y in points:
    pixels[x][y] = 1

# Display the pixel raster
plt.imshow(pixels, cmap='binary')
plt.show()
