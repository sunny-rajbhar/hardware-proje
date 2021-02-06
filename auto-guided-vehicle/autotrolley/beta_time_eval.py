#importing all necessary packeges
import RPi.GPIO as gpio
import sys
import time

#Initialization of GPIO pins
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

#Forward function
#tf is time in sec.. which we will pass
def fwd(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

# Reverse function
def rev(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def right(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup

def wait(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup


#Defining Main function	
def main():
    product_lane1 = (0,2,4,6)
    product_lane2 = (8,10,12,14)
    product_lane3 = (16,18,20,22)
    product_lane4 = (24,26,28,30)
    turn = [6,14,22]
    trolly_location = 0
    user_input = []
    #user_input = [20,40,100]
    pro = input("Enter how many product you want?")
    print 'Enter Products'
    for i in range(int(pro)):
            a = input("Product:")
        user_input.append(int(a))
        print 'Products',user_input
    #-----------------------------------------
        # for loops for running
        # 1st for loop
    for product in product_lane1:
        #lane 1
        if product in user_input:
                        time = product-trolly_location
                    #print("\nRun(%d)"%time)
                        fwd(time)
                        wait(2.5)
                        trolly_location = product

        # 2nd for loop        
    for product in product_lane2:
        #lane 2
        if product in user_input:
            if trolly_location <= turn[0]:
                time = turn[0] - trolly_location
                #print("\nRun(%d)\nTurn"%time)
                fwd(time)
                right(0.63)
                                fwd(1.4)
                                right(0.55)
                trolly_location = turn[0] + 2
                time = product - trolly_location
                #print("\nRun(%d)"%time)
                fwd(time)
                wait(2.5)
                trolly_location = product
            else:
                time = product - trolly_location
                #print("\nRun(%d)"%time)
                fwd(time)
                wait(2.5)
                trolly_location = product

        # 3rd for loop
    for product in product_lane3:
        #lane 3
        if product in user_input:
            if trolly_location <= turn[0]:
                time = turn[0] - trolly_location
                trolly_location = turn[0] + 2
                #print("\nRun(%d)\nTurn"%time)
                fwd(time)
                right(0.63)
                fwd(1.4)
                right(0.55)
            if trolly_location <= turn[1]:
                            time = turn[1] - trolly_location
                            #print("\nRun(%d)\nTurn"%time)
                            fwd(time)
                            left(0.63)
                            fwd(1.4)
                            left(0.55)
                            trolly_location = turn[1] + 2
                            time = product - trolly_location
                            #print("\nRun(%d)"%time)
                            fwd(time)
                            wait(2.5)
                            trolly_location = product
            else:
                time = product - trolly_location
                #print("\nRun(%d)"%time)
                fwd(time)
                wait(2.5)
                trolly_location = product
        
        # 4th for loop
    for product in product_lane4:
        #lane 4
        if product in user_input:
            if trolly_location <= turn[0]:
                            time = turn[0] - trolly_location
                            
                #print("\nRun(%d)\nTurn"%time)
                            fwd(time)
                            right(0.63)
                            fwd(1.4)
                            right(0.55)
                            trolly_location = turn[0] + 2
            if trolly_location <= turn[1]:
                            time = turn[1] - trolly_location
                            #print("\nRun(%d)\nTurn"%time)
                            fwd(time)
                            left(0.63)
                            fwd(1.4)
                            left(0.55)
                            trolly_location = turn[1] + 2
                        if trolly_location <= turn[2]:
                time = turn[2] - trolly_location
                #print("\nRun(%d)\nTurn"%time)
                            fwd(time)
                            right(0.63)
                fwd(1.4)
                right(0.55)
                trolly_location = turn[2] + 2
                time = product-trolly_location
                #print("\nRun(%d)"%time)
                fwd(time)
                wait(2.5)
                trolly_location = product
            else:
                time = product - trolly_location
                #print("\nRun(%d)"%time)
                fwd(time)
                wait(2.5)
                trolly_location = product
    #----------------------------------------------------

# Calling main function	:)	
main()

