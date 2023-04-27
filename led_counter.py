import pygame

class LedCounter:
    def __init__(self, pos, font_path, font_size):
        self.pos = pos
        self.font = pygame.font.Font(font_path, font_size)
        self.digit_size = (12, 60)
        self.spacing = 3
        self.value = 0
        self.digit_images = [self.font.render(str(i), True, (000, 000, 000)) for i in range(10)]

    def update_value(self, new_value):
        self.value = new_value

    def draw(self, screen):
        x, y = self.pos

        digits = [int(d) for d in str(self.value)]
        num_digits = len(digits)
        total_width = num_digits * self.digit_size[0] + (num_digits - 1) * self.spacing

        for i, digit in enumerate(reversed(digits)):
            digit_image = self.digit_images[digit]
            screen.blit(digit_image, (x + (self.digit_size[0] + self.spacing) * (num_digits - 1), y))
            num_digits -= 1

