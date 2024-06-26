import turtle as t

def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(300)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()

def circle(color):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(-70)
    t.end_fill()
    


t.up()
t.goto(-100,-200)
t.down()
t.goto(-100, 200)
rectangle('green')

t.goto(-100, 170)
t.color('green')
t.forward(150)
circle('red')

t.mainloop()