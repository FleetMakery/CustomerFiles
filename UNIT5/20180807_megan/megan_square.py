from turtle import TurtleScreen, RawTurtle, TK
root = TK.Tk()
cv1 = TK.Canvas(root, width=500, height=500, bg="#ddffff")
cv1.pack()
s1 = TurtleScreen(cv1)
s1.bgcolor("orange") 
p = RawTurtle(s1)
t = RawTurtle(s1)

p.begin_fill()
p.circle(60)
p.end_fill()

TK.mainloop()
