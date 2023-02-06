import  turtle
import  time
def myfun():
    colors=["red","blue","green","yellow","orange","brown"]
    t=turtle
    t.pensize(5)
    t.bgcolor('black')
    t.speed(1000)
    for x in range(360):
        t.pencolor(colors[x%len(colors)])
        t.pensize(x/50)
        t.forward(x)
        t.left(59)
myfun()
time.sleep(4)