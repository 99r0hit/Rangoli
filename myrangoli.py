#Rangoli by Rohit

#we need to import turtle to draw rangoli

import turtle

#tn is name to turtle

tn=turtle.Turtle()

'''for drawing design,
square and circle are two things'''

tn.speed(1) #define speed
tn.color('red')

'''
with goto command move turtle
for square
'''

tn.goto(0,100)
tn.goto(-100,100)
tn.goto(-100,0)
tn.goto(0,0)
tn.hideturtle()#hideturtle use to hide arrow

'''
tc is another turtle
to draw circles

'''
tc=turtle.Turtle()
tc.speed(10)

#First circle

tc.color('green')
rad=50
tc.circle(rad)
tc.color('red')
tc.goto(0,100)
tc.left(90)

#Second circle

tc.color('green')
rad=50
tc.circle(rad)
tc.color('red')
tc.goto(-100,100)
tc.left(90)

#Third circle

tc.color('green')
rad=50
tc.circle(rad)
tc.color('red')
tc.goto(-100,0)
tc.left(90)

#Fourth circle

tc.color('green')
tc.circle(rad)

#move turtle

tc.penup()
tc.goto(60,50)
tc.pendown()

'''
write '' HAPPY DIWALI '' text
'''

tc.color('purple')
tc.write('HAPPY')
tc.penup()
tc.goto(80,10)
tc.write('DIWALI')
tc.hideturtle()#hide turtle

'''
design is completed
need to click on screen to exit
'''

turtle.exitonclick()
