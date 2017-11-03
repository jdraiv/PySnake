
import pygame
import random


class AppleClass:
    def __init__(self, screen, snake_head_pos):
        self.screen = screen
        self.apple_pos = self.random_pos()
        self.snake_head_pos = snake_head_pos

    def random_pos(self):
        pos = []
        for c in range(2):
            pos.append(2 * random.randint(0, 150))
        return pos

    def draw_apple(self):
        pygame.draw.rect(self.screen, (250, 0, 0), [self.apple_pos[0], self.apple_pos[1], 20, 20])

