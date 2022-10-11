from threading import *
import time

class Calc():
    def sum(self):
        for i in range(3):
            print("The number is ", i)
            time.sleep(1)
    def double(self):
        for i in range(3):
            print("The triple of %d is" %(i), i*3)
            time.sleep(1)
    def square(self):
        for i in range(3):
            print("The square of %d is " %(i), i*i)
            time.sleep(1)

obj = Calc()
t1 = Thread(target=obj.sum)
t2 = Thread(target=obj.double)
t3 = Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()
time.sleep(0.2)

t1.join()
t2.join()
t3.join()




