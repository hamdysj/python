# Array: Is a container that holds multiple values of same type`
# Syntax: var = array(TypeCode, [elements])
# TypeCode: 'c' - Character, 'b' - Int, 'B' - Int, 'u' - Unicode Character, 'h' -  Int, 'H' - Int
# TypeCode:  'i' - Int, 'I' - Long, 'l' - Int, 'L' - Long, 'f' - float, 'd' - Float

from array import *

arr = array('i', [1, -3, 4, 2, 6])
for i in arr:
    print(i, end='')
print()

for i in range(1, 4):
    print(f'%d : {arr[i]}' % i)

arr.reverse()
arr.append(9)
arr.remove(-3)

arr1 = array('i', [])
arrSize = int(input('Enter size of array: '))
print('Enter %d elements ' % arrSize)
for i in range(arrSize):
    arrElem = int(input())
    arr1.append(arrElem)

for i in range(arrSize):
    print(arr1[i], end='')
