import pygame
from portes import Porte1

# creer un seconde classe qui va representer notre jeu
class Game:

    def __init__(self):
        # generer notre porte1
        self.porte1 = Porte1()
        self.pressed = {}