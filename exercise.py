import turtle
import math
def arc(ang):
    for i in range(ang//5):
        bob.fd(5)
        bob.lt(5)
def pettle():
    arc(60)
    bob.lt(120)
    arc(60)
    bob.lt(120)
def flower(p_count):
    ang = 360//p_count
    r_pi = 0
    g_pi = math.pi / 2
    b_pi = math.pi
    w_pi = 2*math.pi / p_count
    for i in range(p_count):
        bob.color((130+math.cos(r_pi+i*w_pi)*80)/255, (130+math.cos(g_pi+i*w_pi)*80)/255, (130+math.cos(b_pi+i*w_pi)*80)/255)
        pettle()
        bob.lt(ang)
        
bob = turtle.Turtle()
bob.speed(100)
bob.width(2)
flower(60)

turtle.mainloop()