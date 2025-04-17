import pygame
import time
import random
import requests
import os

# Obtenir le chemin du répertoire du script
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

def load_image(filename):
    return pygame.image.load(os.path.join(BASE_DIR, filename))

# Exemple d'utilisation
icon = load_image("icon.png")
player_image = load_image("boat.png")


# Initialisation de Pygame
pygame.init()

# Constantes
tile_size = 40  # Taille des cases
cols, rows = 10, 10  # Nombre de colonnes et lignes
width, height = 700, 700  # Taille de la fenêtre (400x400 pixels)

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("C:\Users\lchab\OneDrive\Bureau\jeux labyrinthe v2\icon.ico")  # Remplace "icon.png" par le chemin de ton image d'icône
pygame.display.set_icon(icon)

pygame.display.set_caption("Boat VS Ships")


# Chargement de la police pour le texte
font = pygame.font.SysFont('Arial Black', 24)

# Labyrinthe pour 5 niveaux
mazes = [
        # Niveau 1
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    # Niveau 2
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    # Niveaux 3
     [       
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],

    #Niveaux 4
       [  
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    
    #Niveaux 5
     [       
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],	

   
]

# Position initiale du joueur
player_x, player_y = 1, 3
# Position de la sortie
exit_x, exit_y = 8, 8
level = 0

# Ajout des ennemis
enemies = [(5, 5), (7, 7)]
initial_enemy_positions = enemies.copy()

# Charger les images
player_image = pygame.image.load("boat.png")
player_image = pygame.transform.scale(player_image, (tile_size, tile_size))
enemy_image = pygame.image.load("pirate.png")
enemy_image = pygame.transform.scale(enemy_image, (tile_size, tile_size))
treasure_image = pygame.image.load("tresor.png")
treasure_image = pygame.transform.scale(treasure_image, (tile_size, tile_size))
wall_image = pygame.image.load("wall.png")
wall_image = pygame.transform.scale(wall_image, (tile_size, tile_size))
road_image = pygame.image.load("road.jpg")
road_image = pygame.transform.scale(road_image, (tile_size, tile_size))

# Fonction pour dessiner le labyrinthe
def draw_maze():
    for row in range(rows):
        for col in range(cols):
            if mazes[level][row][col] == 1:
                screen.blit(wall_image, (col * tile_size, row * tile_size))
            elif mazes[level][row][col] == 0:
                screen.blit(road_image, (col * tile_size, row * tile_size))

# Fonction pour dessiner le joueur
def draw_player():
    screen.blit(player_image, (player_x * tile_size, player_y * tile_size))

# Fonction pour dessiner la sortie
def draw_exit():
    screen.blit(treasure_image, (exit_x * tile_size, exit_y * tile_size))

# Fonction pour dessiner les ennemis
def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy_image, (enemy[0] * tile_size, enemy[1] * tile_size))

# Fonction pour déplacer les ennemis
def move_enemies():
    global enemies
    new_positions = []
    for enemy in enemies:
        x, y = enemy
        direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        new_x, new_y = x + direction[0], y + direction[1]
        if mazes[level][new_y][new_x] == 0:
            new_positions.append((new_x, new_y))
        else:
            new_positions.append((x, y))
    enemies = new_positions

# Affichage du texte à l'écran
def draw_text(text, y_position):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (10, y_position))  # Positionner le texte en haut à gauche

# Chronomètre
time_limit = 30  # secondes
time_start = time.time()
running = True

while running:
    screen.fill(BLACK)  # Remplir l'écran de noir
    draw_maze()  # Dessiner le labyrinthe
    draw_player()  # Dessiner le joueur
    draw_exit()  # Dessiner la sortie
    draw_enemies()  # Dessiner les ennemis
    move_enemies()  # Déplacer les ennemis
    
    # Calculer le temps écoulé
    elapsed_time = time.time() - time_start
    time_remaining = time_limit - int(elapsed_time)
    
    # Affichage du texte
    draw_text(f"Niveau: {level + 1}", 10)  # Afficher le niveau
    draw_text(f"Temps restant: {time_remaining}s", 40)  # Afficher le temps restant
    
    if elapsed_time > time_limit:
        draw_text("Temps écoulé! Game Over", 70)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
    
    # Détection des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            new_x, new_y = player_x, player_y
            if event.key == pygame.K_LEFT:
                new_x -= 1
            elif event.key == pygame.K_RIGHT:
                new_x += 1
            elif event.key == pygame.K_UP:
                new_y -= 1
            elif event.key == pygame.K_DOWN:
                new_y += 1
            
            if mazes[level][new_y][new_x] == 0:
                player_x, player_y = new_x, new_y
    
    # Vérification de la victoire
    if player_x == exit_x and player_y == exit_y:
        level += 1
        if level >= len(mazes):
            draw_text("Bravo! Tu as terminé tous les niveaux!", 100)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False
        else:
            player_x, player_y = 1, 1
            enemies = initial_enemy_positions.copy()  # Réinitialiser les ennemis
            time_start = time.time()
            draw_text(f"Niveau {level + 1}", 100)
            pygame.display.flip()
            pygame.time.delay(1000)
    
    # Vérification si le joueur touche un ennemi
    if (player_x, player_y) in enemies:
        draw_text("Game Over! Un ennemi t'a attrapé", 100)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
    
    pygame.display.flip()  # Mettre à jour l'écran
    pygame.time.delay(100)

    
    #-------MENUS-------

    # Menu Start  

    

        

pygame.quit()
