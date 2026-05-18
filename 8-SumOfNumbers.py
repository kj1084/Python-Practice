num=int(input("Enter a number:- "))
total=0
expression=""
for i in range(1,num+1):
    total=total+i
    expression=expression+str(i)
    if i<num:
        expression = expression + "+"
print(expression, "=", total)