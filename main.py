import pygame
from utilities import scall
from portes import Porte1
from portes import Porte2
from portes import Porte3
from cabine import Cabine
from led_counter import LedCounter
from pupitres import Pupitres
from voyants import ButtonLight
from capteurs import Capteurs_y
from capteurs import Capteurs_x

clock = pygame.time.Clock()
pygame.init()

# Chargement du fichier audio
#monte_plat = pygame.mixer.Sound('assets/applause.wav')
# Lecture du fichier audio
#monte_plat.play()
# Pause de l'application pendant la lecture du fichier audio
#pygame.time.wait(int(monte_plat.get_length() * 10))

# générer la fenêtre du jeu
pygame.display.set_caption("Monte plats simulation")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arrière-plan de l'appli
background1 = pygame.image.load("assets/Fond2.png")
background2 = pygame.image.load("assets/FondChambranles2.png")

# charger notre jeu
game = pygame.sprite.Group()
cabine = Cabine((431, 70))
led_counter = LedCounter((600, 62), font_path="assets/digits/KARNIVOL.ttf", font_size=15)

game.add(cabine)
porte1 = Porte1()
game.add(porte1)
porte3 = Porte3()
game.add(porte3)
porte2 = Porte2()
game.add(porte2)
pupitre1 = Pupitres("assets/pupitre1.png")
game.add(pupitre1)
pupitre2 = Pupitres("assets/pupitre2.png")
game.add(pupitre2)
#capteur1 = Capteurs()
#game.add(capteur1)
#capteur2 = Capteurs()
#game.add(capteur2)


# charger l'image des pupitres
pupitre1 = pygame.image.load("assets/pupitre1.png")
pupitre1 = scall(pupitre1, 0.8)  # Redimensionne l'image à 80% de sa taille d'origine
pupitres_rect1 = pupitre1.get_rect()
pupitres_rect1.x = 600
pupitres_rect1.y = 56
pupitre2 = pygame.image.load("assets/pupitre2.png")
pupitre2 = scall(pupitre2, 0.845)  # Redimensionne l'image à 85,4% de sa taille d'origine
pupitres_rect2 = pupitre2.get_rect()
pupitres_rect2.x = 600
pupitres_rect2.y = 411

# Initialisation des boutons lumineux
button1 = ButtonLight((300, 20), "BPorange.png", "BPvert.png")
button2 = ButtonLight((340, 20), "BPorange.png", "BPvert.png")
button3 = ButtonLight((380, 20), "BPorange.png", "BPvert.png")
button4 = ButtonLight((420, 20), "BPorange.png", "BPvert.png")

# create capteur group
capteur_group = pygame.sprite.Group()

#Charger l'image des capteurs de la cabine
capteur1 = Capteurs_y((80, 20), "BPorange.png", "BPvert.png", 65,70) #((pos_x, pos_y), "image1", "image2", detect_min-y, detct_max_y)
capteur2 = Capteurs_y((120, 20), "BPorange.png", "BPvert.png", 430, 440) #((pos_x, pos_y), "image1", "image2", detect_min-y, detct_max_y)
capteur4 = Capteurs_y((160, 20), "BPorange.png", "BPvert.png", 420, 421) #((pos_x, pos_y), "image1", "image2", detect_min-y, detct_max_y)

#Charger l'image des capteurs de portes
capteur3 = Capteurs_x((200, 20), "BPorange.png", "BPvert.png", 430,431) #((pos_x, pos_y), "image1", "image2", detect_min-y, detct_max_y)


# add capteurs to group
capteur_group.add(capteur1, capteur2, capteur3, capteur4)

running = True

# Boucle tant que cette condition est vraie
while running:
    # appliquer l'arrière-plan1 de notre appli
    screen.blit(background1, (0, 0))

    # mise à jour de game pour déplacer les "mobiles"
    game.update()

    # appliquer les image "mobiles"?
    game.draw(screen)

    # appliquer l'arrière-plan2 de notre appli
    screen.blit(background2, (0, 0))

    # dessiner l'image des pupitres
    screen.blit(pupitre1, pupitres_rect1)
    screen.blit(pupitre2, pupitres_rect2)

    # Dessiner les boutons lumineux
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)

    # Mise à jour et affichage du compteur
    led_counter.update_value(cabine.rect.y)
    led_counter.draw(screen)

    # Affichage de la position y de la cabine
    print("Cabine position y :", cabine.rect.y)

    # Mise à jour de la cabine et des capteurs
    #cabine.update()
    capteur1.update(cabine.rect.y)
    capteur2.update(cabine.rect.y)
    capteur3.update(porte1.rect.x)
    capteur4.update(porte2.rect.y)


    # Dessiner les capteurs
    #capteur1.draw(screen)
    #capteur2.draw(screen)


    # draw capteurs
    capteur_group.draw(screen)

    # mettre à jour notre écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # vérifier que l'événement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                porte1.move_right()
            elif event.key == pygame.K_LEFT:
                porte1.move_left()
            elif event.key == pygame.K_UP:
                porte2.move_down()
                porte3.move_up()
            elif event.key == pygame.K_DOWN:
                porte2.move_up()
                porte3.move_down()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # récupérer la position de la souris
            mouse_pos = pygame.mouse.get_pos()

            # vérifier si la position de la souris se trouve sur la porte1
            if porte1.rect.collidepoint(mouse_pos):
                # ouvrir ou fermer la porte1 en fonction de son état actuel
                if event.button == 1:
                    if porte1.status == 0:
                        porte1.move_right()
                    elif porte1.status == 3:
                        porte1.move_left()

            # vérifier si la position de la souris se trouve sur la porte2
            if porte2.rect.collidepoint(mouse_pos):
                # ouvrir ou fermer la porte1 en fonction de son état actuel
                if event.button == 1:
                    if porte2.status == 0:
                        porte2.move_up()
                        porte3.move_down()
                    elif porte2.status == 3:
                        porte2.move_down()
                        porte3.move_up()

            # vérifier si la position de la souris se trouve sur la cabine
            if cabine.rect.collidepoint(mouse_pos):
                # faire descendre ou monter la cabine en fonction de son état actuel
                if event.button == 1:
                    if cabine.status == 0:
                        cabine.move_up()
                        #monte_plat.play() neutralisé en lignes 11 à 16 car ne fonctionne pas
                        print("montée")
                    elif cabine.status == 3:
                        cabine.move_down()
                        #monte_plat.play() neutralisé en lignes 11 à 16 car ne fonctionne pas
                        print("descendre")


    # Gérer les événements des boutons lumineux
    button1.handle_event(event)
    button2.handle_event(event)
    button3.handle_event(event)
    button4.handle_event(event)

    # Récupérer l'état de chaque bouton
    state1 = button1.state
    state2 = button2.state
    state3 = button3.state
    state4 = button4.state

    # Recuperer les états des boutons
    if state1 == 1:
        print("Le bouton 1 est actif !")
    else:
        print("Le bouton 1 est inactif.")

    if state2 == 1:
        print("Le bouton 2 est actif !")
    else:
        print("Le bouton 2 est inactif.")

    if state3 == 1:
        print("Le bouton 3 est actif !")
    else:
        print("Le bouton 3 est inactif.")

    if state4 == 1:
        print("Le bouton 4 est actif !")
    else:
        print("Le bouton 4 est inactif.")


    # gerer les états de capteurs
    cabine.rect.y




    clock.tick(60)