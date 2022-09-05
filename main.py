# import libraries
import pygame
import random 
import math 
from pygame import mixer 

# initialize pygame
pygame.init()

# window size
screen_width = 800
screen_heigh = 600

# size variable
size = (screen_width, screen_heigh)

# display window
screen = pygame.display.set_mode( size )

#background image
background = pygame.image.load("spacefondo.png")

#background music 
mixer.music.load("musica-bit-para-videojuego-indie-114696.wav")
mixer.music.play(-1)


# title
pygame.display.set_caption("Space Invaders")

# icon
icon = pygame.image.load("icono.png")
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load("nave.png")
player_x = 370
player_y = 480
player_x_change = 0

# enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

#number of enemies
number_enemies = 8

#create mulpiplt enemies
for item in range( number_enemies ):
    enemy_img.append(pygame.image.load("alien.png"))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(30)

# bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480      #the same player y
bullet_x_change = 0
bullet_y_change = 20
bullet_state = "ready"

#score
score = 0

#font variable 
score_font = pygame.font.Font("Stocky-lx5.ttf", 32)

#text position
text_x = 10
text_y = 10

# game over text
go_font = pygame.font.Font( "Stocky-lx5.ttf", 64)
go_x = 200
go_y = 250

#game over function
def game_over(x, y):
    go_text=go_font.render("Game Over", True, (0, 0, 0))
    screen.blit(go_text, (x, y) )
    
#text function
def show_text( x, y ):
    score_text = score_font.render("SCORE:   " + str( score ), True, (0, 0, 0))
    screen.blit(score_text, (x, y))

#player function
def player(x, y,):
    screen.blit(player_img, (x , y)) 

#enemy function
def enemy(x, y, item):
    screen.blit(enemy_img[item], (x , y))

# shoot function
def fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# collision function
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
    
    if distance < 27:
        return True
    else:
        return False



# game loop
running = True
while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

# comprobando si las teclas estan siendo presionadas 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_x_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("8-bit-explosion-95847.wav")
                    bullet_sound.play()

                    bullet_x = player_x  
                fire(player_x, bullet_y)

                            
    # color RGB
    rgb = (16,44,84)       
    screen.fill(rgb)

#llamar fondo
    screen.blit(background, (0, 0))

#llamar imagen jugador  
    player_x += player_x_change
    player(player_x, player_y)

#call player function
    player_x += player_x_change
    player(player_x, player_y)

 

#player boundarries
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    #enemy movement
    for item in range( number_enemies ):

        #game over zone
        if enemy_y[ item ] > 460:
            for j in range( number_enemies ):
                enemy_y[ j ] = 2000

            #call game_over function
            game_over(go_x, go_y)

            break
        enemy_x[item] += enemy_x_change [item]

        if enemy_x[item] <= 0:
            enemy_x_change[item] = 4
            enemy_y[item] += enemy_y_change[item]

        elif enemy_x[item] >= 736:
            enemy_x_change[item] = -4
            enemy_y[item] += enemy_y_change[item]

        # call collision funtion
        collision = is_collision(enemy_x[item], enemy_y[item], bullet_x, bullet_y)

        if collision:
            explosion_sound = mixer.Sound("8-bit-explosion-95847.wav")
            bullet_y = 480
            bullet_state = "ready"
            score += 5
            #print(score) 
            enemy_x[item] = random.randint(0, 735)
            enemy_y[item] = random.randint(50, 150)
        #call enemy funct
        enemy(enemy_x[item] , enemy_y[item], item)
    

    #bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire(player_x, bullet_y)
        bullet_y -= bullet_y_change

    


    #call the text function
    show_text(text_x, text_y)
    # update window
    pygame.display.update()
