from random import randint, random
import turtle as t
from moves import request_moves
# import the modules moves, and random here.

t.speed(0)
t.title('Monster Movement Pattern')
t.up()

pixels_per_move = 40

# generate a random integer between 5 and 10 here (hint: randint() function in 'random' module) and
# assign number_of_segments to refer to it.
number_of_segments = randint(5, 10)

# call the request_moves() function in the moves module with number_of_segments as the argument and
# assign steps refer to the returned string.
steps = request_moves(number_of_segments)

# x and y store the coordinates at which the most recent circle was drawn:
x = 0
y = 0
t.fillcolor((random(), random(), random()))
# This following loop will draw all of the circles.
# remember that i contains the current move number and the i-th character
# of the string steps describes the current move.
#for i in range(len(steps)):
    # If this is the first step, or the current step is different from the previous step,
    # then change the fill colour to a new random colour.
    # (hint:  fillcolor() function in the turtle module, random() function in the 'random' module)
    #<write code yere>



    # adjust x or y depending on the i-th character of the steps string
    # by adding or subtracting pixels_per_move from either x or y.  For example, if
    # the i-th character of steps is 'u', then add pixels_per_move to y so that the next
    # circle drawn is above the previous one.
    #<write code yere>

for pos, i in enumerate(steps):
    if pos != 0 and steps[pos-1] != i:
        t.fillcolor((random(), random(), random()))
    if i == 'u':
        y += pixels_per_move
    elif i == 'd':
        y -= pixels_per_move
    elif i == 'r':
        x += pixels_per_move
    elif i == 'l':
        x -= pixels_per_move


    # draw a filled circle at location (x,y) with radius 15.  You'll need to use
    # turtle module functions for this such as goto(), down(), up(), begin_fill(),
    # end_fill(), and circle().  These are described in the assignment description.
    # Demo 2 in Lecture 06 also shows example usage of these functions.
    #<write code yere>
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.up()


t.done()
