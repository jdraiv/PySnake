import pygame
import Vars

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.direction = "left"
        self.head = [400, 400]
        self.head_old = []
        self.snake_body = [[420, 400], [440, 400]]

    def controller(self, key_char):
        if key_char == 97 and self.direction != "right":
            self.direction = "left"
        elif key_char == 100 and self.direction != "left":
            self.direction = "right"
        elif key_char == 119 and self.direction != "down":
            self.direction = "up"
        elif key_char == 115 and self.direction != "up":
            self.direction = "down"

    def head_movement(self):
        # Set old position of the head
        self.head_old = self.head[:]

        def update_direction(list_to_update, direction):
            def border_col(l, index):
                # Spawns snake at the opposite direction
                if l[index] <= -20:
                    l[index] = 480
                elif l[index] >= 500:
                    l[index] = 0

            positive_l = ["right", "down"]
            negative_l = ["left", "up"]

            if direction in positive_l:
                l_index = positive_l.index(direction)
                list_to_update[l_index] += Vars.snake_size

                border_col(list_to_update, l_index)
            elif direction in negative_l:
                l_index = negative_l.index(direction)
                list_to_update[l_index] -= Vars.snake_size

                border_col(list_to_update, l_index)

        update_direction(self.head, self.direction)

    def tail_movement(self, h, body):
        # Update body
        last_segment = h
        for c, l in enumerate(self.snake_body):
            body[c] = [last_segment[0], last_segment[1]]
            last_segment = l
        return body

    def snake_collision(self):
        for l in self.snake_body:
            if self.head[0] == l[0] and self.head[1] == l[1]:
                return True

    def draw_snake(self):
        pygame.draw.rect(self.screen, Vars.white_color, [self.head[0], self.head[1], 20, 20])
        # Update snake body
        self.snake_body = self.tail_movement(self.head_old, self.snake_body)

        for l in self.snake_body:
            pygame.draw.rect(self.screen, Vars.white_color, [l[0], l[1], 20, 20])


