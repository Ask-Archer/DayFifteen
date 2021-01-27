from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
#.canvheight is an attribute
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
#this variable "table" is an object in the class pretty table

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander",])
table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
