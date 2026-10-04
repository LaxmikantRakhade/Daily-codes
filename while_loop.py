# i = 0
# while (i<5):
#     print (i)
#     i = i+1 


# number = int (input ("Enter a number : "))
# while (number<50):
#     number = int (input("Enter a number : "))
#     print (number)

# print ("done with the loop !")



# decrementing whilw loop
# number = 5 # -5
# while (number > 0):
#     print(number) 
#     number = number-1
# else:
#     print ("Done") 



# Print numbers from 1 to 100.

# count  = 1
# while count<=100:
#     print (count)
#     count+=1

# Print numbers from 100 to 1.

# count  = 100
# while count >= 1:
#     print (count)
    # count-=1

# Print the multiplication table of a number n.
# count = 1
# n = int (input("Enter a number : "))
# while count <=10:
#     print(n*count)
#     count += 1
# break;


# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# elements = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(len(elements))
# while index <= len(elements)-1:
#     print(elements[index])
#     index+=1
    
# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
numbers = (1, 4, 9, 16, 25, 36, 1, 49, 64, 81, 100)
x = int (input ("Enter a number :"))
index = 0
while index < len(numbers):
    if x == numbers[index] :
        print ("number is present  at index : ",index)
    else :
        print ("finding...")
    index+=1
