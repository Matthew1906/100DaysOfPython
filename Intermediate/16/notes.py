# Object Oriented -> Simple Relations
# Objects = real world Object
# Objects has attributes (variables, associated with the object)
# and methods (functions, what the object can do)

# class = blueprint of objects -> pascal case
# object hte actual thing that we are using

# import a module -> add graphics to the screen

from turtle import Turtle,Screen
# check the documentation

# create a new object from turtle
timmy = Turtle()
timmy.shape("turtle") #change the shape
timmy.color("coral","green") #border, fill
timmy.forward(100) #move forward
# print(timmy) -> an object

# accessing attribute -> object.attribute
my_screen = Screen()
# print(my_screen.canvheight) # height of the screen
# print(my_screen.canvwidth) #width of the screen

# accessing methods -> object.method()
my_screen.exitonclick() # running until we click on the screen

# creating table -> hard
# import prettytable

import prettytable as pt

# look at the documentation
table = pt.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle","Charmander"], align = "c", valign="t")
table.add_column("Type", ["Electric", "Water","Fire"], align='l', valign = "b")
print(table)

