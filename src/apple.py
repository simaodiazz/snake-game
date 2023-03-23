from random import randint

class Apple:

    def __init__(self):
        xRand = randint(0, 1920)
        yRand = randint(0, 1080)
        
        while (xRand % 20 and yRand % 20):
            xRand = randint(0, 1920)
            yRand = randint(0, 1080)

        self.x = xRand
        self.y = yRand

    def spawn(self):
        self.x = randint(0, 1920)
        self.y = randint(0, 1080)

    def show(self, screen, pygame):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 20, 20))
