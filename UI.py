
import pygame


class UIClass:
    def __init__(self, screen):
        self.screen = screen

    def draw_text(self, t, x_pos, y_pos):
        font = pygame.font.SysFont("monospace", 13)
        text = font.render(t, 1, (0, 250, 0))
        self.screen.blit(text, (x_pos, y_pos))
