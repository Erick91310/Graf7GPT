import pygame

def scall(surface, scale):
    """
    Redimensionne la surface Pygame donnée à l'échelle spécifiée.
    :param surface: Surface Pygame à redimensionner
    :param scale: Échelle de la nouvelle surface Pygame (float ou tuple)
    :return: Surface Pygame redimensionnée
    """
    if isinstance(scale, tuple):
        # Si l'échelle est une tuple, appliquer l'échelle sur chaque dimension de la surface
        return pygame.transform.scale(surface, (int(surface.get_width() * scale[0]), int(surface.get_height() * scale[1])))
    else:
        # Sinon, appliquer l'échelle uniformément sur la surface
        return pygame.transform.scale(surface, (int(surface.get_width() * scale), int(surface.get_height() * scale)))
