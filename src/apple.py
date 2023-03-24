from random import randint


class Apple:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.spawn()

    def spawn(self):
        self.x = randint(0, (self.width / 20) - 1) * 20
        self.y = randint(0, (self.height / 20) - 1) * 20

    def show(self, screen, pygame):
        pygame.draw.rect(screen, (128, 0, 0), (self.x, self.y, 20, 20))
