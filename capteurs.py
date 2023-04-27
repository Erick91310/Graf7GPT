import pygame
import os


class Capteurs_y(pygame.sprite.Sprite):
    def __init__(self, pos, img1, img2, min_y, max_y, scale=0.03):
        super().__init__()
        self.image1 = pygame.image.load(os.path.join("assets", img1)).convert_alpha()
        self.image2 = pygame.image.load(os.path.join("assets", img2)).convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (int(self.image1.get_width() * scale), int(self.image1.get_height() * scale)))
        self.image2 = pygame.transform.scale(self.image2, (int(self.image2.get_width() * scale), int(self.image2.get_height() * scale)))
        self.image = self.image1
        self.rect = self.image.get_rect(topleft=pos)
        self.min_y = min_y
        self.max_y = max_y
        self.status = False

    def update(self, y_position):
        if self.min_y <= y_position <= self.max_y:
            self.image = self.image2
            self.status = True
        else:
            self.image = self.image1
            self.status = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    @property
    def state(self):
        return self.status


class Capteurs_x(pygame.sprite.Sprite):
    def __init__(self, pos, img1, img2, min_x, max_x, scale=0.03):
        super().__init__()
        self.image1 = pygame.image.load(os.path.join("assets", img1)).convert_alpha()
        self.image2 = pygame.image.load(os.path.join("assets", img2)).convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (int(self.image1.get_width() * scale), int(self.image1.get_height() * scale)))
        self.image2 = pygame.transform.scale(self.image2, (int(self.image2.get_width() * scale), int(self.image2.get_height() * scale)))
        self.image = self.image1
        self.rect = self.image.get_rect(topleft=pos)
        self.min_x = min_x
        self.max_x = max_x
        self.status = False

    def update(self, x_position):
        if self.min_x <= x_position <= self.max_x:
            self.image = self.image2
            self.status = True
        else:
            self.image = self.image1
            self.status = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    @property
    def state(self):
        return self.status
