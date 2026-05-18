a=int(input("Enter First Number :- "))
b=int(input("Enter Second Number :- "))
c=int(input("Enter Third Number :- "))
if a==b and a==c:
    print("All Numbers are Equal")
elif a>=b and a>=c:
    print(a, "is the Largest Number")
elif b>=a and b>=c:
    print(b, "is the Largest Number")
else:
    print(c, "is the Largest Number")
