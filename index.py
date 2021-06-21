import pygame
import random

pygame.init()  

screenWidth = 1000
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))  
gameOver = False  

green = (0,255,0)
red = (255, 0, 0)

x = 500
y = 400

xMove = 0
yMove = 0

foodX = round(random.randrange(0, screenWidth - 10) / 10) * 10
foodY = round(random.randrange(0, screenHeight - 10) / 10) * 10

snakeArr = []
snakeLength = 1

ms = pygame.time.Clock()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yMove = -10
                xMove = 0
            elif event.key == pygame.K_DOWN:
                yMove = 10
                xMove = 0
            elif event.key == pygame.K_RIGHT:
                xMove = 10
                yMove = 0
            elif event.key == pygame.K_LEFT:
                xMove = -10
                yMove = 0
    x += xMove
    y += yMove
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, red, [foodX, foodY, 10, 10])
    
    snakeArr.append([x, y])

    if len(snakeArr) > snakeLength:
        snakeArr.pop(0)

    for i in snakeArr:
        pygame.draw.rect(screen, green, [i[0], i[1], 10, 10])

    pygame.display.update()

    if x == foodX and y == foodY:
        foodX = round(random.randrange(0, screenWidth - 10) / 10) * 10
        foodY = round(random.randrange(0, screenHeight - 10) / 10) * 10
        snakeLength +=1

    ms.tick(30)
pygame.quit()