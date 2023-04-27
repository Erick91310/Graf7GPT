import pygame

# créer une classe pour représenter les boutons
class Pupitres(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()


