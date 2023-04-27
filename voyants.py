import pygame
import os

pygame.init()
pygame.display.init()
script_dir = os.path.dirname(__file__)

class ButtonLight(pygame.sprite.Sprite):
    def __init__(self, pos, image1, image2, scale=0.03):
        super().__init__()
        self.image1 = pygame.image.load(os.path.join(script_dir, "assets", image1)).convert_alpha()
        self.image2 = pygame.image.load(os.path.join(script_dir, "assets", image2)).convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (int(self.image1.get_width() * scale), int(self.image1.get_height() * scale)))
        self.image2 = pygame.transform.scale(self.image2, (int(self.image2.get_width() * scale), int(self.image2.get_height() * scale)))
        self.image = self.image1
        self.rect = self.image.get_rect(topleft=pos)
        self.status = 0

    def toggle(self):
        self.status = 1 - self.status
        if self.status == 0:
            self.image = self.image1
        else:
            self.image = self.image2

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.toggle()

    @property
    def state(self):
        return self.status

