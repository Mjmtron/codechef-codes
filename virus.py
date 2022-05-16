import turtle
t=turtle.Turtle ()
t.speed(10000)
turtle.color("black")
a=200
while a>0:
	t.right(a)
	t.forward(a*2)
	a-=1
turtle.mainloop()