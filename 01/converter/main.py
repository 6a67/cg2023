import svgpathtools
# import matplotlib.pyplot as plt
import json
import jsmin
import base64

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Load the SVG file
svg_file = "firefox.svg"
paths, attributes = svgpathtools.svg2paths(svg_file)

# Define the number of points to approximate each path with
num_points = 200

# Initialize min and max x and y values
min_x = min_y = float("inf")
max_x = max_y = float("-inf")

# Iterate over each path in the SVG file
for path in paths:
    # Approximate the path with a series of points
    points = []
    for i in range(num_points):
        point = path.point(i / (num_points - 1))
        points.append(point)

    # Update min and max x and y values
    for point in points:
        min_x = min(min_x, point.real)
        max_x = max(max_x, point.real)
        min_y = min(min_y, point.imag)
        max_y = max(max_y, point.imag)

# Compute scaling factors and translation values
scale_factor = 500 / max(max_x - min_x, max_y - min_y)
x_trans = -0.5 * (max_x + min_x) * scale_factor
y_trans = -0.5 * (max_y + min_y) * scale_factor

combined_points = []

# Iterate over each path in the SVG file again
for path in paths:
    # Approximate the path with a series of points
    points = []
    for i in range(num_points):
        point = path.point(i / (num_points - 1))
        points.append(point)

    # Scale and translate the points
    points = [(point.real * scale_factor + x_trans, point.imag * scale_factor + y_trans) for point in points]

    # Reverse the y coordinates
    points = [(point[0], -point[1]) for point in points]

    # Separate the x and y coordinates of the modified points
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    # Plot the points
    # plt.plot(x, y)

    combined_points += points

# Set the x and y limits
# plt.xlim(-250, 250)
# plt.ylim(-250, 250)

points = []

# Print points
for point in combined_points:
    # print(f"points.push(new Point({round(point[0],3)}, {round(point[1],3)}));")
    points.append(Point(round(point[0],3), round(point[1],3)))

# Create JSON with points
json_string = json.dumps([ob.__dict__ for ob in points])

# Minify json
json_string = jsmin.jsmin(json_string)

# Base64 encode json
json_string = base64.b64encode(json_string.encode('utf-8')).decode('utf-8')

print(f"atob(\"{json_string}\"),")


# Show the plot
# plt.show()
