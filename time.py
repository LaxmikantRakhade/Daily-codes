# """Create a python program capable of greeting you with Good Morning, 
# Good Afternoon and Good Evening. 
# Your program should use time module to get the current hour.  """

# import time
# timestamp = time.strftime("%H:%M:%S")   # strftime: string format time 

# print(timestamp)
# print (time.strftime("%H"))
# print (time.strftime("%M"))  
# print (time.strftime("%S"))

# if(6<int(time.strftime("%H"))<12):      #  if(6<int(time.strftime("%H"))<12):  
#     print ("Good Morning")              #  "%H" its string so typecast int use

# elif (18<int(time.strftime("%H"))<6):
#     print ("Good Night")

# else: 
#     print ("Good Afternon")

# # explanation: https://chatgpt.com/share/69be7c47-7cd8-800b-8cba-738483c30a63




















import time
timestamp = time.strftime('%H:%M:%S')
print (timestamp)












