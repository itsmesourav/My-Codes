n = int(input("Enter the number:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if((i+j)<=n):
            print(end=" ")
        else:
            print("*", end=" ")
    print("")
for i in range(n-1,0,-1):
    for j in range(1, n+1):
        if((i+j)<=n):
            print(end=" ")
        else:
            print("*", end=" ")
    print("")