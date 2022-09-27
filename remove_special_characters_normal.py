x="" # #declaring output word
word=input("State your name\n") #input



 for char in word: #Iteration through all the input
     if  ord(char) in range(33,64): #if in range of 33 till 64 ASCI code
         x=word.replace(char,"") #replace char with blank space



print (x) #print the output
