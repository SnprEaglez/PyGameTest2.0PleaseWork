import pygame

# Checking if load in is succesfull
try:
    pygame.init()
except False:
    print("Fail")
else:
    print("Success")

# Basic Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Initializing Display
DisplayX = 400
DisplayY = 400
Display = pygame.display.set_mode((DisplayX, DisplayY))
Display.fill(white)
border = pygame.image.load('Sprites/Border.png')
Display.blit(border, (0, 0))

# Initializing Character Directions
CharacterUp = pygame.image.load('Sprites/Basic Movement/Up.png')
CharacterDown = pygame.image.load('Sprites/Basic Movement/Down.png')
CharacterCenter = pygame.image.load('Sprites/Basic Movement/Center.png')
CharacterRight = pygame.image.load('Sprites/Basic Movement/Right.png')
CharacterLeft = pygame.image.load('Sprites/Basic Movement/Left.png')

# Character Basic Movement Functions
# Character Coords
currentCharacterCoord = [200, 200]
Display.blit(CharacterCenter, (200, 200))
Direction = 'Center'


def moveCharacter():
    global Direction
    if Direction == 'left':
        if currentCharacterCoord[0] > 20:
            currentCharacterCoord[0] -= 10

    elif Direction == 'right':
        if currentCharacterCoord[0] + 20 < 370:
            currentCharacterCoord[0] += 10

    elif Direction == 'up':
        if currentCharacterCoord[1] > 20:
            currentCharacterCoord[1] -= 10

    elif Direction == 'down':
        if currentCharacterCoord[1] + 20 < 350:
            currentCharacterCoord[1] += 10


def makeCharacter():
    Display.fill(white)
    Display.blit(border, (0, 0))
    if Direction == 'up':
        Display.blit(CharacterUp, currentCharacterCoord)
    elif Direction == 'down':
        Display.blit(CharacterDown, currentCharacterCoord)
    elif Direction == 'right':
        Display.blit(CharacterRight, currentCharacterCoord)
    elif Direction == 'left':
        Display.blit(CharacterLeft, currentCharacterCoord)
    else:
        Display.blit(CharacterCenter, currentCharacterCoord)


def checkMoveKey():
    global Direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Direction = "left"
                moveCharacter()
            elif event.key == pygame.K_d:
                Direction = "right"
                moveCharacter()
            elif event.key == pygame.K_w:
                Direction = "up"
                moveCharacter()
            elif event.key == pygame.K_s:
                Direction = "down"
                moveCharacter()
            else:
                pass


while True:
    makeCharacter()
    checkMoveKey()
    pygame.display.update()

# Upload to Github
