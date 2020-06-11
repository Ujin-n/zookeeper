length = int(input())
width = int(input())
height = int(input())

edges_sum = 4 * (length + width + height)
S = 2 * (length * width + length * height + width * height)
V = length * width * height

print(edges_sum)
print(S)
print(V)
