from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)


def nightdrawer():
    number = random.randrange(20, 50)
    colors = ['silver', 'grey', 'darkgray', 'lightgray', 'gainsboro', 'white']
    for i in range(number):
        x = random.randrange(10, 290)
        y = random.randrange(10, 290)
        size = random.randrange(2, 5)
        starry_box = canvas.create_rectangle((x-(size//2)), (y-(size//2)), (x+(size//2)), (y+(size//2)), fill = random.choice(colors))
nightdrawer()
root.mainloop()
