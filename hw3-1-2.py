#author CJP 9/29/2021
firstcardvalue = int(input("What the value of your first card? "))
secondcardvalue= int(input("What is the value of the second card? "))

if (firstcardvalue + secondcardvalue) <= 21:
    print("You are safe!")
else:
    print("Bust!")

