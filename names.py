nameList=[]                                        # define empty list                          # define empty list

while True:                                        # loop until true
    name=input("Input Student Name: ").lower()     # ask user input and puts name
    if name == "stop":                             # if name is stop then break
        break                                      # break
    nameList.append(name)                          # appends list
print ("Students:",nameList)    
                               

