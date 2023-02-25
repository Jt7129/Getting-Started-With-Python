#Let's accept input and add a choice
print("Enter a Word")
word = input("Enter Word Here then press enter: ")
print("Your Word is",word.capitalize(),"Correct?")
answer = input("[Y/N]:")

if answer == "y":
    print("I guessed it!")

elif answer == "n": 
    print("I guess i was wrong")

else:
    print("You did not answer correctly")
    
