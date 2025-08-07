a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
d = int(input("Enter 4th number:"))

if(a>=b and a>=c and a>=d):
    print("1st number is largest:",a)
elif(b>=c and b>=d):
    print("2nd number is largest:",b)
elif(c>=d):
    print("3rd number is largest:",c)
else:
    print("4th number is largest:",d)
