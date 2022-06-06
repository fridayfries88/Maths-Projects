from asyncore import loop
from time import sleep

while True:
    
    print ("using the euclidean algorithm you can find the Greatest Common Divisor between 2 positive intagers")
    sleep(3)
    print ("type your first number in now")
    x = int(input())
    
    print ('type your second number in now')
    y = int(input())

    if(x < y):
        tempx = x
        tempy = y
        y = tempx
        x = tempy


    r = x % y
    res = x // y

    print(str(x) + " = " + str(y) + "(" + str(res) + ") + " + str(r)) 
    print("")


    if r == 0:
        print("the GCD is, " + str(y))
    else:
        prevr = r
        r = y % r
        res = y // prevr
        print(str(y) + " = " + str(prevr) + "(" + str(res) + ") + " + str(r)) 
        print("")

    while True:
        sleep(0.03)
        if r == 0:
            print("the GCD is, " + str(prevr))
            break
        else:
            prevprevr = prevr
            prevr = r
            r = prevprevr % prevr
            res = prevprevr // prevr
            print(str(prevprevr) + " = " + str(prevr) + "(" + str(res) + ") + " + str(r)) 
            print("")