for i in range (13):
    if (i == 10):
        break
    print (i+1,"x 5 =",(i+1)*5)
print ("left from the loop")


for i in range (15):
    if (i==10):
        print ("skip the iteration")
        continue
    print (i,"* 5 =",i*5)


# practice

for i in range (10):
    print (i+1,"x 10 = ",(i+1) * 10)
    
name = "Laxmikant"
for letters in name:
    print(letters)

number = int(input("Eenter an number : "))  
for i in range (10):
    print (number,'x ',i+1,'=',number*(i+1))







    