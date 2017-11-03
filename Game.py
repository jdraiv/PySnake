
import pygame
import sys

# Classes
import Snake
import Apple
import UI

class Game:
    def __init__(self, bg):
        self.bg = bg
        self.screen = pygame.display.set_mode([500, 500])
        self.snake_class = Snake.Snake(self.screen)
        self.apple_class = Apple.AppleClass(self.screen, self.snake_class.head)
        self.start = False

    def game(self):
        clock = pygame.time.Clock()
        clock.tick(25)

        # Draw apple
        self.apple_class.draw_apple()

        # Update snake head position
        self.snake_class.head_movement()
        self.snake_class.draw_snake()

        # Collision detection
        # If snake collision
        if self.snake_class.snake_collision():
            sys.exit()

        # If the apple is eaten
        if self.apple_class.apple_collision():
            # Append a segment to the snake_body list
            self.snake_class.snake_body.append([])


    def game_controller(self, key_char):
        if key_char == 111:
            self.start = True
        elif key_char == 112:
            self.start = False

    def game_loop(self):
        pygame.font.init()
        play = True

        while play:
            self.screen.fill([0, 0, 0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exit")
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.game_controller(event.key)
                    self.snake_class.controller(event.key)
            # Execute game
            if self.start:
                self.game()
            # Show pause screen
            else:
                UI.UIClass(self.screen).start_text()

            # Update screen
            pygame.display.update()


game = Game(1)
game.game_loop()