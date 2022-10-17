word=input("Enter a word\n")
condition=''
end_result=[]
new_condition=''
new_word=''
for x in word:
    condition=word[::-1] #holds the reversed world

    new_condition=condition.upper() #we upper both of our variables so they have equal size of caps so we can compare them without any concern
    new_word=word.upper()

if new_condition==new_word: #if reversed word is equal to inital word append it to variable end_result.
    end_result.append(condition)
    print("Input is a palindrome")

else:
        print("Input is not a palindrome")


print(new_word)
print(new_condition)