N = int(input())
R = int(input())
counter = 0

while N > R:
    N /= 2
    counter += 12

print(counter)
