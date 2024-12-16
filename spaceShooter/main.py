import pygame
import random
import math
import asyncio
from pygame import mixer


#initializes the game 
pygame.init()

#holds screen size 
screen_height = 600
screen_width = 800

#controls the fps/snake speed 
clock = pygame.time.Clock()

#sets up screen using pygame module 
screen = pygame.display.set_mode((screen_width, screen_height))

#creates title 
pygame.display.set_caption("Space Invaders Knockoff")


score = 0 
score_x = 5
score_y = 5

#default font 
font = pygame.font.Font('freesansbold.ttf', 20)

#font used when game ends 
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

#creates formt for score text 
def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_text, (x , y ))

#creates format for game over text 
def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255,255,255))

    screen.blit(game_over_text, (190, 250))

#player image 
player_image = pygame.image.load('spaceShooter/images/spaceship.png')

#sets location for spaceship
player_x = 370
player_y = 523
player_xModified = 0

#alien image 
invaderImage = []

#holds coordinates of aliens 
invader_x = []
invader_y = []
invader_xModified = []
invader_yModified = []
number_of_invaders = 8

#loops through the number of aliens and randomly assigns them x and y coordinates 
for num in range(number_of_invaders):
    invaderImage.append(pygame.image.load('spaceShooter/images/alien.png'))
    invaderImage.append(pygame.image.load('spaceShooter/images/ufo.png'))
    invader_x.append(random.randint(64, 737))
    invader_y.append(random.randint(30, 180))
    invader_xModified.append(1.2)
    invader_yModified.append(50)

bulletImage = pygame.image.load('spaceShooter/images/bullet.png')

#bullet coordinates  
bullet_x = 0
bullet_y = 500
bullet_xModified = 0
bullet_yModified = 3
bullet_state = 'rest'

#checks if the 
def hitAlien(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) + 
                        (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False 
    
#renders spaceship image at different x and y locations 
def player(x, y):
    screen.blit(player_image, (x - 16, y + 10))

#changes aliens location based on the random number generated 
def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

def bullet(x, y):
    global bullet_state
    screen.blit(bulletImage, (x,y))
    bullet_state = "fire"


running = True

async def main():

    global running, player_x, player_xModified, bullet_y, bullet_state, bullet_x, score

    while running:

        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            
            #movements based on the keys pressed 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player_xModified = -1.7

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player_xModified = 1.7
                
                if event.key == pygame.K_SPACE:

                    if bullet_state == "rest":
                        bullet_x = player_x
                        bullet(bullet_x, bullet_y)

            if event.type == pygame.KEYUP or event.type == pygame.K_w:
                player_xModified = 0

        player_x += player_xModified

        for i in range(number_of_invaders):
            invader_x[i] += invader_xModified[i]

        if bullet_y <= 0:
            bullet_y = 600
            bullet_state = "rest"
        
        if bullet_state == "fire":
            bullet(bullet_x, bullet_y)
            bullet_y -= bullet_yModified

        for i in range(number_of_invaders):

            if invader_y[i] >= 450:
                if abs(player_x - invader_x[i]) < 80:
                    for j in range(number_of_invaders):
                        invader_y[j] = 2000
                    game_over()
                    break
            
            if invader_x[i] >= 735 or invader_x[i] <= 0:
                invader_xModified[i] *= -1 
                invader_y[i] += invader_yModified[i]

            collision = hitAlien(bullet_x, invader_x[i], bullet_y, invader_y[i])

            if collision: 
                score += 1
                bullet_y = 600
                bullet_state = 'rest'
                invader_x[i] = random.randint(64, 736)
                invader_y[i] = random.randint(30, 200)
                invader_xModified[i] *= -1
            
            invader(invader_x[i], invader_y[i], i)

        if player_x <= 16:
            player_x = 16
        elif player_x >= 750:
            player_x = 750

        player(player_x, player_y)
        show_score(score_x, score_y)
        clock.tick(150)
        pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())
    

