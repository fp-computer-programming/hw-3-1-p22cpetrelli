number = int(input("Type a Number! "))
if number % 2 == 0:
    print("Number is divisable by 2")
elif number % 3 == 0:
    print("Number is divisable by 3")
elif number % 5 == 0:
    print("Number is divisable by 5")
else:
    print("Number is not divisable by 2, 3, or 5")