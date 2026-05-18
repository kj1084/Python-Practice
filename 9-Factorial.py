num = int(input("Enter a number :- "))
fact = 1
expression = ""
for i in range(1, num + 1):
    fact = fact * i
    expression = expression + str(i) 
print(expression, "=", fact)