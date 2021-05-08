class Rectangle:
    def __init__(self, x, y, a, b, color):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas
        Changes a slice of the array with new values"""
        canvas.data[self.x: self.x + self.a, self.y: self.y + self.b] = self.color


class Square:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.a, self.y: self.y + self.a] = self.color

