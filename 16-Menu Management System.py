menu=["Paneer Butter Masala","Dal Makhani","Kaju Kari","Masala Dosa","Idli Sambhar"]
print("Welcome to our restaurant!")
print("Here is our Menu:")
price={"Paneer Butter Masala": 250, "Dal Makhani": 200, "Kaju Kari": 300, "Masala Dosa": 150, "Idli Sambhar": 100}
for dish, cost in price.items():
        print(dish, ":", cost, "INR")
order=input("Please enter the dish you would like to order: ")
if order in menu:
        print("Thank you for your order! Your", order, "will be ready soon.")
else:
        print("Sorry, we don't have that dish on our menu. Please choose from the available options.")
while True:
    more=input("Would you like to order anything else? (yes/no) ")
    if more.lower()=="yes":
        order=input("Please enter the dish you would like to order: ")
        if order in menu:
            print("Thank you for your order! Your", order, "will be ready soon.")
        else:
            print("Sorry, we don't have that dish on our menu. Please choose from the available options.")
    elif more.lower()=="no":
        print("Thank you for dining with us! Have a great day!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
total_bill = 0
orders = []
orders.append(order)
for item in orders:
    total_bill = total_bill + price[item]
print("Total Bill =", total_bill)