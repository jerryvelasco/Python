import pygame
import random
import time
import asyncio
from pygame.locals import *

#starts the game 
pygame.init()


screen_width = 750
pixel_width = 30

screen = pygame.display.set_mode([screen_width] * 2)

#controls the fps/snake speed 
clock = pygame.time.Clock()

#controls the starting positions/random 
def generate_starting_position():
    position_range = (pixel_width // 2, screen_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]


# def reset():
#     target.center = generate_starting_position()
#     snake_pixel.center = generate_starting_position()
#     return snake_pixel.copy()

#define font
font = pygame.font.SysFont(None, 40)
target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_position()

async def main ():

    #controls what happens if the snake goes out of bounds 
    def is_out_of_bounds():
        return snake_pixel.bottom > screen_width or snake_pixel.top < 0 \
            or snake_pixel.left < 0 or snake_pixel.right > screen_width


    #controls what happens after the snake goes out of bounds 
    def game_over():
    
        #custom font
        my_font = pygame.font.SysFont('times new roman', 50)
        
        #game over text formatting 
        game_over_text = my_font.render(
            'Your Score is : ' + str(score), True, (255,255,255))
        
        # creates rectangular object for text 
        game_over_rect = game_over_text.get_rect()
        
        #sets position of the text
        game_over_rect.midtop = (screen_width/2, screen_width/4)
        
        #blit draws the text on screen, flip updates the ui 
        screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()
        
        # after 2 seconds we will quit the program
        time.sleep(1)

        # deactivating pygame library
        pygame.quit()
        
        # quit the program
        quit()


    running = True
    score = 0
    info_line = 10

    #controls the starting location of snake 
    snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
    snake_pixel.center = generate_starting_position()

    snake = [snake_pixel.copy()]
    snake_direction = (0, 0)
    snake_length = 1

    target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
    target.center = generate_starting_position()
    
    while running:

        screen.fill("black")

        #formatting for the score text 
        score_text = font.render(f"score: {score}", True, (255,255,255))

        #sets position of the score box
        score_rectangle = score_text.get_rect(topleft = (10, info_line))

        #creates rectangle for score 
        pygame.draw.rect(screen, (255,165,0), score_rectangle.inflate(10,5))

        #bilt draws text to screen 
        screen.blit(score_text, score_rectangle)

        #event listner 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #condition checks if the square is out of bounds 
        if is_out_of_bounds():
            snake_length = 1
            target.center = generate_starting_position()
            snake_pixel.center = generate_starting_position()
            snake = [snake_pixel.copy()]
            game_over()

        #condition checks if snake ate the square and controls how to grow
        if snake_pixel.center == target.center:
            target.center = generate_starting_position()
            snake_length += 1
            score += 10
            snake.append(snake_pixel.copy())
            
        #starts game if one of the keys is pressed 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            snake_direction = (0, - pixel_width)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            snake_direction = (0, pixel_width)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            snake_direction = (- pixel_width, 0)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            snake_direction = (pixel_width, 0)
        
        #makes the snake green 
        for snake_part in snake:
            pygame.draw.rect(screen, "green", snake_part)

        #makes the snakes food red 
        pygame.draw.rect(screen, "red", target)

        snake_pixel.move_ip(snake_direction)
        snake.append(snake_pixel.copy())
        snake = snake[-snake_length:]
        
        #updates the ui
        pygame.display.flip()

        #controls the speed of the snake 
        clock.tick(10)

        await asyncio.sleep(0)

    #ends the pygame 
    pygame.quit()
    
asyncio.run(main())