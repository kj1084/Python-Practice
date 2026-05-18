try:
    num=int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

try:
    print(10/0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")