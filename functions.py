# a = 10
# b = 5
# sum = a+b
# print (sum)

# c = 4
# d = 6
# sum = c+d 
# print (sum)

# def CalculateMean (a,b):
#     mean = (a+b)/2
#     print (mean)

# a = 25
# b = 1
# if (a and b > 5):
#     CalculateMean(a,b)
# else :
#     print ("done")

# c = 250
# d  = 250
# if (c and d > 5):
#     CalculateMean(c,d)
# else :
#     print ("done")
#     CalculateMean(c,d)



def CalculateGMean(a,b):
    GMean = (a*b)/(a+b)
    print("The geometric mean is : ",GMean)

def CalculateMinMax(a,b):
    if (a>b):
        print (a,"is greater !")
    elif (b>a):
        print (b, "is greater !")
    else:
        print (a,'=',b, "a and b are equal !")

a = int (input ("Enter a first number : "))
b = int (input ("Enter a second number : "))
CalculateMinMax(a,b)
CalculateGMean(a,b)
