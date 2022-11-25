import random
import os


def getUserPoint(userName):
    try:
        inputFile = open("userScores.txt", "r")
        for line in inputFile:
            content = line.split(",")
            if content[0] == userName:
                inputFile.close()
                return content[1]
        inputFile.close()
        return "-1"
    except IOError:
        print("File Not Found. \n A new file will be created")
        inputFile = open("userScores.txt", "w")
        inputFile.close()
        return "-1"


def updateUserprofile(newUser, userName, score):
    if newUser:
        openFile = open("userScores.txt", "a")
        openFile.write('\n' + userName + ', ' + score)
        openFile.close()
    else:
        openFile = open("userScores.txt", "r")
        output = open("userScores.tmp", "w")
        for line in openFile:
            content = line.split(",")
            if content[0] == userName:
                content[1] = score
                line = content[0] + ", " + content[1] + "\n"
            output.write(line)
        openFile.close()
        output.close()
        os.remove("userScores.txt")
        os.rename("userScores.tmp", "userScores.txt")


def generateQuestion():
    operandList = [0, 0, 0, 0, 0]
    operatorList = ['', '', '', '']
    operatorDict = {
        1: "+",
        2: "-",
        3: "/",
        4: "*"
    }

    for lists in range(len(operandList)):
        operandList[lists] = random.randint(1, 9)

    for sym in range(len(operatorList)):
        if sym > 0 and operatorList[sym - 1] != '**':
            operatorList[sym] = operatorDict[random.randint(1, 4)]
        else:
            operatorList[sym] = operatorDict[random.randint(1, 3)]

    questionString = str(operandList[0])
    for num in range(1, 5):
        questionString = questionString + operatorList[num - 1] + str(operandList[num])
    result = eval(questionString)

    questionString = questionString.replace("**","^")
    print(questionString)
    userResult = input('Answer: ')

    while True:
        try:
            if int(userResult) == result:
                print("Excellent! You got it")
                return 1
            else:
                print("Sorry, Wrong Answer \n")
                print(result)
                return 0
        except Exception as e:
            print("You did not enter a number. Please try again")
            userResult = input('Answer: ')









