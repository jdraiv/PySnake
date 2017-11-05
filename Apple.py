
import pygame
import random


class AppleClass:
    def __init__(self, screen, s_head_pos):
        self.screen = screen
        self.apple_pos = self.random_pos()
        self.s_head_pos = s_head_pos

    def apple_collision(self):
        if self.s_head_pos[0] == self.apple_pos[0] and self.s_head_pos[1] == self.apple_pos[1]:
            self.apple_pos = self.random_pos()
            self.draw_apple()
            return True
        else:
            return False

    def random_pos(self):
        pos = []
        for c in range(2):
            pos.append(20 * random.randint(0, 20))
        return pos

    def draw_apple(self):
        pygame.draw.rect(self.screen, (250, 0, 0), [self.apple_pos[0], self.apple_pos[1], 20, 20])

