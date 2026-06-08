# 1)
# name = "Shrikant"
# for letters in name :
#     print(letters,end=", ")

# 2)
# colors = ["black","white","pink","yellow","green","brown","red"]
# for color in colors:
#     print (color)
#     for i in color:
#         print (i) 

# # range function

# 3)
# for number in range(10):
#     print (number+1) 

# 4)
# for number in range (1,11):
#     print (number)

# 5)
# for number in range (1,10,2):
#     print (number)

# 6)
# games = ["cricket","tennis","hocky"]
# for game in games: 
#     print (game, end="\n")
#     for alphabates in game:
#         print (alphabates, end ="\n")

# 7)  print number from 1 to 10
# for number in range (10):
#     print (number+1)

# 8)  print even number from 1 to 10
# for number in range (1,11):
#     if(number%2==0):
#         print (number)
# OR.  (0 to 10)
# for number in range (0,11,2):
#     print (number)

# 9)  print odd number from 1 to 10
# for number in range (10):
#     if(number%2!=0):
#         print (number)

# 10) print sum of first 10 natural numbers 
# sum = 0 
# for number in range (1,11):
#     sum = sum + number
#     print (sum)

# 11) print multipliaction table of 5 
# for number in range (5,51,5):
#     print (number)
# OR
# for number in range (1,11):
#     print("5 *", number,"=",number*5)

# 12) find factorial of 5 
# factorial  = 1
# for number in range (1,6):
#     factorial = factorial * number
#     print (factorial)

# 13)   count digits in a number 
# number = 9075237838
# count = 0
# for digit in str(number):
#     count = count + 1
#     print (count)

# 14)   reverse a string 
# name = "motu"            # length of name = 4
# for alphabates in range(len(name)-1,-1,-1):
#     print (name[alphabates])

# 15) patterns 
# for i in range (1,6):
#     print (i*" *")

# print ("\n")

# for i in range (6-1,-1,-1):
#     print (i*" *")
# print ("\n")

# # square pattern
# for i in range (1,6):
#     print (5*' *')


# 16) prime number check
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

# 17) fibonacci series
# num1 = 0
# num2 = 1
# for i in range (100):     # 100 iterations f100th value 
#     print (num1,end=" ")
#     num1 , num2 = num2 , num1 + num2 

# 18) find largest number in a list
# numbers = [10,35,5,64,25,7,9,11]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print (largest)

# 19) print numbers in a reverse order from 10 to 1
# for numbers in range (10,0,-1):
#     print (numbers)

# 20) count vowels in a string
# sentence= " i love panda "
# count = 0
# for charactors in sentence.lower():
#     if charactors in "aeiou":
#         count = count + 1 
# print (count)

