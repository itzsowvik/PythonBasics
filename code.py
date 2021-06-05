secret_word = "sowvik"
guess = ""

while 1:
    guess = input("Enter Your Guess: ")
    if(guess != secret_word):
        print("Invalid Input: ")
        continue
    else:
        print("You Win!!")
        