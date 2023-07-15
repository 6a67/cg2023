
n = 2**10 * 2**10
total_bytes = n

while n > 1:
    n = (n**0.5 / 2) ** 2
    total_bytes += n
    print(n)

print(total_bytes)
# additional bytes needed:
print(total_bytes - 2**20)