data = [
    (-1.0, (0, 1, 1), 0.8), # (z, color, alpha)
    (-0.2, (1, 1, 1), 0.5),
    (-0.3, (0, 1, 0), 1.0),
    (0.2, (0.1, 0.1, 0.1), 0.2),
    (0.6, (0.7, 0.8, 0.9), 0.2)
]

# sort data by high z value to low z value
data.sort(key=lambda x: x[0], reverse=True)

C_i = (1, 1, 1)

for (index, item) in enumerate(data):
    a_iXc_i = tuple(map(lambda x: x * item[2], item[1]))    # a_i * c_i
    a_a_iXC_i = tuple(map(lambda x: x * (1 - item[2]), C_i))    # (1 - a_i) * C_i
    
    C_i_new = tuple(map(lambda x, y: x + y, a_iXc_i, a_a_iXC_i))    # C_i = a_i * c_i + (1 - a_i) * C_i
    rounded_color = tuple(map(lambda x: round(x, 3), item[1]))
    rounded_C_i = tuple(map(lambda x: round(x, 3), C_i))
    rounded_C_i_new = tuple(map(lambda x: round(x, 3), C_i_new))
    subitem_string = f"C_{index + 1} = {round(item[2], 3)} \cdot {rounded_color} + (1 - {round(item[2], 3)}) \cdot {rounded_C_i} = {rounded_C_i_new}"
    C_i = C_i_new

    print(f"\\item $[z = {item[0]};\\ c = {item[1]};\\ \\alpha = {item[2]}]$")
    print(f"\\begin{'{itemize}'}\n    \\item ${subitem_string}$\n\\end{'{itemize}'}")

print(tuple(map(lambda x: round(x, 3), C_i)))



