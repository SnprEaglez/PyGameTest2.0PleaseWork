import pygame

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
border = pygame.image.load('Border.png')
Display.blit(border, (0, 0))


# Stop Display

def checkStopPlay():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

# Character Functions
# Initializing Character
CharacterUp = pygame.image.load('Up.png')
CharacterDown = pygame.image.load('Down.png')
CharacterCenter = pygame.image.load('Center.png')
CharacterRight = pygame.image.load('Right.png')
CharacterLeft = pygame.image.load('left.png')
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


def checkMoveKey():
    global Direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            print("hi")
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