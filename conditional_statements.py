# if-elase statements 

# age = int (input("Enter your age : "))
# if (age >= 18):
#    print ("You can drive")
# else:
#    print ("You can't drive")
# print ("Thank You")

# MarksOfMotu = int(input ("Enter marks of motu :  "))
# MarksOfShrii = int(input ("Enter marks of Shrii :  "))

# if (MarksOfMotu>MarksOfShrii):
#    print ("Motu is smarter than Shrii")
# else :
#    print ("Shrii is smarter than Motu")

# elif statement

# number = float (input ("Enter a number : "))

# if (number > 0):
#     print (number," is positive number")
# elif (number == 0):
#     print (number," is nigther positive nor negative it's Zero")
# elif (number<0):
#     print(number," is negative number")
# else:
#     print ("Invalid input \n Plesase enter an integer value")
# print ("Thank You")

# Nested if statement
number = float (input ("Enter a number : "))

if (number > 0):
    if(10 < number < 20):
        print ("number is strongly positive ")
    elif (number > 20):
        print("number is most strongly postive")
    else:
        print (number," is positive number")

elif (number<0):
    if (-10 < number > 0):
        print("number is strongly negative")
    elif (-10 > number ):
        print ("number is most strongly negative")
    else:
        print ("number is negative")

else:
    print (number," is nigther positive nor negative it's Zero")
    


