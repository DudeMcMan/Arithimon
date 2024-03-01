import pygame
import math
import sys
from sys import exit
from random import randint
from random import random
from pygame import mixer

# for running python3 TheCode/arithimon.py
# assuming the directory is the same

#Currently, this is unused
class gameTitle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        gameTitle = pygame.image.load("Items/arithilogo.png").convert_alpha()
        gameTitle = pygame.transform.scale_by(gameTitle, (1/2, 1/2))
       
        self.image = gameTitle
        self.rect = self.image.get_rect(center=(410, 150))

#Startup screens in order
class theABCD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        teamLogo = pygame.image.load("Items/ABCD.png").convert_alpha()
        teamLogo = pygame.transform.scale_by(teamLogo, (1.05, 1.1))
       
        self.image = teamLogo
        self.rect = self.image.get_rect(center=(675, 450))
class menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        gameMenu = pygame.image.load("Items/arithimon v2.png").convert_alpha()
        #gameMenu = pygame.transform.scale_by(gameMenu, (0.5, 0.5))
       
        self.image = gameMenu
        self.rect = self.image.get_rect(center=(675, 400))

#Backgrounds
class diffSelectBackground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        gameMenu = pygame.image.load("Items/menuBackground.png").convert_alpha()
        #gameMenu = pygame.transform.scale_by(gameMenu, (0.5, 0.5))
       
        self.image = gameMenu
        self.rect = self.image.get_rect(center=(675, 400))
class battleScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        battleScreen1 = pygame.image.load("Items/Hintergrund.png").convert_alpha()
        #battleScreen1 = pygame.transform.scale_by(battleScreen1, (1/2, 1/2))
       
        self.image = battleScreen1
        self.rect = self.image.get_rect(center=(675, 400))

#Characters
class playerAppleKun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        playerAppleKun = pygame.image.load("Items/Apple-kun.png").convert_alpha()
        #playerAppleKun = pygame.image.load("Items/New Piskel (1).gif").convert_alpha()
        playerAppleKun = pygame.transform.scale_by(playerAppleKun, (2, 2))
        playerAppleKun = pygame.transform.flip(playerAppleKun, True, False)
       
        self.image = playerAppleKun
        self.rect = self.image.get_rect(center=(200, 400))
class enemyAppleKun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        enemyAppleKun = pygame.image.load("Items/Apple-kun.png").convert_alpha()
        enemyAppleKun = pygame.transform.scale_by(enemyAppleKun, (2, 2))
       
        self.image = enemyAppleKun
        self.rect = self.image.get_rect(center=(1150, 315))
class playerBarry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        playerBarry = pygame.image.load("Items/Barry.png").convert_alpha()
        playerBarry = pygame.transform.scale_by(playerBarry, (2, 2))
        playerBarry = pygame.transform.flip(playerBarry, True, False)
       
        self.image = playerBarry
        self.rect = self.image.get_rect(center=(200, 350))
class enemyBarry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        enemyBarry = pygame.image.load("Items/Barry.png").convert_alpha()
        enemyBarry = pygame.transform.scale_by(enemyBarry, (2, 2))
       
        self.image = enemyBarry
        self.rect = self.image.get_rect(center=(1150, 315))
class playerRuley(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        playerRuley = pygame.image.load("Items/Ruley.png").convert_alpha()
        playerRuley = pygame.transform.scale_by(playerRuley, (2, 2))
        playerRuley = pygame.transform.flip(playerRuley, True, False)
       
        self.image = playerRuley
        self.rect = self.image.get_rect(center=(200, 370))
class enemyRuley(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        enemyRuley = pygame.image.load("Items/Ruley.png").convert_alpha()
        enemyRuley = pygame.transform.scale_by(enemyRuley, (2, 2))
       
        self.image = enemyRuley
        self.rect = self.image.get_rect(center=(1150, 340))

#Button class
class Button:
    def __init__(self, screen, text, width, height, pos, elevation, event, key = None, alternateKey = None):
        #Core attributes 
        self.screen = screen
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.event = event
        self.key = key
        self.alternateKey = alternateKey if alternateKey is not None else key
        self.buttonActive = True

        # top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'
        self.original_top_rect = pygame.Rect((pos[0],pos[1]-elevation), (width,height))

        # bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
        #text
        self.text_surf = pygame.font.Font("Items/Pixeltype.ttf", 50).render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
        self.onButton = False

    def draw(self):
        # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(self.screen,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(self.screen,self.top_color, self.top_rect,border_radius = 12)
        self.screen.blit(self.text_surf, self.text_rect)
        self.check_click()
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        self.onButton = False
        if pygame.key.get_pressed()[self.key] or pygame.key.get_pressed()[self.alternateKey] or self.original_top_rect.collidepoint(mouse_pos) or self.top_rect.collidepoint(mouse_pos) if self.key is not None else self.original_top_rect.collidepoint(mouse_pos) or self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            self.onButton = True
            if pygame.key.get_pressed()[self.key] or pygame.key.get_pressed()[self.alternateKey] or pygame.mouse.get_pressed()[0] if self.key is not None else pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    pygame.event.post(pygame.event.Event(self.event))
        else:
            if self.pressed and not pygame.mouse.get_pressed()[0]:
                print("test")
                pygame.event.post(pygame.event.Event(self.event))
            self.pressed = False
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'

#Question class
class Question:
    questionText = ""
    answer = 0
    def createEasy():
        Question.questionText = ""
        temp = randint(1,4)
        # temp = 2
        if(temp==1):
            #+
            firstInt = randint(0,12)
            secondInt = randint(0,12)
            Question.questionText = str(firstInt)+" + "+str(secondInt)+" = ?"
            Question.answer = firstInt+secondInt
        elif(temp==2):
            #-
            firstInt = randint(0,12)
            secondInt = randint(0,12)
            while(firstInt-secondInt<0):
                firstInt = randint(0,12)
                secondInt = randint(0,12)
            Question.questionText = str(firstInt)+" - "+str(secondInt)+" = ?"
            Question.answer = firstInt-secondInt
        elif(temp==3):
            #*
            firstInt = randint(0,12)
            secondInt = randint(0,12)
            while(firstInt*secondInt>50):
                firstInt = randint(0,12)
                secondInt = randint(0,12)
            Question.questionText = str(firstInt)+" * "+str(secondInt)+" = ?"
            Question.answer = firstInt*secondInt
        else:
            #/
            firstInt = randint(0,12)
            secondInt = randint(1,12)
            while(firstInt%secondInt!=0):
                firstInt = randint(0,12)
                secondInt = randint(1,12)
            Question.questionText = str(firstInt)+" / "+str(secondInt)+" = ?"
            Question.answer = (int)(firstInt/secondInt)
            
    def createNormal():
        Question.questionText = ""
        while(True):
            try:
                firstInt = randint(0, 12)
                secondInt = randint(0, 12)
                thirdInt = randint(0, 12)
                operation1 = randint(1,4)
                operation2 = randint(1,4)
                operations = {1: " + ", 2: " - ", 3: " * ", 4: " / "}
                
                parenthesis = randint(0, 1)
                if parenthesis:
                    #If there will be parenthesis in the equation
                    parenthesisNum = 0
                    parenthesisText = ""
                    parenthesis = randint(0, 1)
                    if parenthesis:
                        #Parenthesis location (firstInt and secondInt) or (secondInt and thirdInt)
                        if operation2 == 4:
                            if thirdInt == 0: 
                                thirdInt = randint(1,12)
                            if operation1 == 4 and secondInt == 0: 
                                secondInt = randint(1, 12)
                            while(secondInt % thirdInt != 0): 
                                secondInt = randint(0, 12)
                                thirdInt = randint(1, 12)
                        parenthesisText = "(" + str(secondInt) + operations[operation2] + str(thirdInt) + ")"
                        parenthesisNum = eval(parenthesisText)
                        
                        if operation1 == 4:
                            while parenthesisNum == 0:
                                secondInt = randint(0, 12)
                                if operation2 == 4:
                                    thirdInt = randint(1, 12)
                                else: 
                                    thirdInt = randint(0, 12)
                                parenthesisText = "(" + str(secondInt) + operations[operation2] + str(thirdInt) + ")"
                                parenthesisNum = eval(parenthesisText)
                            
                            while firstInt % parenthesisNum != 0:
                                firstInt = randint(0, 12)
                                secondInt = randint(0, 12)
                                thirdInt = randint(0, 12)
                                if operation2 == 3 or operation2 == 4:
                                    if secondInt == 0: secondInt = randint(1, 12)
                                    if thirdInt == 0: thirdInt = randint(1,12)
                                    if operation2 == 4:
                                        while(secondInt % thirdInt != 0): 
                                            secondInt = randint(1, 12)
                                            thirdInt = randint(1, 12)
                                else:
                                    while eval(str(secondInt) + operations[operation2] + str(thirdInt)) == 0:
                                        secondInt = randint(0, 12)
                                        thirdInt = randint(0, 12)
                                parenthesisText = "(" + str(secondInt) + operations[operation2] + str(thirdInt) + ")"
                                parenthesisNum = eval(parenthesisText)
                        Question.questionText = str(firstInt) + operations[operation1] + parenthesisText
                        Question.answer = int(eval(Question.questionText))
                        Question.questionText += " = ?"
                        break
                                    
                    else:
                        if operation1 == 4:
                            if secondInt == 0: 
                                secondInt = randint(1,12)
                            while(firstInt % secondInt != 0): 
                                firstInt = randint(0, 12)
                                secondInt = randint(1, 12)
                        parenthesisText = "(" + str(firstInt) + operations[operation1] + str(secondInt) + ")"
                        parenthesisNum = eval(parenthesisText)
                        
                        if operation2 == 4:
                            if thirdInt == 0: thirdInt = randint(1, 12)
                            while(parenthesisNum % thirdInt != 0):
                                firstInt = randint(0, 12)
                                secondInt = randint(0, 12)
                                thirdInt = randint(1, 12)
                                if operation1 == 4:
                                    if secondInt == 0: 
                                        secondInt = randint(1,12)
                                    while(firstInt % secondInt != 0): 
                                        firstInt = randint(0, 12)
                                        secondInt = randint(1, 12)
                                parenthesisText = "(" + str(firstInt) + operations[operation1] + str(secondInt) + ")"
                                parenthesisNum = eval(parenthesisText)
                        Question.questionText = parenthesisText + operations[operation2] + str(thirdInt)
                        Question.answer = int(eval(Question.questionText))
                        Question.questionText += " = ?"
                        break
                    
                else:
                    groupNum = 0
                    groupText = ""
                    if operation1 == 3 or operation1 == 4:
                        if operation1 == 4: 
                            if secondInt == 0: secondInt = randint(1, 12)
                            while(firstInt % secondInt != 0):
                                firstInt = randint(0, 12)
                                secondInt = randint(1, 12)
                        groupText = str(firstInt) + operations[operation1] + str(secondInt)
                        groupNum = eval(groupText)
                        
                        if operation2 == 4 :
                            if thirdInt == 0: thirdInt = randint(1, 12)
                            while(groupNum % thirdInt != 0):
                                firstInt = randint(0, 12)
                                secondInt = randint(0, 12)
                                thirdInt = randint(1, 12)
                                if operation1 == 4: 
                                    if secondInt == 0: secondInt = randint(1, 12)
                                    while(firstInt % secondInt != 0):
                                        firstInt = randint(0, 12)
                                        secondInt = randint(1, 12)
                                groupText = str(firstInt) + operations[operation1] + str(secondInt)
                                groupNum = eval(groupText)
                        Question.questionText = groupText + operations[operation2] + str(thirdInt)
                        Question.answer = int(eval(Question.questionText))
                        Question.questionText += " = ?"
                        break
                            
                    elif operation2 == 3 or operation2 == 4:
                        if operation2 == 4:
                            if thirdInt == 0: thirdInt = randint(1, 12)
                            while(secondInt % thirdInt != 0):
                                secondInt = randint(0, 12)
                                thirdInt = randint(1, 12)
                        groupText = str(secondInt) + operations[operation2] + str(thirdInt)
                        groupNum = eval(groupText)
                        Question.questionText = str(firstInt) + operations[operation1] + groupText
                        Question.answer = int(eval(Question.questionText))
                        Question.questionText += " = ?"
                        break
                    else:
                        Question.questionText = str(firstInt) + operations[operation1] + str(secondInt) + operations[operation2] + str(thirdInt)
                        Question.answer = int(eval(Question.questionText))
                        Question.questionText += " = ?"
                        break
            except ZeroDivisionError:
                print("When creating a normal difficulty equation, 0 was divided. Probably want to look into that")
                pygame.quit()
                exit()
                break
    
    def createHard():
        Question.questionText = ""
        temp = randint(1,2)
        # temp = 2
        if(temp==1):
            #+
            firstInt = randint(1,12)
            secondInt = randint(1,12)
            thirdInt = randint(1, 12)
            while (thirdInt - secondInt) % firstInt !=0:
                firstInt = randint(1,12)
                secondInt = randint(1,12)
                thirdInt = randint(1, 12)
            Question.questionText = str(firstInt)+"x + "+str(secondInt)+" = " + str(thirdInt)
            Question.answer = int((thirdInt - secondInt) / firstInt)

        else:
            #-
            firstInt = randint(1,12)
            secondInt = randint(1,12)
            thirdInt = randint(1, 12)
            while (thirdInt + secondInt) % firstInt !=0:
                firstInt = randint(1,12)
                secondInt = randint(1,12)
                thirdInt = randint(1, 12)
            Question.questionText = str(firstInt)+"x - "+str(secondInt)+" = " + str(thirdInt)
            Question.answer = int((thirdInt + secondInt) / firstInt)

    def createExtreme():
        Question.questionText = ""
        temp = randint(1, 3)
        if temp == 1:
            Question.createEasy()
        elif temp == 2:
            Question.createNormal()
        else:
            Question.createHard()

#Healthbar during battle
def healthBar(screen, health, damage, damageRect, healthRect, clock):
    #healthBar(screen, michael, alvin, otherDamageRect, otherHealthRect, clock)
    player_health = health / 2
    newHealth = (float(health) - float(damage))/2.0
    if newHealth < 0:
        newHealth = 0
    WIDTH, HEIGHT = 1350, 800
    FPS = 30
    clock = pygame.time.Clock()

    # Health bar properties
    health_bar_width = 200
    health_bar_height = 25
    health_bar_x = damageRect.left
    health_bar_y = damageRect.top

    # Health bar speed (decrease per second)
    health_bar_speed = 50

    # Main game loop
    while player_health >= newHealth:

        # Update health
        player_health -= health_bar_speed / FPS

        # Snaps to grid, makes whole number
        player_health = round(player_health)
        
        # Draw health bar
        pygame.draw.rect(screen, "red", (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, "green", (health_bar_x, health_bar_y, player_health * (health_bar_width / 100), health_bar_height))

        # Update display
        pygame.display.update()

        clock.tick(FPS)


            
def main():
    pygame.init()
    pygame.display.set_caption('Arithimon') #window name
    #pygame.display.set_icon() #window icon
    screenWidth = 1350 #the width
    screenHeight = 800 #the height
    screen = pygame.display.set_mode((screenWidth, screenHeight)) #the display
   
    clock = pygame.time.Clock() #needed for frame rate
    
    clickSound = pygame.mixer.Sound("Items/zipclick.wav") #Adds the click sound effect
    
    jeremy = 0 # this is for the start up screen, so it can change
    michael = 200 # to make te health bar go down
    battleTimer = 0 #deducts from base
    alvin = 0 #damage deduction
    simon = 200 #to make health bar go down 
    theodre = 200 #damage deduction base
    ash = 0 #time stayed on enemy turn
    kat = False #to help change screen
    beavis = 0 #for character sprite randomization
    butthead = 0 #for character sprite randomization
    correct = False #tells if answer is correct
    carl = 0 #to slow down the game a bit
    weezer = 0 #to help with damage calc
    win = False #tells if the player has won
    done = False #tells if the match is over
    oNeal = 0 #damage reduction
    gameActive = False
    diffSelect = False
    diffEasy = False
    diffNormal = False
    diffHard = False
    diffExtreme = False
    answered = False
    playerTurn = True
    textActive = False
    diffSelectButtonsActive = True
    returnButtonActive = False
    
    userText = "Input\u00A0Here"
 
    # text rect
    inputRect = pygame.Rect(580, 200, 140, 32)
    playerHealthRect = pygame.Rect(100, 500, michael, 25)
    playerDamageRect = pygame.Rect(100, 500, 200, 25)
    otherHealthRect = pygame.Rect(1000, 175, michael, 25)
    otherDamageRect = pygame.Rect(1000, 175, 200, 25)
   
    # colorActive stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    colorActive = pygame.Color('lightskyblue3')
 
    # colorPassive store color(chartreuse4) which is
    # color of input box.
    colorPassive = pygame.Color('chartreuse4')
    color = colorPassive
 
    title = pygame.sprite.GroupSingle()#the title
    title.add(theABCD())
    
    background = pygame.sprite.GroupSingle()
    background.add(battleScreen())
    
    menuBackground = pygame.sprite.GroupSingle()
    menuBackground.add(diffSelectBackground())

    
    playerSprite = pygame.sprite.Group()
    #playerSprite.add(playerBarry())
    
    enemySprite = pygame.sprite.Group()
    #enemySprite.add(enemyBarry())
   
    theFont = pygame.font.Font("Items/Pixeltype.ttf", 50) #The font, most likely temporary
   
    gameMessage = theFont.render("Press Enter To Start", False, "black") #how to start the game
    gameMessageRect = gameMessage.get_rect(center=(400, 450))
   
    secretMessage = theFont.render("Sick", False, "white") #for fun
    secretMessageRect = secretMessage.get_rect(center=(675, 400))
   
    # answerMessage = theFont.render("Click To Answer (Or Press Enter)", False, "black") #temporary answer button
    # answerMessageRect = answerMessage.get_rect(center=(675, 600))
   
    wrongMessage = theFont.render("Incorrect", False, "white") #temporary answer button
    wrongMessageRect = wrongMessage.get_rect(center=(675, 400))

   
    tempMessage = theFont.render("Select Your Difficulty", False, "black") #temporary start game message
    tempMessageRect = tempMessage.get_rect(center=(675, 150))
   
    # tempMessageDiffTwo = theFont.render("(1)Easy", False, "black") #temporary difficulty option
    # tempMessageRectDiffTwo = tempMessageDiffTwo.get_rect(center=(675, 300))
    
    # tempMessageDiffThree = theFont.render("(2)Normal", False, "black") #temporary difficulty option
    # tempMessageRectDiffThree = tempMessageDiffThree.get_rect(center=(675, 400))
    
    # tempMessageDiffFour = theFont.render("(3)Solve for x", False, "black") #temporary difficulty option
    # tempMessageRectDiffFour = tempMessageDiffFour.get_rect(center=(675, 500))
    
    # tempMessageDiffFive = theFont.render("(4)Extreme", False, "black") #temporary difficulty option
    # tempMessageRectDiffFive = tempMessageDiffFive.get_rect(center=(675, 600))
    
    # messageBack = theFont.render("Return to Difficulty Selection", False, "black") #temporary message
    # messageRectBack = messageBack.get_rect(center=(675, 600))
    
    questionMessage = theFont.render("Placeholder", False, "white") #Message used for displaying the question
    questionMessageRect = questionMessage.get_rect(center=(675, 150))
    
    tempMessageTurn = theFont.render("Enemy Turn", False, "white") #temporary message
    tempMessageRectTurn = tempMessageTurn.get_rect(center=(675, 150))
    
    tempMessageWin = theFont.render("You Win", False, "white") #temporary message
    tempMessageRectWin = tempMessageWin.get_rect(center=(675, 150))
    
    tempMessageLose = theFont.render("You Lose", False, "white") #temporary message
    tempMessageRectLose = tempMessageLose.get_rect(center=(675, 150))
    
    #tempMessageNormal = theFont.render("Normal Mode Selected", False, "white") #temporary message
    #tempMessageRectNormal = tempMessageNormal.get_rect(center=(675, 150))
   
    # tempMessageHard = theFont.render("Hard Mode Selected", False, "white") #temporary message
    # tempMessageRectHard = tempMessageHard.get_rect(center=(675, 150))
   
    # tempMessageExtreme = theFont.render("Extreme Mode Selected", False, "white") #temporary message
    # tempMessageRectExtreme = tempMessageExtreme.get_rect(center=(675, 150))
   
    #timers
    startUpTimer = pygame.USEREVENT + 1
    pygame.time.set_timer(startUpTimer, 2000)

    #Starts menu music immediately
    mixer.init()
    mixer.music.load('Items/menuMusic.wav')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)
    
    easyButtonClick = pygame.USEREVENT + 2
    normalButtonClick = pygame.USEREVENT + 3
    hardButtonClick = pygame.USEREVENT + 4
    extremeButtonClick = pygame.USEREVENT + 5
    answerButtonClick = pygame.USEREVENT + 6
    returnButtonClick = pygame.USEREVENT + 7
    
    easyDiffButton = Button(screen, '(1) Easy - Two Number Arithmetic', 600, 40, (375, 280), 5, easyButtonClick, pygame.K_1, pygame.K_KP1)
    normalDiffButton = Button(screen, '(2) Normal - Three Number Arithmetic', 600, 40, (375, 380), 5, normalButtonClick, pygame.K_2, pygame.K_KP2)
    hardDiffButton = Button(screen, '(3) Hard - Solve For x', 600, 40, (375, 480), 5, hardButtonClick, pygame.K_3, pygame.K_KP3)
    extremeDiffButton = Button(screen, '(4) Extreme - All', 600, 40, (375, 580), 5, extremeButtonClick, pygame.K_4, pygame.K_KP4)
    answerButton = Button(screen, 'Click To Answer (Or Press Enter)', 600, 40, (375, 580), 5, answerButtonClick, pygame.K_RETURN, pygame.K_KP_ENTER)
    returnButton = Button(screen, 'Return to Difficulty Selection', 600, 40, (375, 580), 5, returnButtonClick, pygame.K_RETURN, pygame.K_KP_ENTER)
    
    while True:
        battleTimer = int(pygame.time.get_ticks() / 100) #Every tenth of a second is tracked
        # print("FPS: "+str(pygame.time.Clock.get_fps(clock))) #To test FPS if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #this will close the game
                pygame.quit()
                exit()
            
            if event.type == returnButtonClick: #Back to diffSelect
                diffSelect = True
                win = False
                done = False
                diffEasy = False
                diffNormal = False
                diffHard = False
                diffExtreme = False
                playerTurn = True
                answered = False
                userText = "Input\u00A0Here"
                clickSound.play()
                mixer.music.load('Items/menuMusic.wav')
                mixer.music.set_volume(0.1)
                mixer.music.play(-1)
                pygame.sprite.Group.empty(playerSprite)
                pygame.sprite.Group.empty(enemySprite)
                beavis = 0
                butthead = 0
                diffSelectButtonsActive = True
            elif event.type == answerButtonClick and playerTurn:
                if userText != "Input\u00A0Here" and userText != "":
                    answered = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
               
                if inputRect.collidepoint(event.pos) and playerTurn:
                    textActive = True
                    if userText == "": userText = "Input\u00A0Here" 
                else:
                    textActive = False
                    if userText == "": userText = "Input\u00A0Here" 
           
            if textActive:
                
                if event.type == pygame.KEYDOWN:
                    # if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                    #     if textActive:
                    #         answered = True
 
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        if userText == "Input\u00A0Here": userText = ""
                        # get text input from 0 to -1 i.e. end.
                        userText = userText[:-1]
                        
                    elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_DELETE):
                        pass
                        #prevents enter from being typed
 
                    # Unicode standard is used for string formation
                    else:
                        if userText == "Input\u00A0Here": userText = ""
                        userText += event.unicode
                        print(event.mod)
                        if event.mod in (4097, 4098, 4160, 4224, 4352, 4608):
                            print("True! "+str(event.key))
            elif userText == "": userText = "Input\u00A0Here"
           
            if gameActive:
                if diffSelect:
                    # button1.draw()
                    # if(button1.clicked):
                    #     print("YE") #FIX THIS
                    userText = "Input\u00A0Here"
                    
                    michael = 200
                    simon = 200
                    
                    otherHealthRect.update(1000, 175, michael, 25)
                    playerHealthRect.update(100, 500, simon, 25)
                    
                    if beavis == 0:
                        beavis = randint(1, 3)
                    if butthead == 0:
                        butthead = randint(1, 3)
                    
                    if beavis == 1:
                        playerSprite.add(playerAppleKun())
                    elif beavis == 2:
                        playerSprite.add(playerBarry())
                    elif beavis == 3:
                        playerSprite.add(playerRuley())
                        
                    if butthead == 1:
                        enemySprite.add(enemyAppleKun())
                    elif butthead == 2:
                        enemySprite.add(enemyBarry())
                    elif butthead == 3:
                        enemySprite.add(enemyRuley())
                    
                    if event.type == easyButtonClick:
                        clickSound.play()
                        diffEasy = True
                        diffSelect = False
                        textActive = True
                        weezer = battleTimer
                        Question.createEasy()
                        questionMessage = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                        mixer.music.stop()
                        mixer.music.load('Items/battleMusic.wav')
                        mixer.music.set_volume(0.2)
                        mixer.music.play(-1)
                    if event.type == normalButtonClick:
                        clickSound.play()
                        diffNormal = True
                        diffSelect = False
                        textActive = True
                        weezer = battleTimer
                        Question.createNormal()
                        questionMessage = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                        mixer.music.stop()
                        mixer.music.load('Items/battleMusic.wav')
                        mixer.music.set_volume(0.2)
                        mixer.music.play(-1)
                    if event.type == hardButtonClick:
                        clickSound.play()
                        diffHard = True
                        diffSelect = False
                        textActive = True
                        weezer = battleTimer
                        Question.createHard()
                        questionMessage = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                        mixer.music.stop()
                        mixer.music.load('Items/battleMusic.wav')
                        mixer.music.set_volume(0.2)
                        mixer.music.play(-1)
                    if event.type == extremeButtonClick:
                        clickSound.play()
                        diffExtreme = True
                        diffSelect = False
                        textActive = True
                        weezer = battleTimer
                        Question.createExtreme()
                        questionMessage = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                        mixer.music.stop()
                        mixer.music.load('Items/battleMusic.wav')
                        mixer.music.set_volume(0.2)
                        mixer.music.play(-1)
            else:
                #How to start the game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                    clickSound.play()
                    gameActive = True
                    diffSelect = True
                   
        # screen.fill("white") #fills the screen with a specific color
        menuBackground.draw(screen)
        
        if gameActive:
            
            screen.blit(tempMessage, tempMessageRect)
            
            if not diffSelect: #Battle screen
                diffSelectButtonsActive = False
                if win and done: #Won
                    #screen.fill("gray")
                    background.draw(screen)
                    screen.blit(tempMessageWin, tempMessageRectWin)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)
                    
                if win == False and done: #Lost
                    mixer.music.stop()
                    #screen.fill("gray")
                    background.draw(screen)
                    screen.blit(tempMessageLose, tempMessageRectLose)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)
                
                if playerTurn and done == False: #Player turn
                    
                    #screen.fill("gray")
                    background.draw(screen)
                    screen.blit(questionMessage, questionMessageRect)
                    answerButton.draw()
                    
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)
                
                    if textActive:
                        color = colorActive
                    else:
                        color = colorPassive
                    
                    text_surface = theFont.render(userText, True, (255, 255, 255))
                    
                    # set width of textfield so that text cannot get outside of user's text input
                    inputRect.w = max(100, text_surface.get_width()+10)
                    
                    # draw rectangle and argument passed which should be on screen
                    pygame.draw.rect(screen, color, inputRect)
        
                    # render at position stated in arguments
                    screen.blit(text_surface, (inputRect.x+5, inputRect.y+5))
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)

                    if battleTimer - weezer <= 600:
                        #y = -28log(x + 1) + 120
                        alvin = -28 * math.log10(battleTimer - weezer + 1) + 120
                    
                    if answered:
                        if userText == str(Question.answer):
                            
                            if alvin < 0: #If player damage below 0, then it is set to 0
                                alvin = 0
                            
                            healthBar(screen, michael, alvin, otherDamageRect, otherHealthRect, clock)
                            michael -= alvin
                            if michael < 0: #If enemy health is below 0, then it is set to 0
                                michael = 0
                                
                            if michael == 0: #Enemy health at 0, player win
                                otherHealthRect.update(1000, 175, michael, 25)
                                screen.blit(secretMessage, secretMessageRect)
                                win = True
                                done = True
                                correct = True
                                answered = False
                                textActive = False
                                playerTurn = False
                                kat = False
                                carl = 0
                                weezer = 0
                                mixer.music.stop()
                                mixer.music.load('Items/victoryMusic.wav')
                                mixer.music.set_volume(0.2)
                                mixer.music.play(-1)
                                
                            else: #Enemy health not yet 0, go to computer turn
                                otherHealthRect.update(1000, 175, michael, 25)
                                correct = True
                                answered = False
                                textActive = False
                                playerTurn = False
                                kat = False
                                carl = 0
                                weezer = battleTimer

                        else: #Wrong, go to computer turn
                            screen.blit(wrongMessage, wrongMessageRect)
                            correct = False
                            answered = False
                            textActive = False
                            playerTurn = False
                            kat = False
                            carl = 0
                            weezer = battleTimer
                            
                elif playerTurn == False and done == False: #Enemy turn
                    
                    ash = int(pygame.time.get_ticks() / 100)
                    #screen.fill("gray")
                    background.draw(screen)
                    screen.blit(tempMessageTurn, tempMessageRectTurn)
                    
                    if correct == False:
                        screen.blit(wrongMessage, wrongMessageRect)
                    else:
                        screen.blit(secretMessage, secretMessageRect)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)
                    
                    if ash % 2 == 0:
                        carl += 1
                        
                    if carl == 10:
                        kat = True
                    
                    if kat:
                        if randint(1, 50) == 1: #1 in 50 chance to not hit
                            playerTurn = True
                            userText = "Input\u00A0Here"
                            weezer = battleTimer
                            if diffEasy:    
                                Question.createEasy()
                                questionMessage = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                            elif diffNormal:
                                Question.createNormal()
                                questionMessage = theFont.render(Question.questionText, False, "white")
                            elif diffHard:
                                Question.createHard()
                                questionMessage = theFont.render(Question.questionText, False, "white")
                            elif diffExtreme:
                                Question.createExtreme()
                                questionMessage = theFont.render(Question.questionText, False, "white")
                            textActive = True
                                
                        else:
                            oNeal = -28 * math.log10((math.floor(20+(600-20)*random()**2)) + 1) + 120
                            healthBar(screen, simon, oNeal, playerDamageRect, playerHealthRect, clock)
                            simon -= oNeal
                            
                            if simon < 0:
                                simon = 0
                                
                            if simon == 0: #Player health at 0, computer win
                                playerHealthRect.update(100, 500, simon, 25)
                                done = True
                                kat = False
                                carl = 0
                                weezer = 0
                            
                            else: #Player health not yet 0, go to player turn
                                playerHealthRect.update(100, 500, simon, 25)
                                playerTurn = True
                                userText = "Input\u00A0Here"
                                weezer = battleTimer
                                if diffEasy:    
                                    Question.createEasy()
                                    questionMessage = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                                elif diffNormal:
                                    Question.createNormal()
                                    questionMessage = theFont.render(Question.questionText, False, "white")
                                elif diffHard:
                                    Question.createHard()
                                    questionMessage = theFont.render(Question.questionText, False, "white")
                                elif diffExtreme:
                                    Question.createExtreme()
                                    questionMessage = theFont.render(Question.questionText, False, "white")
                                textActive = True
            
            if diffSelectButtonsActive:
                easyDiffButton.draw()
                normalDiffButton.draw()
                hardDiffButton.draw()
                extremeDiffButton.draw()
            if done:
                returnButton.draw()
        
        else:
            title.draw(screen)
            #playerSprite.draw(screen)
            if event.type == startUpTimer:
                if jeremy == 0:
                    jeremy = 1
                elif jeremy == 1:
                    title.add(menu())
                    jeremy = 2
       
       
        pygame.display.update() #updates game
        clock.tick(30) #the frame rate


if __name__ == "__main__":
    main()
