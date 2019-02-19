# On my honor, I have neither given nor recieved unauthorized aid
# This program is drawing a turtle with turtle

import turtle as t

t.mode("logo") # changes the angle directions so that they are normal cardinal directions
t.speed(10) # increased the drawing speed
t.colormode(255) # changed the color mode to RGB values
t.pensize(5) # changed the size of the pen
radius = 150
tempRadius = radius # temporary radius for drawing the pattern on the turtle shell
coords = [] # holds coordinates of the turtle when it reaches each 5th of the circle
headings = [] # holds the directions/orientations of the turtle when it reaches each 5hth of the circle

def start(): # this function is preparation for the rest of the program
	t.setheading(270) # sets the orientation to west
	t.penup() # stops drawing; "lifts the pen"
	t.goto((0,radius)) # goes to the given point; this is so the turtle/body of the turtle is centered
	t.ht() # hides the turtle icon
	t.pendown() # resumes drawing; "puts down the pen"

def body(): # draws the body of the turtle
	t.fillcolor("green") # fill color is green
	t.begin_fill() # where it knows to start to fill the shape
	for x in range(5): 
		# This if statement is drawing 5 segments of the shell.
		# This way, I can add the coordinates and headings of the turtle after  
		# Each segment is done so I can easily draw the limbs and head
		t.circle(radius,72,2)
		coords.append(t.pos())
		headings.append(t.heading())
	t.end_fill() # stops filling the shapes

def bodyParts():
	t.fillcolor(0,255,0) # fill color is pure green
	t.begin_fill()
	# This next for loop drawing the limbs using the coords. and headings stored in the lists mentioned before
	for x in range(5):
		if x is 4:
			t.setheading(headings[x])
			t.goto(coords[x])
			t.circle(-60)
		else:
			t.setheading(headings[x])
			t.goto(coords[x])
			t.circle(-75,360,7)
	t.end_fill()

def shellPattern():
	# do loop to make continuous pattern
	for x in range(6):
		global tempRadius # so the pattern can get smaller and smaller as it repeats, resembling a fractal
		tempRadius -= 30-(3*x)
		if x > 2:
			# when the for loop gets to drawing the 4th pattern, the stroke gets smaller
			# I did this so that you could see the pattern easier and be less bulky and cluttered
			t.pensize(3)
		#decagon pattern
		t.begin_fill()
		t.fillcolor("green")
		t.penup()
		t.goto(0,int(tempRadius))
		t.pendown()
		t.circle(tempRadius,360,10)
		t.end_fill()
		#pentagon pattern
		t.begin_fill()
		t.fillcolor(0,255,0)
		t.penup()
		t.goto(0,int(tempRadius))
		t.pendown()
		t.circle(tempRadius,360,5)
		t.end_fill()

def face():
	# draws the eyes on the head of the turtle 
	t.penup()
	t.goto(20,radius+100)
	t.pendown()
	t.begin_fill()
	t.fillcolor(0,0,0)
	t.left(45) # turns the ovals/eyes so that they line up straight
	talloval(10)
	t.penup()
	t.goto(-25,radius+100)
	t.pendown()
	talloval(10)
	t.end_fill()

# https://stackoverflow.com/questions/29465666/how-do-you-draw-an-ellipse-oval-in-turtle-graphics-python
def talloval(r):
	for loop in range(2):
		t.circle(r,90)
		t.circle(r/2,90)

start()
body()
bodyParts()
shellPattern()
face()
t.done()
