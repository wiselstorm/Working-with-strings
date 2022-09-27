
i=0 #inicialization
word=input("Write your character to remove spaces\n")
fullword=""
for char in word:  #traversing

    if char !=' ' : #if char has white space
        znak = word[i]  # add sign to variable
        i+=1
znak=word.replace(' ','') #replace all spaces with no space
fullword+=znak #add sign to new code


print (fullword)