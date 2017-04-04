class Ball():
    def __init__(self, canvas, x, y, size, color="Black"):
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 1
        self.size = size
        self.color = color
        self.canvas = canvas
        self.circle = None
        self.draw()

    def draw(self):
        x1 = self.x
        x2 = self.x + self.size
        y1 = self.y
        y2 = self.y + self.size
        self.circle = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color)

    def get_coord(self):
        coords = self.canvas.coords(self.circle)
        return { 'x':coords[0], 'y':coords[1]}

    def move(self):
        self.canvas.move(self.circle, self.dx, self.dy)
