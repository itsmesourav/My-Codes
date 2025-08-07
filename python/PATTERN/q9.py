n = 4
for x in range(n):
    px = 1
    print(" " * (n-x), end="")
    for y in range(x+1):
        print(px, end=" ")
        px = px * (x-y) // (y+1)
    print()
