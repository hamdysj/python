userInput = ""
started = False

while True:
    userInput = input("> ").upper()
    if userInput == "HELP":
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif userInput == "START":
        if started:
            print('Car is already started')
        else:
            print('Car started')
    elif userInput == "STOP":
        print('Car is already stopped!')
    elif userInput == "QUIT":
        break
    else:
        print('I dont understand that!')
