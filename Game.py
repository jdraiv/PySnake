
import pygame
import sys

# Classes
import Snake
import Apple


class Game:
    def __init__(self, bg):
        self.bg = bg
        self.screen = pygame.display.set_mode([500, 500])
        self.snake_class = Snake.Snake(self.screen)
        self.apple_class = Apple.AppleClass(self.screen, self.snake_class.head)

    def game_loop(self):
        play = True

        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exit")
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.snake_class.controller(event.key)

            # Frames per second
            clock = pygame.time.Clock()
            clock.tick(25)

            self.screen.fill([0, 0, 0])
            # Update snake head position
            self.snake_class.head_movement()
            self.apple_class.draw_apple()
            self.snake_class.draw_snake()

            # TODO
            # Collision detection
            print(self.apple_class.snake_head_pos())

            pygame.display.update()


game = Game(1)
game.game_loop()