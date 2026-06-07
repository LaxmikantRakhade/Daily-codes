# name = "Shrikant"
# for letters in name :
#     print(letters,end=", ")

# colors = ["black","white","pink","yellow","green","brown","red"]
# for color in colors:
#     print (color)
#     for i in color:
#         print (i) 


# # range function

# for number in range(10):
#     print (number+1) 

# for number in range (1,11):
#     print (number)


# for number in range (1,10,2):
#     print (number)


# games = ["cricket","tennis","hocky"]
# for game in games: 
#     print (game, end="\n")
#     for alphabates in game:
#         print (alphabates, end ="\n")

# # print number from 1 to 10
# for number in range (10):
#     print (number+1)

# print even number from 1 to 10
# for number in range (1,11):
#     if(number%2==0):
#         print (number)
# OR.  (0 to 10)
# for number in range (0,11,2):
#     print (number)

# print odd number from 1 to 10
# for number in range (10):
#     if(number%2!=0):
#         print (number)

# print sum of first 10 natural numbers 
# sum = 0 
# for number in range (1,11):
#     sum = sum + number
#     print (sum)

# print multipliaction table of 5 
# for number in range (5,51,5):
#     print (number)
# OR
# for number in range (1,11):
#     print("5 *", number,"=",number*5)

# find factorial of 5 
# factorial  = 1
# for number in range (1,6):
#     factorial = factorial * number
#     print (factorial)

# count digits in a number 
# number = 9075237838
# count = 0
# for digit in str(number):
#     count = count + 1
#     print (count)

# reverse a string 
# name = "motu"            # length of name = 4
# for alphabates in range(len(name)-1,-1,-1):
#     print (name[alphabates])

# patterns 
# for i in range (1,6):
#     print (i*" *")

# print ("\n")

# for i in range (6-1,-1,-1):
#     print (i*" *")
# print ("\n")

# # square pattern
# for i in range (1,6):
#     print (5*' *')


# prime number check
# num = int (input("enter a number : "))
# if num >1:
#     for i in range (2,num):
#         if (num % i) == 0:
#             print ('number is not prime !')
#             break
#     else:
#         print ('number is prime!')
# else: 
#     print ("number is not prime !")

# fibonacci series
# num1 = 0
# num2 = 1
# for i in range (100):     # 100 iterations f100th value 
#     print (num1,end=" ")
#     num1 , num2 = num2 , num1 + num2 

# find largest number in a list
numbers = [10,35,5,64,25,7,9,11]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print (largest)
