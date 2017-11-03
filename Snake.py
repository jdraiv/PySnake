import pygame


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.direction = "left"
        self.head = [400, 400]
        self.head_old = []
        self.snake_body = [[420, 400], [440, 400]]

    def controller(self, key_char):
        if key_char == 97:
            self.direction = "left"
        elif key_char == 100:
            self.direction = "right"
        elif key_char == 119:
            self.direction = "up"
        elif key_char == 115:
            self.direction = "down"

    def head_movement(self):
        # Set old position of the head
        self.head_old = self.head[:]

        if self.direction == "left":
            self.head[0] -= 20
        elif self.direction == "right":
            self.head[0] += 20
        elif self.direction == "up":
            self.head[1] -= 20
        elif self.direction == "down":
            self.head[1] += 20

    def tail_movement(self, h, body):
        # Update body
        last_segment = h
        for c, l in enumerate(self.snake_body):
            body[c] = [last_segment[0], last_segment[1]]
            last_segment = l
        return body

    def draw_snake(self):
        pygame.draw.rect(self.screen, (250, 250, 250), [self.head[0], self.head[1], 20, 20])
        # Update snake body
        self.snake_body = self.tail_movement(self.head_old, self.snake_body)

        for l in self.snake_body:
            pygame.draw.rect(self.screen, (250, 250, 250), [l[0], l[1], 20, 20])


