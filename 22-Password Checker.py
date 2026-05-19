easy = [
    "1234",
    "123456",
    "password",
    "qwerty",
    "admin",
    "0000"
]
password=input("Enter your Password:")
while True:
    if password in easy:
        print("Your password is too easy")
    elif len(str(password))<8:
        print("Your password is too short")
    elif len(str(password))>16:
        print("Your password is too long")
    else:
        print("Your password is perfect")
        break
    password=input("Enter your Password:")