print('Numbers from 1 to 10')

secretNum = 9
userGuess = ""
count = 0

while userGuess != secretNum:
    userGuess = int(input("Guess the number: "))
    count += 1
if userGuess == secretNum:
    print("Great! You did it!")
