import myPythonFunctions as my

try:
    username = input('Enter your username: ')
    userScore = int(my.getUserPoint(username))
    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False
    userChoice = 0
    while userChoice != "-1":
        userScore += my.generateQuestion()
        print("Current Score = ", userScore)
        userChoice = input('Enter -1 to end or 0 to continue: ')
    my.updateUserprofile(newUser, username, str(userScore))
except Exception as e:
    print("Error Occurred")
