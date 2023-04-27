import pygame

# créer une classe pour représenter la porte 1
class Porte1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("assets/porte1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 431
        self.rect.y = 70
        self.status = 3  # 0 = fermée, 1 = en train de s'ouvrir, 2 = en train de se fermer, 3 = ouverte

    def move_right(self):
        if self.status == 0:
            self.status = 1
        elif self.status == 2:
            self.status = 1

    def move_left(self):
        if self.status == 1:
            self.status = 2
        elif self.status == 0:
            self.status = 2
        elif self.status == 3:
            self.status = 2

    def update(self):
        if self.status == 1:
            if self.rect.x < 431:
                self.rect.x += self.velocity
            else:
                self.status = 3
        elif self.status == 2:
            if self.rect.x > 335:
                self.rect.x -= self.velocity
            else:
                self.status = 0
        elif self.status == 3:
            # Porte ouverte, rien à faire ici
            pass

# créer une classe pour représenter la porte 2
class Porte2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("assets/porte2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 431
        self.rect.y = 310
        self.status = 0  # 0 = fermée, 1 = en train de s'ouvrir, 2 = en train de se fermer, 3 = ouverte

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
            if self.rect.y < 420:
                self.rect.y += self.velocity
            else:
                self.status = 3
        elif self.status == 2:
            if self.rect.y > 310:
                self.rect.y -= self.velocity
            else:
                self.status = 0
        elif self.status == 3:
            # Porte ouverte, rien à faire ici
            pass

# créer une classe pour représenter la porte 2
class Porte3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("assets/porte3.png")
        self.rect = self.image.get_rect()
        self.rect.x = 431
        self.rect.y = 645
        self.status = 0  # 0 = fermée, 1 = en train de s'ouvrir, 2 = en train de se fermer

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

    def update(self):
        if self.status == 1:
            if self.rect.y < 645:
                self.rect.y += self.velocity
            else:
                self.status = 0
        elif self.status == 2:
            if self.rect.y > 545:
                self.rect.y -= self.velocity
            else:
                self.status = 0