import turtle

c1 = input('First colour: ')
c2 = input('Second colour: ')
pencolour ("black")
fillcolor(c1)
begin_fill()
forward (200)
left (90)
forward (100)
left (90)
forward (200)
left (90)
forward (100)
end_fill()
backward (50)
pencolor(c2)
fillcolor(c2)
begin_fill()
left (90)
forward (200)
penup()
right(90)
forward(50)
right(90)
forward(200)
right(90)
forward(50)
end_fill()
