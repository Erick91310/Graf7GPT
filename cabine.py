import pygame

# créer une classe pour représenter la cabine
class Cabine(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("assets/cabine.png")
        self.rect = self.image.get_rect()
        self.rect.x = 431
        self.rect.y = 70
        self.status = 3  # 0 = haut, 1 = en train de descendre, 2 = en train de monter, 3 = en bas
        self.y = pos[0] # Ajout de l'attribut self.y pour stocker la position y de la cabine
        self.pos = pos
    def update(self):
        self.rect.move_ip(self.vel, 0)
        self.y = self.rect.y  # Mise à jour de self.y avec la nouvelle position y de la cabine

    def move_up(self):
        if self.status == 0:
            self.status = 1
        elif self.status == 2:
            self.status = 1

    def move_down(self):
        if self.status == 1:
            self.status = 2
        elif self.status == 0:
            self.status = 2
        elif self.status == 3:
            self.status = 2

    def update(self):
        if self.status == 1:
            if self.rect.y < 500:
                self.rect.y += self.velocity
            else:
                self.status = 3
        elif self.status == 2:
            if self.rect.y > 10:
                self.rect.y -= self.velocity
            else:
                self.status = 0
        elif self.status == 3:
            # Porte ouverte, rien à faire ici
            pass

    def display_position(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Position Y de la cabine : {self.rect.y}", True, (255, 255, 255))
        screen.blit(text, (20, 20))