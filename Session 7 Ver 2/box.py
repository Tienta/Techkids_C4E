class Box:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def calc_next(self,dx,dy):
        return self.x + dx, self.y + dy

    def match(self,x,y):
        return self.x == x and self.y == y