import pygame

from snake import Snake
from apple import Apple
from direction import Direction


class Game:

    def __init__(self):
        # Declaring variables
        self.height = 0
        self.width = 0
        self.fullscreen = True

        self.limit = 10

        # Setup basic informations
        pygame.init()

        self.screen = pygame.display.set_mode((self.height, self.width), self.fullscreen)

        # This method it's to limit framerate to 60
        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.apple = Apple()

    # This method is to start runnable
    def run(self):

        # This is loop, when finish, come back to start        
        while True:

            self.clock.tick(30)

            if len(self.snake.parts) == self.limit:
                print("Ganhou o jogo.")

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.type == pygame.K_UP:
                        self.snake.move(Direction.UP.value)
                    
                    if event.type == pygame.K_DOWN:
                        self.snake.move(Direction.DOWN.value)

                    if event.type == pygame.K_RIGHT:
                        self.snake.move(Direction.RIGHT.value)

                    if event.type == pygame.K_LEFT:
                        self.snake.move(Direction.LEFT.value)
                        
            self.snake.update()
            self.snake.show(self.screen, pygame)

            self.apple.show(self.screen, pygame)

            pygame.display.update()
