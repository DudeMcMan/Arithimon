import pygame
from sys import exit
from random import randint
from pygame import mixer

# for running python3 TheCode/arithimon.py
# assuming the directory is the same

class gameTitle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        gameTitle = pygame.image.load("Items/arithilogo.png").convert_alpha()
        gameTitle = pygame.transform.scale_by(gameTitle, (1/2, 1/2))
       
        self.image = gameTitle
        self.rect = self.image.get_rect(center=(410, 150))
       
class menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        gameMenu = pygame.image.load("Items/arithimon v2.png").convert_alpha()
        #gameMenu = pygame.transform.scale_by(gameMenu, (0.5, 0.5))
       
        self.image = gameMenu
        self.rect = self.image.get_rect(center=(675, 400))
   
class theABCD(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        teamLogo = pygame.image.load("Items/ABCD.png").convert_alpha()
        teamLogo = pygame.transform.scale_by(teamLogo, (1.05, 1.1))
       
        self.image = teamLogo
        self.rect = self.image.get_rect(center=(675, 450))
       
class battleScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        battleScreen1 = pygame.image.load("Items/battleScreen1.png").convert_alpha()
        battleScreen1 = pygame.transform.scale_by(battleScreen1, (1/2, 1/2))
       
        self.image = battleScreen1
        self.rect = self.image.get_rect(center=(675, 400))

class playerAppleKun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
       
        playerAppleKun = pygame.image.load("Items/Apple-kun.png").convert_alpha()
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

class Question:
    questionText = ""
    answer = 0
    def createEasy():
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
        temp = randint(1,4)
        other = randint(1, 3)
        order = randint(1, 4)
        #temp = 1
        if(temp==1):
            #+
            firstInt = randint(0,12)
            secondInt = randint(1,12)
            thirdInt = randint(1, 12)
            fourthInt = 0
            #Question.questionText = str(firstInt)+" + "+str(secondInt)+" = ?"
            #Question.answer = firstInt+secondInt
            if other == 1:
                #-
                if order % 2 == 0:
                    Question.questionText = str(firstInt)+" + "+str(secondInt)+" - " + str(thirdInt) + " = ?"
                    Question.answer = firstInt + secondInt - thirdInt
                else:
                    Question.questionText = str(firstInt)+" - "+str(secondInt)+" + " + str(thirdInt) + " = ?"
                    Question.answer = firstInt - secondInt + thirdInt
                    
            elif other == 2:
                #*
                if order % 2 == 0:
                    Question.questionText = str(firstInt)+" + "+str(secondInt)+" * " + str(thirdInt) + " = ?"
                    Question.answer = firstInt + secondInt * thirdInt
                else:
                    Question.questionText = str(firstInt)+" * "+str(secondInt)+" + " + str(thirdInt) + " = ?"
                    Question.answer = firstInt * secondInt + thirdInt
                    
            else:
                #/
                while thirdInt == 0:
                    thirdInt = randint(1, 12)
                if order == 1:
                    while(secondInt % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" + ("+str(secondInt)+" / " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt / thirdInt
                    Question.answer = int(firstInt + fourthInt)
                if order == 2:
                    while(firstInt % secondInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(1,12)
                        thirdInt = randint(0, 12)
                    Question.questionText = "(" + str(firstInt)+" / "+str(secondInt)+") + " + str(thirdInt) + " = ?"
                    fourthInt = firstInt / secondInt
                    Question.answer = int(fourthInt + thirdInt)
                if order == 3:
                    while((firstInt + secondInt) % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = "(" + str(firstInt)+" + "+str(secondInt)+") / " + str(thirdInt) + " = ?"
                    fourthInt = firstInt + secondInt
                    Question.answer = int(fourthInt / thirdInt)
                if order == 4:
                    while(firstInt % (secondInt + thirdInt)!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" / ("+str(secondInt)+" + " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt + thirdInt
                    Question.answer = int(firstInt / fourthInt)
            
        elif(temp==2):
            #-
            firstInt = randint(0,12)
            secondInt = randint(1,12)
            thirdInt = randint(1, 12)
            #Question.questionText = str(firstInt)+" + "+str(secondInt)+" = ?"
            #Question.answer = firstInt+secondInt
            if other == 1:
                #+
                if order % 2 == 0:
                    Question.questionText = str(firstInt)+" + "+str(secondInt)+" - " + str(thirdInt) + " = ?"
                    Question.answer = firstInt + secondInt - thirdInt
                else:
                    Question.questionText = str(firstInt)+" - "+str(secondInt)+" + " + str(thirdInt) + " = ?"
                    Question.answer = firstInt - secondInt + thirdInt
                    
            elif other == 2:
                #*
                if order % 2 == 0:
                    Question.questionText = str(firstInt)+" - "+str(secondInt)+" * " + str(thirdInt) + " = ?"
                    Question.answer = firstInt - secondInt * thirdInt
                else:
                    Question.questionText = str(firstInt)+" * "+str(secondInt)+" - " + str(thirdInt) + " = ?"
                    Question.answer = firstInt * secondInt - thirdInt
                    
            else:
                #/
                while thirdInt == 0:
                    thirdInt = randint(1, 12)
                if order == 1:
                    while(secondInt % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" - ("+str(secondInt)+" / " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt / thirdInt
                    Question.answer = int(firstInt - fourthInt)
                if order == 2:
                    while(firstInt % secondInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(1,12)
                        thirdInt = randint(0, 12)
                    Question.questionText = "(" + str(firstInt)+" / "+str(secondInt)+") - " + str(thirdInt) + " = ?"
                    fourthInt = firstInt / secondInt
                    Question.answer = int(fourthInt - thirdInt)
                if order == 3:
                    while((firstInt - secondInt) % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = "(" + str(firstInt)+" - "+str(secondInt)+") / " + str(thirdInt) + " = ?"
                    fourthInt = firstInt - secondInt
                    Question.answer = int(fourthInt / thirdInt)
                if order == 4:
                    while(firstInt % (secondInt - thirdInt)!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" / ("+str(secondInt)+" - " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt - thirdInt
                    Question.answer = int(firstInt / fourthInt)
            
        elif(temp==3):
            #*
            firstInt = randint(0,12)
            secondInt = randint(1,12)
            thirdInt = randint(1, 12)
            #Question.questionText = str(firstInt)+" + "+str(secondInt)+" = ?"
            #Question.answer = firstInt+secondInt
            if other == 1:
                #-
                if order % 2 == 0:
                    Question.questionText = str(firstInt)+" * "+str(secondInt)+" - " + str(thirdInt) + " = ?"
                    Question.answer = firstInt * secondInt - thirdInt
                else:
                    Question.questionText = str(firstInt)+" - "+str(secondInt)+" * " + str(thirdInt) + " = ?"
                    Question.answer = firstInt - secondInt * thirdInt
                    
            elif other == 2:
                #+
                if order % 2 == 0:
                    Question.questionText = str(firstInt)+" + "+str(secondInt)+" * " + str(thirdInt) + " = ?"
                    Question.answer = firstInt + secondInt * thirdInt
                else:
                    Question.questionText = str(firstInt)+" * "+str(secondInt)+" + " + str(thirdInt) + " = ?"
                    Question.answer = firstInt * secondInt + thirdInt
                    
            else:
                #/
                while thirdInt == 0:
                    thirdInt = randint(1, 12)
                if order == 1:
                    while(secondInt % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" * ("+str(secondInt)+" / " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt / thirdInt
                    Question.answer = int(firstInt * fourthInt)
                if order == 2:
                    while(firstInt % secondInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(1,12)
                        thirdInt = randint(0, 12)
                    Question.questionText = "(" + str(firstInt)+" / "+str(secondInt)+") * " + str(thirdInt) + " = ?"
                    fourthInt = firstInt / secondInt
                    Question.answer = int(fourthInt * thirdInt)
                if order == 3:
                    while((firstInt * secondInt) % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = "(" + str(firstInt)+" * "+str(secondInt)+") / " + str(thirdInt) + " = ?"
                    fourthInt = firstInt * secondInt
                    Question.answer = int(fourthInt / thirdInt)
                if order == 4:
                    while(firstInt % (secondInt * thirdInt)!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(1,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" / ("+str(secondInt)+" * " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt * thirdInt
                    Question.answer = int(firstInt / fourthInt)
            
        else:
            #/
            firstInt = randint(0,12)
            secondInt = randint(1,12)
            thirdInt = randint(1, 12)
            fourthInt = 0
            #Question.questionText = str(firstInt)+" + "+str(secondInt)+" = ?"
            #Question.answer = firstInt+secondInt
            if other == 1:
                #-
                while thirdInt == 0:
                    thirdInt = randint(1, 12)
                if order == 1:
                    while(secondInt % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" - ("+str(secondInt)+" / " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt / thirdInt
                    Question.answer = int(firstInt - fourthInt)
                if order == 2:
                    while(firstInt % secondInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(0, 12)
                    Question.questionText = "(" + str(firstInt)+" / "+str(secondInt)+") - " + str(thirdInt) + " = ?"
                    fourthInt = firstInt / secondInt
                    Question.answer = int(fourthInt - thirdInt)
                if order == 3:
                    while((firstInt - secondInt) % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = "(" + str(firstInt)+" - "+str(secondInt)+") / " + str(thirdInt) + " = ?"
                    fourthInt = firstInt - secondInt
                    Question.answer = int(fourthInt / thirdInt)
                if order == 4:
                    while(thirdInt == secondInt): #To make sure the number in the parenthesis isn't equal to 0
                        thirdInt = randint(0, 12)
                    while(firstInt % (secondInt - thirdInt)!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(0, 12)
                        while(thirdInt == secondInt):
                            thirdInt = randint(0, 12)
                    Question.questionText = str(firstInt)+" / ("+str(secondInt)+" - " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt - thirdInt
                    Question.answer = int(firstInt / fourthInt)
                    
            elif other == 2:
                #*
                while thirdInt == 0:
                    thirdInt = randint(1, 12)
                if order == 1:
                    while(secondInt % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" * ("+str(secondInt)+" / " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt / thirdInt
                    Question.answer = int(firstInt * fourthInt)
                if order == 2:
                    while(firstInt % secondInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(1,12)
                        thirdInt = randint(0, 12)
                    Question.questionText = "(" + str(firstInt)+" / "+str(secondInt)+") * " + str(thirdInt) + " = ?"
                    fourthInt = firstInt / secondInt
                    Question.answer = int(fourthInt * thirdInt)
                if order == 3:
                    while((firstInt * secondInt) % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = "(" + str(firstInt)+" * "+str(secondInt)+") / " + str(thirdInt) + " = ?"
                    fourthInt = firstInt * secondInt
                    Question.answer = int(fourthInt / thirdInt)
                if order == 4:
                    while(firstInt % (secondInt * thirdInt)!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(1,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" / ("+str(secondInt)+" * " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt * thirdInt
                    Question.answer = int(firstInt / fourthInt)
                    
            else:
                #+
                while thirdInt == 0:
                    thirdInt = randint(1, 12)
                if order == 1:
                    while(secondInt % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" + ("+str(secondInt)+" / " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt / thirdInt
                    Question.answer = int(firstInt + fourthInt)
                if order == 2:
                    while(firstInt % secondInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(1,12)
                        thirdInt = randint(0, 12)
                    Question.questionText = "(" + str(firstInt)+" / "+str(secondInt)+") + " + str(thirdInt) + " = ?"
                    fourthInt = firstInt / secondInt
                    Question.answer = int(fourthInt + thirdInt)
                if order == 3:
                    while((firstInt + secondInt) % thirdInt!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = "(" + str(firstInt)+" + "+str(secondInt)+") / " + str(thirdInt) + " = ?"
                    fourthInt = firstInt + secondInt
                    Question.answer = int(fourthInt / thirdInt)
                if order == 4:
                    while(firstInt % (secondInt + thirdInt)!=0):
                        firstInt = randint(0,12)
                        secondInt = randint(0,12)
                        thirdInt = randint(1, 12)
                    Question.questionText = str(firstInt)+" / ("+str(secondInt)+" + " + str(thirdInt) + ") = ?"
                    fourthInt = secondInt + thirdInt
                    Question.answer = int(firstInt / fourthInt)

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
   
    userText = "Input Here"
 
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
 
    textActive = False
   
    title = pygame.sprite.Group()#the title
    title.add(theABCD())
    
    playerSprite = pygame.sprite.Group()
    #playerSprite.add(playerBarry())
    
    enemySprite = pygame.sprite.Group()
    #enemySprite.add(enemyBarry())
   
    theFont = pygame.font.Font("Items/Pixeltype.ttf", 50) #The font, most likely temporary
   
    gameMessage = theFont.render("Press Enter To Start", False, "black") #how to start the game
    gameMessageRect = gameMessage.get_rect(center=(400, 450))
   
    secretMessage = theFont.render("Sick", False, "white") #for fun
    secretMessageRect = secretMessage.get_rect(center=(675, 400))
   
    answerMessage = theFont.render("Click To Answer (Or Press Enter)", False, "white") #temporary answer button
    answerMessageRect = answerMessage.get_rect(center=(675, 600))
   
    wrongMessage = theFont.render("Incorrect", False, "white") #temporary answer button
    wrongMessageRect = wrongMessage.get_rect(center=(675, 400))
   
   
    tempMessage = theFont.render("Select Your Difficulty (only easy and normal work)", False, "black") #temporary start game message
    tempMessageRect = tempMessage.get_rect(center=(675, 150))
   
    tempMessageDiffTwo = theFont.render("(1)Easy", False, "black") #temporary difficulty option
    tempMessageRectDiffTwo = tempMessageDiffTwo.get_rect(center=(675, 300))
    
    Question.createEasy() #Creates an initial easy question
    tempMessageEasy = theFont.render(Question.questionText, False, "white") #temporary message
    tempMessageRectEasy = tempMessageEasy.get_rect(center=(675, 150))
    
    Question.createNormal() #Creates an initial normal question
    tempMessageNormal = theFont.render(Question.questionText, False, "white") #temporary message
    tempMessageRectNormal = tempMessageNormal.get_rect(center=(675, 150))
    
    tempMessageTurn = theFont.render("Enemy Turn", False, "white") #temporary message
    tempMessageRectTurn = tempMessageTurn.get_rect(center=(675, 150))
    
    tempMessageWin = theFont.render("You Win", False, "white") #temporary message
    tempMessageRectWin = tempMessageWin.get_rect(center=(675, 150))
    
    tempMessageLose = theFont.render("You Lose", False, "white") #temporary message
    tempMessageRectLose = tempMessageLose.get_rect(center=(675, 150))
    
    messageBack = theFont.render("Return to Difficulty Selection", False, "white") #temporary message
    messageRectBack = messageBack.get_rect(center=(675, 500))
   
    tempMessageDiffThree = theFont.render("(2)Normal", False, "black") #temporary difficulty option
    tempMessageRectDiffThree = tempMessageDiffThree.get_rect(center=(675, 400))
   
    #tempMessageNormal = theFont.render("Normal Mode Selected", False, "white") #temporary message
    #tempMessageRectNormal = tempMessageNormal.get_rect(center=(675, 150))
   
    tempMessageDiffFour = theFont.render("(3)Hard", False, "black") #temporary difficulty option
    tempMessageRectDiffFour = tempMessageDiffFour.get_rect(center=(675, 500))
   
    tempMessageHard = theFont.render("Hard Mode Selected", False, "white") #temporary message
    tempMessageRectHard = tempMessageHard.get_rect(center=(675, 150))
   
    tempMessageDiffFive = theFont.render("(4)Extreme", False, "black") #temporary difficulty option
    tempMessageRectDiffFive = tempMessageDiffFive.get_rect(center=(675, 600))
   
    tempMessageExtreme = theFont.render("Extreme Mode Selected", False, "white") #temporary message
    tempMessageRectExtreme = tempMessageExtreme.get_rect(center=(675, 150))
   
   
    gameActive = False
    diffSelect = False
    diffEasy = False
    diffNormal = False
    diffHard = False
    diffExtreme = False
    answered = False
    playerTurn = True
   
    #timers
    startUpTimer = pygame.USEREVENT + 1
    pygame.time.set_timer(startUpTimer, 2000)

    #Starts menu music immediately
    mixer.init()
    mixer.music.load('Items/menuMusic.wav')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)
    while True:
        battleTimer = int(pygame.time.get_ticks() / 100) #Every tenth of a second is tracked
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #this will close the game
                pygame.quit()
                exit()
               
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                
                if messageRectBack.collidepoint(event.pos) and done:
                    diffSelect = True
                    win = False
                    done = False
                    diffEasy = False
                    diffNormal = False
                    diffHard = False
                    diffExtreme = False
                    answered = False
                    playerTurn = True
                    clickSound.play()
                    mixer.music.load('Items/menuMusic.wav')
                    mixer.music.set_volume(0.1)
                    mixer.music.play(-1)
                    pygame.sprite.Group.empty(playerSprite)
                    pygame.sprite.Group.empty(enemySprite)
                    beavis = 0
                    butthead = 0
                    break #So that clicking this does not immediately select hard mode
                
                if answerMessageRect.collidepoint(event.pos) and playerTurn:
                    if userText != "Input Here" and userText != "":
                        answered = True
               
                if inputRect.collidepoint(event.pos) and playerTurn:
                    textActive = True
                    userText = ""
                else:
                    textActive = False
           
            if textActive:
                if event.type == pygame.KEYDOWN:
                    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                        if textActive:
                            answered = True
 
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
 
                        # get text input from 0 to -1 i.e. end.
                        userText = userText[:-1]
                        
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        pass
                        #prevents enter from being typed
 
                    # Unicode standard is used for string
                    # formation
                    else:
                        userText += event.unicode
           
            if gameActive:
                if diffSelect:
                        
                    userText = "Input Here"
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
                    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_1 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_1 or event.type == pygame.MOUSEBUTTONUP and event.button == 1 and tempMessageRectDiffTwo.collidepoint(event.pos):
                        clickSound.play()
                        diffEasy = True
                        diffSelect = False
                        weezer = battleTimer
                        Question.createEasy()
                        tempMessageEasy = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                        mixer.music.stop()
                        mixer.music.load('Items/battleMusic.wav')
                        mixer.music.set_volume(0.2)
                        mixer.music.play(-1)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2 or event.type == pygame.MOUSEBUTTONUP and event.button == 1 and tempMessageRectDiffThree.collidepoint(event.pos):
                        clickSound.play()
                        diffNormal = True
                        diffSelect = False
                        Question.createNormal()
                        tempMessageNormal = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                        mixer.music.stop()
                        mixer.music.load('Items/battleMusic.wav')
                        mixer.music.set_volume(0.2)
                        mixer.music.play(-1)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_3 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_3 or event.type == pygame.MOUSEBUTTONUP and event.button == 1 and tempMessageRectDiffFour.collidepoint(event.pos):
                        clickSound.play()
                        diffHard = True
                        diffSelect = False
                        mixer.music.stop()
                        mixer.music.load('Items/battleMusic.wav')
                        mixer.music.set_volume(0.2)
                        mixer.music.play(-1)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_4 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_4 or event.type == pygame.MOUSEBUTTONUP and event.button == 1 and tempMessageRectDiffFive.collidepoint(event.pos):
                        clickSound.play()
                        diffExtreme = True
                        diffSelect = False
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
                   
        screen.fill("white") #fills the screen with a specific color
                   
        if gameActive:
            screen.blit(tempMessage, tempMessageRect)
            screen.blit(tempMessageDiffTwo, tempMessageRectDiffTwo)
            screen.blit(tempMessageDiffThree, tempMessageRectDiffThree)
            screen.blit(tempMessageDiffFour, tempMessageRectDiffFour)
            screen.blit(tempMessageDiffFive, tempMessageRectDiffFive)
            
            if diffEasy:
                if win and done: #Won
                    screen.fill("gray")
                    screen.blit(tempMessageWin, tempMessageRectWin)
                    
                    screen.blit(messageBack, messageRectBack)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)

                    #Question.createEasy()
                    #tempMessageEasy = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                    
                if win == False and done: #Lost
                    mixer.music.stop()
                    screen.fill("gray")
                    screen.blit(tempMessageLose, tempMessageRectLose)
                    
                    screen.blit(messageBack, messageRectBack)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)
                
                if playerTurn and done == False: #Player turn
                    
                    screen.fill("gray")
                    screen.blit(tempMessageEasy, tempMessageRectEasy)
                    pygame.draw.rect(screen, "red", answerMessageRect)
                    screen.blit(answerMessage, answerMessageRect)
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)
                
                    if textActive:
                        color = colorActive
                    else:
                        color = colorPassive
            
                    # draw rectangle and argument passed which should
                    # be on screen
                    pygame.draw.rect(screen, color, inputRect)
    
                    text_surface = theFont.render(userText, True, (255, 255, 255))
        
                    # render at position stated in arguments
                    screen.blit(text_surface, (inputRect.x+5, inputRect.y+5))
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
        
                    # set width of textfield so that text cannot get
                    # outside of user's text input
                    inputRect.w = max(100, text_surface.get_width()+10)
                    
                    if battleTimer - weezer <= 150: #Damage minimum of 50. Maximum time is 15 seconds
                        alvin = theodre - (battleTimer - weezer)
                
                    if answered:
                        if userText == str(Question.answer):
                            
                            if alvin < 0:
                                alvin = 0
                            
                            michael = michael - alvin
                            
                            if michael < 0:
                                michael = 0
                                
                            if michael == 0:
                                otherHealthRect.update(1000, 175, michael, 25)
                                win = True
                                done = True
                                correct = False
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
                                
                            else:
                                otherHealthRect.update(1000, 175, michael, 25)
                                screen.blit(secretMessage, secretMessageRect)
                                correct = True
                                answered = False
                                textActive = False
                                playerTurn = False
                                kat = False
                                carl = 0
                                weezer = battleTimer

                        else:
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
                    screen.fill("gray")
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
                        if randint(1, 50) == 1:
                            playerTurn = True
                            userText = "Input Here"
                            weezer = battleTimer
                            Question.createEasy()
                            tempMessageEasy = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                                
                        else:
                            simon = simon - randint(10, 150)
                            
                            if simon < 0:
                                simon = 0
                                
                            if simon == 0:
                                playerHealthRect.update(100, 500, simon, 25)
                                done = True
                                kat = False
                                carl = 0
                                weezer = 0
                            
                            else:
                                playerHealthRect.update(100, 500, simon, 25)
                                
                                playerTurn = True
                                userText = "Input Here"
                                weezer = battleTimer
                                Question.createEasy()
                                tempMessageEasy = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                        
               
            if diffNormal:
                if win and done: #Won
                    screen.fill("gray")
                    screen.blit(tempMessageWin, tempMessageRectWin)
                    
                    screen.blit(messageBack, messageRectBack)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)

                    #Question.createEasy()
                    #tempMessageEasy = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                    
                if win == False and done: #Lost
                    mixer.music.stop()
                    screen.fill("gray")
                    screen.blit(tempMessageLose, tempMessageRectLose)
                    
                    screen.blit(messageBack, messageRectBack)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)
                
                if playerTurn and done == False: #Player turn
                    
                    screen.fill("gray")
                    screen.blit(tempMessageNormal, tempMessageRectNormal)
                    pygame.draw.rect(screen, "red", answerMessageRect)
                    screen.blit(answerMessage, answerMessageRect)
                    playerSprite.draw(screen)
                    enemySprite.draw(screen)
                
                    if textActive:
                        color = colorActive
                    else:
                        color = colorPassive
            
                    # draw rectangle and argument passed which should
                    # be on screen
                    pygame.draw.rect(screen, color, inputRect)
    
                    text_surface = theFont.render(userText, True, (255, 255, 255))
        
                    # render at position stated in arguments
                    screen.blit(text_surface, (inputRect.x+5, inputRect.y+5))
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
        
                    # set width of textfield so that text cannot get
                    # outside of user's text input
                    inputRect.w = max(100, text_surface.get_width()+10)
                    
                    if battleTimer - weezer <= 150: #Damage minimum of 50. Maximum time is 15 seconds
                        alvin = theodre - (battleTimer - weezer)
                    #print(Question.answer)
                
                    if answered:
                        if userText == str(Question.answer):
                            
                            if alvin < 0:
                                alvin = 0
                            
                            michael = michael - alvin
                            
                            if michael < 0:
                                michael = 0
                                
                            if michael == 0:
                                otherHealthRect.update(1000, 175, michael, 25)
                                win = True
                                done = True
                                correct = False
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
                            else:
                                otherHealthRect.update(1000, 175, michael, 25)
                                screen.blit(secretMessage, secretMessageRect)
                                correct = True
                                answered = False
                                textActive = False
                                playerTurn = False
                                kat = False
                                carl = 0
                                weezer = battleTimer

                        else:
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
                    screen.fill("gray")
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
                        if randint(1, 50) == 1:
                            playerTurn = True
                            userText = "Input Here"
                            weezer = battleTimer
                            Question.createNormal()
                            tempMessageNormal = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
                                
                        else:
                            simon = simon - randint(10, 150)
                            
                            if simon < 0:
                                simon = 0
                                
                            if simon == 0:
                                playerHealthRect.update(100, 500, simon, 25)
                                done = True
                                kat = False
                                carl = 0
                                weezer = 0
                            
                            else:
                                playerHealthRect.update(100, 500, simon, 25)
                                
                                playerTurn = True
                                userText = "Input Here"
                                weezer = battleTimer
                                Question.createNormal()
                                tempMessageNormal = theFont.render(Question.questionText, False, "white") #Replaces the message with new question
            if diffHard:
                screen.fill("black")
                done = True
                screen.blit(tempMessageHard, tempMessageRectHard)
                screen.blit(messageBack, messageRectBack)
            if diffExtreme:
                screen.fill("black")
                done = True
                screen.blit(tempMessageExtreme, tempMessageRectExtreme)
                screen.blit(messageBack, messageRectBack)
       
        else:
            title.draw(screen)
            #playerSprite.draw(screen)
            if event.type == startUpTimer:
                if jeremy == 0:
                    jeremy = 1
                else:
                    title.add(menu())
       
       
        pygame.display.update() #updates game
        clock.tick(30) #the frame rate




if __name__ == "__main__":
    main()
