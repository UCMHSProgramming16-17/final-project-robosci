sumlist = []
# Initialized list

while True:
    #Infinite while loop
    
    temp = input("Input element of list or \"break\" to print list\n : ")
    # Input prompt
    
    if temp == "break":
    # Detect break word used
    
        break
        #Break infinite loop
        
    sumlist.append(temp)
    # Append input string to list
    
print(sumlist)
# print list