from random import randint


class Apple:

    def __init__(self):
        self.spawn()

    def spawn(self):
        self.x = randint(0, 49) * 20
        self.y = randint(0, 49) * 20

    def show(self, screen, pygame):
        pygame.draw.rect(screen, (128, 0, 0), (self.x, self.y, 20, 20))
