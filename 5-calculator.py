num1=int(input("Enter Frist Number :- "))
num2=int(input("Enter Second Number :- "))
op=input("Enter Oprator :- ")
if op=="+":
    print("Result:",num1, op, num2, "=", num1+num2)
elif op=="-":
    print("Result:",num1, op, num2, "=", num1-num2)
elif op=="*":
    print("Result:",num1, op, num2, "=", num1*num2)
elif op=="/":
    print("Result:",num1, op, num2, "=", num1/num2)
else:
    print("Invalid Oprator")