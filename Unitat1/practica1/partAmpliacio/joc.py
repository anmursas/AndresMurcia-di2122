# Import the pygame module
import pygame
import pygame.locals
import random
import os.path
import time
import sqlite3
from sqlite3 import Error

from pygame import RLEACCEL, K_SPACE

# Path
dir = os.path.dirname(__file__)
res = os.path.join(dir, 'resources')

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_p
)

# Initialize pygame
pygame.init()

# Setup for sounds
pygame.mixer.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Setup the clock for a decent framerate
clock = pygame.time.Clock()


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(os.path.join(res, "jet.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join(res, "missile.png")).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2 * nivell, 10 + 3 * nivell)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        global scorev
        global nivell
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            for e in enemies:
                if e.rect.right <= 1:
                    scorev += 10
                    if scorev % 500 == 0:
                        nivell += 1
            self.kill()


# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(os.path.join(res, "cloud.png")).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Definir las balas
# La bala se moverá a 5px/s
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load(os.path.join(res, "laser.png")).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self):
        self.rect.x += 5


# Definimos la variable global Scorev
# Donde se almacenará la puntuación
global scorev
scorev = 0

# Definimos la variable global nivell
# Donde se almacenará el nivel actual
global nivell
nivell = 1

font = pygame.font.Font('freesansbold.ttf', 25)


# La función score recibe dos argumentos
# X e Y será la posición en la que se mostrará la puntuación
def score(x, y):
    score = font.render("Score: " + str(scorev), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Idem score pero con el Nivel
def mostranivell(x, y):
    level = font.render("Nivell: " + str(nivell), True, (255, 255, 255))
    screen.blit(level, (x, y))


# Nos conectamos a la base de datos
# En esta bd se almacena la puntuación máxima
def connexion():
    try:
        sqliteConnection = sqlite3.connect((os.path.join(res, "max_score.db")))
        return sqliteConnection
    except Error:
        print(Error)


# Creamos un objeto con y creamos un cursor a partir de éste
con = connexion()
cursor = con.cursor()


# Ejecutamos la consulta
# Almacenamos la respuesta y será lo que devuelva la función
def leersql():
    cursor.execute("SELECT score FROM punts")
    row = cursor.fetchone()
    return row[0]


# Si la consulta a la base de datos es menor que nuestra puntuación
# Guardamos nuestra puntuación actual dentor de la base de datos
def updatesql():
    if leersql() < scorev:
        cursor.execute("update punts set score = " + str(scorev))
        con.commit()


# Esta pantalla se muestra cuando perdemos
# Nos muestra nuestra puntuación y si hemos superado el récord
def pantalla_final():
    screen.fill((0, 0, 0))
    intro_label = font.render("La partida ha finalitzat", 1, (255, 255, 255))
    score_label = font.render("Tens: " + str(scorev) + " punts", 1, (255, 255, 255))
    lvl_label = font.render("Has arribat al nivell " + str(nivell), 1, (255, 255, 255))
    screen.blit(intro_label, (250, 200))
    screen.blit(score_label, (250, 300))
    screen.blit(lvl_label, (250, 400))
    if leersql() < scorev:
        new_label = font.render("Felicitats, nou rècord amb: " + str(scorev) + " punts", 1, (255, 255, 255))
        screen.blit(new_label, (250, 500))
    pygame.display.update()


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, int(50 + 200 / nivell))

# Create a custom event for adding a new cloud
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Cambiar fondo
CHANGECOLOR = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGECOLOR, 20000)
color_fons = (135, 206, 250)
background = True

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
balas = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play background music
pygame.mixer.music.load(os.path.join(res, "Apoxode_-_Electric_1.mp3"))
pygame.mixer.music.set_volume(0.1)  # volumen del juego
pygame.mixer.music.play(loops=-1)

# Load all sound files
move_up_sound = pygame.mixer.Sound(os.path.join(res, "Rising_putter.mp3"))
move_down_sound = pygame.mixer.Sound(os.path.join(res, "Falling_putter.mp3"))
collision_sound = pygame.mixer.Sound(os.path.join(res, "Collision.mp3"))
move_down_sound.set_volume(0.1)
move_up_sound.set_volume(0.1)

# Variable to keep the main loop running
running = True
tiempo = False
intro = True

# Menu intro
while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((135, 206, 250))
    intro_label = font.render("Press p to play", 1, (255, 255, 255))
    max_score_label = font.render("Record: " + str(leersql()), 1, (255, 255, 255))
    screen.blit(intro_label, (250, 200))
    screen.blit(max_score_label, (250, 300))

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_p]:
        intro = False
    pygame.display.update()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():

        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet()
                new_bullet.rect.x = player.rect.x + 45
                new_bullet.rect.y = player.rect.y + 3

                balas.add(new_bullet)
                all_sprites.add(new_bullet)
            if event.key == K_ESCAPE:
                running = False


        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
            velocitatEnemies = 50 + (200 / nivell)

        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

        elif event.type == CHANGECOLOR:
            if background is True:
                background = False
                color_fons = 0, 0, 0
            elif background is False:
                background = True
                color_fons = 135, 206, 250

    for laser in balas:
        meteor_hit_list = pygame.sprite.spritecollide(laser, enemies, True)
        for meteor in meteor_hit_list:
            all_sprites.remove(laser)
            balas.remove(laser)
            scorev += 10
        if laser.rect.x < -10:
            all_sprites.remove(laser)
            balas.remove(laser)
    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update positions
    enemies.update()
    clouds.update()
    balas.update()

    screen.fill(color_fons)
    # Mostra score i lvl
    score(10, 10)
    mostranivell(10, 50)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # Sounds stop
        move_up_sound.stop()
        move_up_sound.stop()

        # Collision sound play
        collision_sound.play()
        time.sleep(0.5)

        # Guardar score
        connexion()

        pantalla_final()
        updatesql()
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        time.sleep(10)

        # If so,then remove the player and stop the loop
        player.kill()

        running = False

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()

    # Ensure program manintains a rate of 30fps
    clock.tick(75)
