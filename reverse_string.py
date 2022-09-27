rev='' #declaring output variable
name=input("Insert your name\n") #insert imput
lenght=(len(name)) #calculating lenght of input
lenght=int(lenght) #inserting lenght to variable
i=lenght-1 #calculating I,the index


while i>=0: #checking if there is any input

    rev= rev+name[i]
    i=i-1 # backwards character becomes first character

print(rev) #end output