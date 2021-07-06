import random
def computerWin():
    print("Computer win")
def userWin():
    print("User win")
print("Let's Play Rock Paper Scissors!")
options = ["r", "p", "s"]
computer_choice = random.choice(options)
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
if (user_choice == "r") and (computer_choice == "s"):
    print("User win")
elif (user_choice == "s") and (computer_choice == "r"):
    print("Computer win")
elif (user_choice == "s") and (computer_choice == "p"):
    print("User win")
elif (user_choice == "p") and (computer_choice == "s"):
    print("Computer win")
elif (user_choice == "p") and (computer_choice == "r"):
    print("User win")
elif (user_choice == "r") and (computer_choice == "p"):
    print("Computer win")
else :
     print(f"System error : {user_choice} and {computer_choice}")
reMatch = input("Lets play again [y/n]")