from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# importing all necessary packeges
import RPi.GPIO as gpio
import sys
import time

user_input1 = []


def index(request):
	return render(request, "p1.html")


def buy(request):
	main(user_input1)
	htm="<center><h3><b>Total Buyed Products<br>"
	htm2="<center><b>~Thank You~</b></center>"
	return HttpResponse(htm+str(len(user_input1))+"</b></h3></center>"+htm2)

def submit(request):
	user_input = []
	a = []
	price = 0
	for i in range(1, 16):

		try:
			user_input.append(request.POST[str(i)])

		except:
			pass

	try:

		if request.POST["1"]:
			a.append("Milk")
			price += 21

	except:
		pass

	try:
		if request.POST["2"]:
			a.append("Chips")
			price = price + 10
	except:
		pass
	try:
		if request.POST["3"]:
			a.append("Chocolate")
			price = price + 10
	except:
		pass

	try:
		if request.POST["4"]:
			a.append("Pen")
			price = price + 5
	except:
		pass

	try:
		if request.POST["5"]:
			a.append("Soap")
			price = price + 50

	except:
		pass

	try:
		if request.POST["6"]:
			a.append("FaceWash")
			price = price + 45
	except:
		pass

	try:
		if request.POST["7"]:
			a.append("Tea")
			price = price + 40

	except:
		pass

	try:
		if request.POST["8"]:
			a.append("Perfume")
			price = price + 75
	except:
		pass

	try:
		if request.POST["9"]:
			a.append("Pepsi")
			price = price + 25
	except:
		pass

	try:
		if request.POST["10"]:
			a.append("Water Bottle")
			price = price + 15

	except:
		pass

	try:
		if request.POST["11"]:
			a.append("Biscuit")
			price = price + 10

	except:
		pass

	try:
		if request.POST["12"]:
			a.append("Colgate")
			price = price + 39

	except:
		pass

	try:
		if request.POST["13"]:
			a.append("Shampoo")
			price = price + 35
	except:
		pass

	try:
		if request.POST["14"]:
			a.append("Glue")
			price = price + 10

	except:
		pass
	try:
		if request.POST["15"]:
			a.append("Soup")
			price = price + 25
	except:
		pass

	print(user_input)
	print(a)
	for item in user_input: user_input1.append(item)
	return render(request, 'product_details.html', {'list': a, 'price': price})


# Initialization of GPIO pins
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




# Defining Main function
def main(user_input1):
	product_lane1 = (0, 2, 4, 6)
	product_lane2 = (8, 10, 12, 14)
	product_lane3 = (16, 18, 20, 22)
	product_lane4 = (24, 26, 28, 30)
	turn = [6, 14, 22]
	user_input = [int(i) for i in user_input1]
	print("Passed in main" + str(user_input))
	trolly_location = 0
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

