#while - used to repeat a section of code unknown number of times until a specific condition is met
#i = 0
#sum = 0
#while i<=10:
#    if i%2 == 0:
#        sum = sum + i
#    i += 1
#print(sum)


#To print a number in reverse order
#value = int(input('Enter an Number: '))
#nv = 0
#while value%10 != 0:
#    nValue = value%10
 #   nv = nv*10 + nValue
 #   value = value//10
#print(nv)

#To get the length of a string without using len function
### Bonus: To extract the last number of a digit, we find the remainder of the digit by dividing it by 10 - num%10

#Exercise 3
#x = [3,"gift",'for','you']
#i = 0
#length = 0
#try:
 #   while x[i]:
 #       length += 1
 #       i+=1
# except IndexError:
#    print(f'List Length is {length}')

#Exercise 4
#n = int(input('Enter a number: '))
#i = 0
#while i<=n:
#        j = 0
#        while j<=i:
  #              print(i,end='')
  #              j+=1
   #     i += 1
  #      print()

#Exercise 5
import random
pnum = random.randint(10,99)
n = int(input('Enter your guessed number: '))
print(pnum)


while n != 10:
    tnum = pnum
    ans = 0
    while tnum%10:
        numA = tnum%10
        nA = n%10
        tnum = tnum//10
        n = n//10
        if numA == nA:
            ans = ans + 1
    if ans == 2:
        print('Congrats! You guessed it right')
        break
    else :
        print('You guessed %d digits correctly' %(ans))
        n = int(input('Enter your guessed number: '))
else:
    print('You quit the game')











