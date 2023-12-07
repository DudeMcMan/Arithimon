import pygame
from sys import exit
from random import randint

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
   
def main():
    pygame.init()
    pygame.display.set_caption('Arithimon') #window name
    #pygame.display.set_icon() #window icon
    screenWidth = 1350 #the width
    screenHeight = 800 #the height
    screen = pygame.display.set_mode((screenWidth, screenHeight)) #the display
   
    clock = pygame.time.Clock() #needed for frame rate
   
    jeremy = 0 # this is for the start up screen, so it can changeS
    michael = 200 # to make te health bar go down
    battleTimer = 0 #deducts from base
    alvin = 0 #damage deduction
    simon = 200 #to make health bar go down 
    theodre = 200 #damage deduction base
    ash = 0 #time stayed on enemy turn
    kat = False #to help change screen
    beavis = 0
    butthead = False
    correct = False #tells if answer is correct
    carl = 0
    weezer = 0
    win = False
    done = False
   
    userText = "Input Here"
 
    # text rect
    inputRect = pygame.Rect(200, 200, 140, 32)
    playerHealthRect = pygame.Rect(100, 500, michael, 25)
    playerDamageRect = pygame.Rect(100, 500, 200, 25)
    otherHealthRect = pygame.Rect(1000, 175, michael, 25)
    otherDamageRect = pygame.Rect(1000, 175, 200, 25)
   
    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
 
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
 
    textActive = False
   
    title = pygame.sprite.Group()#the title
    title.add(theABCD())
   
    theFont = pygame.font.Font("Items/Pixeltype.ttf", 50) #The font, most likely temperary
   
    gameMessage = theFont.render("Press Enter To Start", False, "black") #how to start the game
    gameMessageRect = gameMessage.get_rect(center=(400, 450))
   
    secretMessage = theFont.render("Sick", False, "white") #for fun
    secretMessageRect = secretMessage.get_rect(center=(675, 400))
   
    answerMessage = theFont.render("Click To Answer (Or Press Enter)", False, "white") #temperary answer button
    answerMessageRect = answerMessage.get_rect(center=(675, 600))
   
    wrongMessage = theFont.render("Incorrect", False, "white") #temperary answer button
    wrongMessageRect = wrongMessage.get_rect(center=(675, 400))
   
   
    tempMessage = theFont.render("Select Your Difficulty (only easy works)", False, "black") #temperary start game message
    tempMessageRect = tempMessage.get_rect(center=(675, 150))
   
    tempMessageDiffTwo = theFont.render("(1)Easy", False, "black") #temperary difficulty option
    tempMessageRectDiffTwo = tempMessageDiffTwo.get_rect(center=(675, 300))
   
    tempMessageEasy = theFont.render("What's 2 + 2?", False, "white") #temperary message
    tempMessageRectEasy = tempMessageEasy.get_rect(center=(675, 150))
    
    tempMessageTurn = theFont.render("Enemy Turn", False, "white") #temperary message
    tempMessageRectTurn = tempMessageTurn.get_rect(center=(675, 150))
    
    tempMessageWin = theFont.render("You Win", False, "white") #temperary message
    tempMessageRectWin = tempMessageWin.get_rect(center=(675, 150))
    
    tempMessageLose = theFont.render("You Lose", False, "white") #temperary message
    tempMessageRectLose = tempMessageLose.get_rect(center=(675, 150))
   
    tempMessageDiffThree = theFont.render("(2)Normal", False, "black") #temperary difficulty option
    tempMessageRectDiffThree = tempMessageDiffThree.get_rect(center=(675, 400))
   
    tempMessageNormal = theFont.render("Normal Mode Selected", False, "white") #temperary message
    tempMessageRectNormal = tempMessageNormal.get_rect(center=(675, 150))
   
    tempMessageDiffFour = theFont.render("(3)Hard", False, "black") #temperary difficulty option
    tempMessageRectDiffFour = tempMessageDiffFour.get_rect(center=(675, 500))
   
    tempMessageHard = theFont.render("Hard Mode Selected", False, "white") #temperary message
    tempMessageRectHard = tempMessageHard.get_rect(center=(675, 150))
   
    tempMessageDiffFive = theFont.render("(4)Extreme", False, "black") #temperary difficulty option
    tempMessageRectDiffFive = tempMessageDiffFive.get_rect(center=(675, 600))
   
    tempMessageExtreme = theFont.render("Extreme Mode Selected", False, "white") #temperary message
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
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #this will close the game
                pygame.quit()
                exit()
               
            if event.type == pygame.MOUSEBUTTONDOWN:
                if answerMessageRect.collidepoint(event.pos):
                    if textActive:
                        answered = True
               
                if inputRect.collidepoint(event.pos):
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
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_1 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_1:
                        diffEasy = True
                        diffSelect = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_2 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2:
                        diffNormal = True
                        diffSelect = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_3 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_3:
                        diffHard = True
                        diffSelect = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_4 or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_4:
                        diffExtreme = True
                        diffSelect = False
            else:
                #How to start the game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
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
                if win and done:
                    screen.fill("black")
                    screen.blit(tempMessageWin, tempMessageRectWin)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                if win == False and done:
                    screen.fill("black")
                    screen.blit(tempMessageLose, tempMessageRectLose)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                
                if playerTurn and done == False:
                    battleTimer = int(pygame.time.get_ticks() / 100)
                    screen.fill("black")
                    screen.blit(tempMessageEasy, tempMessageRectEasy)
                    pygame.draw.rect(screen, "red", answerMessageRect)
                    screen.blit(answerMessage, answerMessageRect)
                
                    if textActive:
                        color = color_active
                    else:
                        color = color_passive
            
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
                    
                    if battleTimer - weezer <= 150:
                        alvin = theodre - (battleTimer - weezer)
                
                    if answered:
                        if userText == "4":
                            
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
                            
                elif playerTurn == False and done == False:
                    
                    ash = int(pygame.time.get_ticks() / 100)
                    screen.fill("black")
                    screen.blit(tempMessageTurn, tempMessageRectTurn)
                    
                    if correct == False:
                        screen.blit(wrongMessage, wrongMessageRect)
                    else:
                        screen.blit(secretMessage, secretMessageRect)
                    
                    pygame.draw.rect(screen, "red", playerDamageRect)
                    pygame.draw.rect(screen, "green", playerHealthRect)
                    
                    pygame.draw.rect(screen, "red", otherDamageRect)
                    pygame.draw.rect(screen, "green", otherHealthRect)
                    
                    if ash % 2 == 0:
                        carl += 1
                        
                    if carl == 10:
                        kat = True
                    
                    if kat:
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
                        
               
            if diffNormal:
                screen.fill("black")
                screen.blit(tempMessageNormal, tempMessageRectNormal)
            if diffHard:
                screen.fill("black")
                screen.blit(tempMessageHard, tempMessageRectHard)
            if diffExtreme:
                screen.fill("black")
                screen.blit(tempMessageExtreme, tempMessageRectExtreme)
       
        else:
            title.draw(screen)
            if event.type == startUpTimer:
                if jeremy == 0:
                    jeremy = 1
                else:
                    title.add(menu())
       
       
        pygame.display.update() #updates game
        clock.tick(30) #the frame rate




if __name__ == "__main__":
    main()
