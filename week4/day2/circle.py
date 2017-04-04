
class Circle():
    def __init__(self, canvas, x, y, size, color="Black"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.canvas = canvas

    def draw(self):
        x1 = self.x
        x2 = self.x + self.size
        y1 = self.y
        y2 = self.y + self.size
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color)
