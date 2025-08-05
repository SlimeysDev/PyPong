import pygame

# pygame setup
pygame.init()

# screen
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()
running = True

# init player bar
playerWidth = 20
playerHeight = 100

playerXpos = 0
playerYpos = (screenHeight - playerHeight) / 2

# game loop
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

    mouseXpos, mouseYpos = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    playerYpos = mouseYpos - playerHeight / 2

    # check player pos relative to screen size
    if playerYpos < 0:
        playerYpos = 0
    elif playerYpos + playerHeight > screenHeight:
        playerYpos = screenHeight - playerHeight 

    pygame.draw.rect(screen, "white", ((playerXpos, playerYpos), (playerWidth, playerHeight)))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()