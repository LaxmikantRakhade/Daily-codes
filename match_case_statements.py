
x = int (input("Enter the no(0/1/2/3/4) :"))
match x:
    case 0 :
        print ("x is zero")
    case 1 : 
        print ("x is one ")
    case 2  if (x%2==0): 
        print ("x is two")
    case 3 : 
        print ("x is three")
    case 4 :
        print ("x is four")
    case _:         # else condition /  defult case
                    # will only be matched if the above cases were not matched)
        print(x)





# marks = int (input ("Enter the marks (out of 3) : "))
# match marks :
#     case 0 :
#         print ("dummm !")
#     case 1 :
#         print ("Average !")
#     case 2 :
#         print ("Good ! ")
#     case 3 :
#         print ('Very good !')
#     case _:
#         print ("Thanks !")
    
    


