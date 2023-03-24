import pygame

from snake import Snake
from apple import Apple
from direction import Direction
from part import Part


class Game:

    def __init__(self):
        # Declaring variables
        self.height = 1000
        self.width = 1000

        # Setup basic informations
        pygame.init()

        self.screen = pygame.display.set_mode((self.height, self.width))

        # This method it's to limit framerate to 60
        self.clock = pygame.time.Clock()

        self.snake = Snake(self.height, self.width)
        self.apple = Apple()

    # This method is to start runnable
    def run(self):

        # This is loop, when finish, come back to start
        while True:

            self.screen.fill((0, 0, 0))

            self.clock.tick(10)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.move(Direction.UP.value)

                    if event.key == pygame.K_DOWN:
                        self.snake.move(Direction.DOWN.value)

                    if event.key == pygame.K_RIGHT:
                        self.snake.move(Direction.RIGHT.value)

                    if event.key == pygame.K_LEFT:
                        self.snake.move(Direction.LEFT.value)

            self.snake.update()
            self.snake.show(self.screen, pygame)

            if self.snake.is_collision():
                quit()

            if self.apple.x == self.snake.head.x and self.apple.y == self.snake.head.y:
                self.snake.add(Part(self.snake.last.x, self.snake.last.y))
                self.apple.spawn()

            self.apple.show(self.screen, pygame)

            pygame.display.update()
