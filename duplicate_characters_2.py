word=input("Input a word\n") #user input
user_list= list(word) #create  list from input
duplicates=[] #empty array of the end result


for char in user_list:  #iterate through string
    if((user_list.count(char)>1 )and (char not in duplicates)): #if char is bigger than one and char not in duplicates
        duplicates.append(char) #appends the chars following the condition to one variable


print (duplicates) #print of end result


