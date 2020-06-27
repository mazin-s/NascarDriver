import pygame
import time
import random
from pygame.locals import *

# Global Variables
pygame.init() # init() initialize all imported pygame modules
clock = pygame.time.Clock() # lets us use clock

WIDTH =  800 # Screen width
HEIGHT = 600 # Screen height
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Set Screen dimensions

white = (255,255,255)
black = (0,0,0)
grey = (169, 130,130)
red = (200,0,0)
brightRed = (255,0,0)
green  =  (0,200,0)
brightGreen = (0,255,0)
darkGreen  = (0,150,0)
yellow = (200,200,0)
brightYellow = (250,250,0)
blue = (0,0,0)

smallFont  =  pygame.font.Font('freesansbold.ttf', 20)
mediumFont = pygame.font.Font('freesansbold.ttf', 24)
# End Global Variables

crashSound = pygame.mixer.Sound("crashmusic.wav") # Loading sound
menuScreen = pygame.image.load('menuWallpaper.jpg') # Loading music
music = pygame.mixer.music.load("menuMusic.mp3") # Loading music
pygame.mixer.music.play(-1) # Play menu music endless loop


# mainCar = pygame.image.load("mainCar.png")
mainCar = pygame.transform.scale(pygame.image.load('mainCar.png').convert_alpha(),(100,100))

def thingsDodged(count):
    text = mediumFont.render("Score: " + str(count), True, white)
    screen.blit(text,(0,0))
    
    
def messageToScreen(font,msg,color,x,y,fontSize):                                                            
    '''
    messageToScreen is a function that outputs to the screen
    ---param
    msg: string
    color: tuple
    x:int(x coordinate)
    y:int(y coordinate)
    z:int(size of input text)
    ---return:none
    '''
    font = pygame.font.Font('freesansbold.ttf',fontSize)
    screenText = font.render(msg, True, color) #set message
    screen.blit(screenText,[x,y])


def messageWithRectangles(font ,text, textColor,rectColor,x,y):
    textSurf = font.render(text,True,textColor,rectColor)
    textRect =  textSurf.get_rect()
    textRect.center  =  (x,y)
    screen.blit(textSurf,textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(font, msg, x, y, w, h,inactiveColor, activeColor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
        # print mouse
    if  (x < mouse[0] < x + w) and  (y < mouse[1] < y + h):
            pygame.draw.rect(screen,activeColor,(x,y,w,h))
            if click[0] ==  1 and action != None:
                action()
    else:
        pygame.draw.rect(screen,inactiveColor,(x,y,w,h))
        
    TextSurf, TextRect = text_objects(msg, font)
    TextRect.center = ((x + w/2),(y + h/2))
    screen.blit(TextSurf, TextRect)

def crashDisplay(text):
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ( (WIDTH/2), (150) )
    screen.blit(TextSurf, TextRect)
    # screen.update()
    pygame.display.update()

    time.sleep(2)

    runGame()
    
def crash():

    # pygame.mixer.music.stop()
    # pygame.mixer.Sound.play("crashSoundEffect.mp3")
    # messageToScreen(mediumFont,"You Crashed",red,WIDTH/2 - 150,HEIGHT/2,40)
    # pygame.display.update()
    # runGame()
    
    crashDisplay("GAMEOVER")


def displayMainCar(x,y):
    screen.blit(mainCar, (x,y))

def things(thingX,thingY,thingW,thingH, color):
    pygame.draw.rect(screen, color, [thingX, thingY, thingW, thingH])
    
def runGame():
    x = WIDTH *  0.42
    xChange = 0
    y = HEIGHT * 0.8
    thingStartX = random.randrange(0,WIDTH)
    thingStartY = -600
    thingSpeed = 20
    thingWidth = 200
    thingHeight = 200
    carWidth = 60
    

    music = pygame.mixer.music.load("gameMusic.mp3")
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Game")

    dodged = 0
    
    gameExit = False
    while not gameExit:

        for event in pygame.event.get(): #  tracks what im doing really fast
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -15
                elif event.key == pygame.K_RIGHT:
                    xChange = 15

            if  event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:x
                xChange = 0
        
                
        x += xChange             

        screen.fill(grey) #  anything that was there  before got written over

        things(thingStartX,thingStartY,thingWidth,thingHeight, white)
        thingStartY += thingSpeed
        
        displayMainCar(x,y) # THIS HAS TO GO after the screen fill
        thingsDodged(dodged)

        if x > WIDTH - carWidth or x < 0: # COLLISION DETECTION 70 is with of  image
            crash()

        if thingStartY > HEIGHT:
            thingStartY  = 0 - thingHeight
            thingStartX =  random.randrange(0,WIDTH)
            dodged += 1
            thingSpeed +=  5 # ADDS SPEED EVERYTIME IMPORTANT QUESTION HERE--------------------------------------
            thingWidth *= 1.05 #ADDS WIDTH SIZE

        
        if y < thingStartY + thingHeight:
            # print("y crossover")
            if  x > thingStartX and x < thingStartX + thingWidth or  x + carWidth > thingStartX and x + carWidth < thingStartX + thingWidth:
                # print( " x crossover")
                crash()
        
            
        pygame.display.update()
        clock.tick(60)

def quitGame():
   # music = pygame.mixer.music.load("gameMusic.mp3")
    #pygame.mixer.music.play(-1)
    pygame.quit()
    quit()
    
def mainMenu():


    continueMenu = True
    while continueMenu:

        for event in pygame.event.get(): #  tracks what im doing really fast
            if event.type == pygame.QUIT:
                pygame.quit()
                notCrashed = False

            # print(event)

        # Menu Screen Labels
        screen.blit(pygame.transform.scale(menuScreen, (800, 600)), (0, 0))
        pygame.display.set_caption("Main Menu")
        messageToScreen(mediumFont, "Nascar Driver", red, 275, 100, 40)
        messageWithRectangles(mediumFont ,"Developed By Mazin S", red, white, WIDTH/2,566)


        # button(smallFont, "PLAY!", 60, 280, 80, 40, green, brightGreen, "play")
        button(smallFont, "PLAY!", 60, 280, 80, 40, green, brightGreen, runGame)
        button(smallFont, "QUIT!", 60, 400, 80, 40, red, brightRed, crash)

        pygame.display.update()
        # End Menu Screen Labels

    
        
        # Set Menu Screen Labels
        clock.tick(60)
        


mainMenu()        
quit()




