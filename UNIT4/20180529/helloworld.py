from turtle import TK

root = TK.Tk()
canvas = TK.Canvas(root, width=500, height=500, bg="#ddffff")
canvas.pack()
canvas.create_text(200, 250, fill="darkblue", font="Times 20", text="Hello World!")

TK.mainloop()
