import pygame

# pygame setup
pygame.init()

# screen
screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()
running = True

# bar class
class Bar:

    def __init__(self, width, height, maxSpeed):
        self.width = width
        self.height = height
        self.xPos = 0
        self.yPos = (screenHeight - self.height) / 2
        self.maxSpeed = maxSpeed

    def setxPos(self, value):
        self.xPos = value

    def setyPos(self, value):
        self.yPos = value

    def render(self):
        pygame.draw.rect(screen, "white", ((self.xPos, self.yPos), (self.width, self.height)))

# player bar
playerBar = Bar(20, 100, 5)
enemyBar = Bar(20, 100, 5)
enemyBar.setxPos(screenWidth - enemyBar.width)

# ball class
class Ball:

    def __init__(self, radius=float, speed=float):
        self.radius = radius
        self.xPos = 0
        self.yPos = 0
        self.speed = speed

    def setxPos(self, value=float):
        self.xPos = value

    def setyPos(self, value=float):
        self.yPos = value

    def render(self):
        pygame.draw.circle(screen, "white", (self.xPos, self.yPos), self.radius)

# ball
ball = Ball(5, 2)
ball.setxPos(screenWidth / 2)
ball.setyPos(screenHeight / 2)

# game loop
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Make the canvas "blank" again
    screen.fill("black")

    # Update player coordinates
    mousePos = pygame.mouse.get_pos()
    
    newXpos = 0
    playerBar.setxPos(newXpos)
    
    newYpos = mousePos[1] - playerBar.height / 2
    playerBar.setyPos(newYpos)

    # Border collisions
    if playerBar.yPos < 0:
        playerBar.setyPos(0)
    elif playerBar.yPos + playerBar.height > screenHeight:
        playerBar.setyPos(screenHeight - playerBar.height)  

    playerBar.render()
    enemyBar.render()
    ball.render()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()