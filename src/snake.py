from direction import Direction
from part import Part


class Snake:

    def __init__(self):
        # When start game snake spawn moving to right
        self.direction = Direction.RIGHT.value
        self.speed = 5
        # Cabeça da cobra
        self.head = Part(200, 200)
        # Partes do corpo da cobra
        self.parts = [self.head, Part(220, 200), Part(240, 200)]
        # Ultima posição da cobra
        self.last = self.head

    def move(self, direction):
        self.direction = direction

    def add(self, part):
        self.parts.append(part)

    def remove(self, part):
        if part in self.parts:
            self.parts.remove(part)

    def update(self):
        self.last = self.head

        if self.direction == Direction.RIGHT.value:
            self.head.x += 20
        if self.direction == Direction.LEFT.value:
            self.head.x -= 20
        if self.direction == Direction.UP.value:
            self.head.y -= 20
        if self.direction == Direction.DOWN.value:
            self.head.y += 20

        for index in range(1, len(self.parts)):
            part = self.parts[index]
            part.x = self.last.x
            part.y = self.last.y
            self.parts[index] = part
            self.last = part
   
    def show(self, screen, pygame):
        for part in self.parts:
            pygame.draw.rect(screen, (0, 255, 0), (part.x, part.y, 20, 20))
