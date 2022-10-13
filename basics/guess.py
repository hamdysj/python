guessNumber = 7
guessCount = 0
guessLoop = 2
while guessCount < guessLoop:
    guess = int(input("Guess: "))
    guessCount += 1
    if guess == guessNumber:
        print('You Win!')
        break
else:
    print('Sorry, Keep trying')