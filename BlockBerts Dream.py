#----Imports-------------------------------------------------------------------
#--------External Code--------
import random
import pygame
pygame.init()

#----Class---------------------------------------------------------------------
class Window():
    def __init__(self):
        self.X = 1280
        self.Y = 720
        self.surface = pygame.display.set_mode((self.X,self.Y))
        pygame.display.set_caption("Block Berts Dream")

class Entities():
    def __init__(self,X = 0,Y = 0):
        self.X = X
        self.Y = Y
        self.direction = "Left"
        
class BlockBert(Entities):
    def __init__(self,X = 0, Y = 0):
        Entities.__init__(self,X,Y)
        self.pos = 10
        self.coins = 0
        
    def Graphics(self):
        #--------Colors--------
        outLine = (0,0,0)
        skin = (250,250,210)
        hair = (253,255,24)
        eyes = (82,145,255)
        shirt = (161,64,43)
        underShirt = (255,255,255)
        shoes = (0,0,0)
        
        if blockBert.direction == "Left":
        #------------Head------------
            pygame.draw.rect(window.surface,skin,pygame.Rect(self.X + 15,self.Y + 4,20,20),10)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 15,self.Y + 4,20,20),1)
            pygame.draw.line(window.surface,hair,(self.X + 19,self.Y),(self.X + 25,self.Y + 4),1)
            pygame.draw.line(window.surface,hair,(self.X + 25,self.Y),(self.X + 25,self.Y + 4),1)
            pygame.draw.line(window.surface,hair,(self.X + 31,self.Y),(self.X + 25,self.Y + 4),1)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 15,self.Y + 4,20,20),1)
            pygame.draw.line(window.surface,eyes,(self.X + 19,self.Y + 7),(self.X + 19,self.Y + 9),2)
            pygame.draw.line(window.surface,outLine,(self.X + 17,self.Y + 18),(self.X + 20,self.Y + 18),1)
            pygame.draw.line(window.surface,outLine,(self.X + 20,self.Y + 18),(self.X + 23,self.Y + 16),1)
            
        #------------Body------------
            pygame.draw.rect(window.surface,shirt,pygame.Rect(self.X + 10,self.Y + 24,30,30),15)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 10,self.Y + 24,30,30),1)
            pygame.draw.rect(window.surface,underShirt,pygame.Rect(self.X + 10,self.Y + 24,10,12),5)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 10,self.Y + 24,12,12),1)
            pygame.draw.polygon(window.surface,outLine,((self.X + 10,self.Y + 36),(self.X + 20,self.Y + 36),(self.X + 10,self.Y + 41)),1)
            pygame.draw.polygon(window.surface,underShirt,((self.X + 12,self.Y + 35),(self.X + 18,self.Y + 35),(self.X + 12,self.Y + 40)),4)
            pygame.draw.rect(window.surface,skin,pygame.Rect(self.X + 25,self.Y + 27,4,14),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 25,self.Y + 27,4,14),1)
            pygame.draw.line(window.surface,outLine,(self.X + 22,self.Y + 45),(self.X + 25,self.Y + 41),4)
            pygame.draw.line(window.surface,skin,(self.X + 22,self.Y + 45),(self.X + 25,self.Y + 40),2)
            pygame.draw.rect(window.surface,skin,pygame.Rect(self.X + 17,self.Y + 54,4,10),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 17,self.Y + 54,4,10),1)
            pygame.draw.rect(window.surface,skin,pygame.Rect(self.X + 27,self.Y + 54,4,10),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 27,self.Y + 54,4,10),1)
            pygame.draw.rect(window.surface,shoes,pygame.Rect(self.X + 13,self.Y + 62,4,2),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 13,self.Y + 62,4,2),1)
            pygame.draw.rect(window.surface,shoes,pygame.Rect(self.X + 23,self.Y + 62,4,2),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(self.X + 23,self.Y + 62,4,2),1)
            
        if blockBert.direction == "Right":
        #------------Head------------
            pygame.draw.rect(window.surface,skin,pygame.Rect(blockBert.X + 29,blockBert.Y + 4,20,20),10)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 29,blockBert.Y + 4,20,20),1)
            pygame.draw.line(window.surface,hair,(blockBert.X + 45,blockBert.Y),(blockBert.X + 45,blockBert.Y + 4),1)
            pygame.draw.line(window.surface,hair,(blockBert.X + 39,blockBert.Y),(blockBert.X + 39,blockBert.Y + 4),1)
            pygame.draw.line(window.surface,hair,(blockBert.X + 33,blockBert.Y),(blockBert.X + 39,blockBert.Y + 4),1)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 29,blockBert.Y + 4,20,20),1)
            pygame.draw.line(window.surface,eyes,(blockBert.X + 45,blockBert.Y + 7),(blockBert.X + 45,blockBert.Y + 9),2)
            pygame.draw.line(window.surface,outLine,(blockBert.X + 47,blockBert.Y + 18),(blockBert.X + 44,blockBert.Y + 18),1)
            pygame.draw.line(window.surface,outLine,(blockBert.X + 44,blockBert.Y + 18),(blockBert.X + 41,blockBert.Y + 16),1)
            
        #------------Body------------
            pygame.draw.rect(window.surface,shirt,pygame.Rect(blockBert.X + 24,blockBert.Y + 24,30,30),15)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 24,blockBert.Y + 24,30,30),1)
            pygame.draw.rect(window.surface,underShirt,pygame.Rect(blockBert.X + 44,blockBert.Y + 24,10,12),5)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 44,blockBert.Y + 24,10,12),1)
            pygame.draw.polygon(window.surface,outLine,((blockBert.X + 44,blockBert.Y + 36),(blockBert.X + 53,blockBert.Y + 36),(blockBert.X + 53,blockBert.Y + 43)),1)
            pygame.draw.polygon(window.surface,underShirt,((blockBert.X + 45,blockBert.Y + 35),(blockBert.X + 50,blockBert.Y + 35),(blockBert.X + 50,blockBert.Y + 42)),4)
            pygame.draw.rect(window.surface,skin,pygame.Rect(blockBert.X + 35,blockBert.Y + 27,4,14),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 35,blockBert.Y + 27,4,14),1)
            pygame.draw.line(window.surface,outLine,(blockBert.X + 38,blockBert.Y + 41),(blockBert.X + 41,blockBert.Y + 44),4)
            pygame.draw.line(window.surface,skin,(blockBert.X + 38,blockBert.Y + 41),(blockBert.X + 41,blockBert.Y + 44),2)
            pygame.draw.rect(window.surface,skin,pygame.Rect(blockBert.X + 43,blockBert.Y + 54,4,10),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 43,blockBert.Y + 54,4,10),1)
            pygame.draw.rect(window.surface,skin,pygame.Rect(blockBert.X + 33,blockBert.Y + 54,4,10),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 33,blockBert.Y + 54,4,10),1)
            pygame.draw.rect(window.surface,shoes,pygame.Rect(blockBert.X + 47,blockBert.Y + 62,4,2),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 47,blockBert.Y + 62,4,2),1)
            pygame.draw.rect(window.surface,shoes,pygame.Rect(blockBert.X + 37,blockBert.Y + 62,4,2),3)
            pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 37,blockBert.Y + 62,4,2),1)
        
    def Move(self,chapter,direction,enviornment):
        self.direction = direction
        if chapter == 1:
            ground = False
            if direction == "Left":
                for a in enviornment:
                    if a.Y == self.Y:
                        ground = True
                        #----Move to open space----
                        if a.state[self.pos - 1] == 0:
                            self.X -= 64
                            self.pos -= 1
                        if a.state[self.pos - 1] == 3:
                            a.state[self.pos - 1] = 0
                            self.coins += 1
                            self.X -= 64
                            self.pos -= 1
                        #----Break Block in way----    
                        elif a.state[self.pos - 1] == 1:
                            a.state[self.pos - 1] = 0
                #----Move if not in ground----            
                if ground == False:
                    self.X -= 64
                    self.pos -= 1 
                    #----Boundaries----    
                if self.X < 0:
                    self.X = 0
                    self.pos = 0
                        
            if direction == "Right":
                for a in enviornment:
                    if a.Y == self.Y:
                        ground = True
                        #----Move to open space----
                        if a.state[self.pos + 1] == 0:
                            self.X += 64
                            self.pos += 1
                        if a.state[self.pos + 1] == 3:
                            a.state[self.pos + 1] = 0
                            self.coins += 1
                            self.X += 64
                            self.pos += 1
                        #----Break Block in way----    
                        elif a.state[self.pos + 1] == 1:
                            a.state[self.pos + 1] = 0
                    #----Move if not in ground----            
                if ground == False:
                    self.X += 64
                    self.pos += 1 
                #----Boundaries----    
                if self.X > 1216:
                    self.X = 1216
                    self.pos = 20
            
    def Break(self,enviornment):
        for a in enviornment:
            if a.Y == self.Y + 64:
                if a.state[self.pos] == 1:
                    a.state[self.pos] = 0

class Sun(Entities):
    def __init__(self,X = 0, Y = 0):
        Entities.__init__(self,X,Y)
        
    def Graphics(self):
        #--------Colors--------
        sunIn = (249,215,28)
        sunOut = (255,210,28)

        #----Sun----
        pygame.draw.circle(window.surface,sunIn,(self.X,self.Y),window.X,500)
        pygame.draw.circle(window.surface,sunOut,(self.X,self.Y),window.X,40)

class Layer():
    def __init__(self,Y,enviornment):
        self.X = -64
        self.Y = Y
        self.state = []
        a = 0
        while a < 20:
            a += 1
            b = random.randint(0,100)
            #----Create Unbreakable Block----
            if b >= 90:
                self.state.append(2)
            #----Create Hole----
            elif b >= 70 and b < 90:
                b = random.randint(0,100)
                if b < 10:
                    self.state.append(3)
                else:
                    self.state.append(0)
            #----Create Breakable Block----
            else:
                self.state.append(1)
        #----Create Edge----
        self.state[0] = 2
        self.state[-1] = 2
        
        #----Add Layer to Enviornment----
        enviornment.append(self)
        
    def EnviornmentCleanUp(enviornment):
        #----Remove Un-Needed Layers from Memory----
        for a in enviornment:
            if a.Y < -64:
                enviornment.remove(a)

#----Def-----------------------------------------------------------------------
def GameOver(score):
    #----Move BlockBert----
    blockBert.X = 640
   
    #----Colors----
    outLine = (0,0,0)
    blanket = (150,100,100)
    desk = (81,59,48)
    bowl = (246,254,255)
    carpetOut = (4,2,115)
    carpetIn = (8,4,240)
    fish = (255,153,19)
    
    
    run = True
    #----BackGround----
    window.surface.fill((255,255,255))
    #----Game Over Score Display----
    text = font.render(str(score),True,(0,0,0))
    textA = font.render("You made it to depth:",True,(0,0,0))
    #----Draw Text----
    window.surface.blit(text,(blockBert.X,blockBert.Y - 60))
    window.surface.blit(textA,(blockBert.X - 100,blockBert.Y - 120))
    #----Coins Count for Something----
    #----Carpet----
    if blockBert.coins > 6:
        #----Carpet----
        pygame.draw.circle(window.surface,carpetOut,(blockBert.X + 32,blockBert.Y + 60),54,54,0,0,1,1)
        pygame.draw.circle(window.surface,carpetIn,(blockBert.X + 32,blockBert.Y + 60),32,12,0,0,1,1)
        pygame.draw.circle(window.surface,outLine,(blockBert.X + 32,blockBert.Y + 60),54,1,0,0,1,1)
    
    #----Bed----
    pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 10,blockBert.Y - 10,85,85),1)
    pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 3,blockBert.Y - 3,67,30),1)
    #----Block Bert----
    BlockBert.Graphics(blockBert)
    #----Bed Cover----
    pygame.draw.rect(window.surface,blanket,pygame.Rect(blockBert.X - 10,blockBert.Y + 30,85,45),23)
    
    #----Coins Count for Something----
    if blockBert.coins > 10:
        #----Fish Bowl----
        pygame.draw.circle(window.surface,bowl,(blockBert.X - 34,blockBert.Y - 2),15,15)
        pygame.draw.circle(window.surface,outLine,(blockBert.X - 34,blockBert.Y - 2),15,1)
        
    if blockBert.coins > 3:
        #----Desk----
        pygame.draw.rect(window.surface,desk,pygame.Rect(blockBert.X - 50,blockBert.Y + 10,35,10),5)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 50,blockBert.Y + 10,35,10),1)
        pygame.draw.rect(window.surface,desk,pygame.Rect(blockBert.X - 48,blockBert.Y + 20,31,30),15)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 48,blockBert.Y + 20,31,30),1)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 46,blockBert.Y + 22,27,10),1)
        pygame.draw.circle(window.surface,outLine,(blockBert.X - 33,blockBert.Y + 27),3,1)
        
    if blockBert.coins > 15:
        #----Fish----
        pygame.draw.circle(window.surface,fish,(blockBert.X - 36,blockBert.Y),5,5)
        pygame.draw.circle(window.surface,fish,(blockBert.X - 32,blockBert.Y - 2),5,5,0,0,1,1)
        pygame.draw.circle(window.surface,fish,(blockBert.X - 32,blockBert.Y + 2),5,5,1,1,0,0)
        pygame.draw.line(window.surface,(0,0,0),(blockBert.X - 38,blockBert.Y - 2),(blockBert.X - 38,blockBert.Y - 1),1)

        
    pygame.display.update()
   #----Exit When Ready---- 
    while run == True:
        for i in pygame.event.get():
            #----Window is Force Closed----
            if i.type == pygame.QUIT:
                run = False
                pygame.quit()
        
            if i.type == pygame.KEYDOWN:
            #----Exit Game---
                if i.key == pygame.K_RETURN:
                    run = False
                    pygame.quit()
    
def Intro(backGround,sequence):
    #----Initialize----
    #----Colors----
    outLine = (0,0,0)
    blanket = (150,100,100)
    car = (180,180,220)
    
    #----Back Ground----
    window.surface.fill(backGround)
    #----Sequence A----
    if sequence == 0:
        #----Text----
        text = font.render("My Name is Block Bert. This is my life",True,outLine)
        #----Block Bert----
        BlockBert.Graphics(blockBert)
        #----Draw Text----
        window.surface.blit(text,(blockBert.X - 200,blockBert.Y - 64))
        pygame.display.update()
        pygame.time.wait(5000)
        text = font.render("",True,outLine)

    if sequence == 1:
        #----Text----
        text = font.render("EAT",True,outLine)
        #----Table----
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 100,blockBert.Y + 32,95,10),1)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 100,blockBert.Y + 42,5,34),1)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 10,blockBert.Y + 42,5,34),1)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 90,blockBert.Y + 42,5,30),1)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 20,blockBert.Y + 42,5,30),1)
        #----Block Bert----
        BlockBert.Graphics(blockBert)
    #----Sequence B----
    if sequence == 2:
        #----Text----
        text = font.render("SLEEP",True,outLine)
        #----Bed----
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 10,blockBert.Y -10,85,85),1)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 3,blockBert.Y - 3,67,30),1)
        #----Block Bert----
        BlockBert.Graphics(blockBert)
        #----Bed Cover----
        pygame.draw.rect(window.surface,blanket,pygame.Rect(blockBert.X - 10,blockBert.Y + 30,85,45),23)
    #----Sequence C----
    if sequence == 3:
        #----Text----
        text = font.render("GO TO WORK",True,outLine)
        #----Car----
        pygame.draw.rect(window.surface,car,pygame.Rect(blockBert.X - 10,blockBert.Y - 10,100,75),50)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 10,blockBert.Y -10,100,75),1)
        pygame.draw.rect(window.surface,car,pygame.Rect(blockBert.X - 70,blockBert.Y + 30,60,35),18)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 70,blockBert.Y + 30,60,35),1)
        pygame.draw.rect(window.surface,car,pygame.Rect(blockBert.X + 90,blockBert.Y + 30,40,35),18)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X + 90,blockBert.Y + 30,40,35),1)
        pygame.draw.rect(window.surface,backGround,pygame.Rect(blockBert.X - 5,blockBert.Y -5,60,35),30)
        #----Block Bert----
        BlockBert.Graphics(blockBert)
        #----Car----
        pygame.draw.rect(window.surface,car,pygame.Rect(blockBert.X - 9,blockBert.Y + 30,98,34),20)
        pygame.draw.rect(window.surface,outLine,pygame.Rect(blockBert.X - 5,blockBert.Y -5,60,35),1)
        pygame.draw.circle(window.surface,outLine,(blockBert.X - 10,blockBert.Y + 65),20,20)
        pygame.draw.circle(window.surface,outLine,(blockBert.X + 90,blockBert.Y + 65),20,20)

        
    #----Draw Text----
    window.surface.blit(text,(blockBert.X - 30,blockBert.Y - 64))

def ChapterOne(backGround):
    #----Back Ground----
    window.surface.fill(backGround)
    
    #----Draw World----
    for a in enviornment:
        #----Colors----
        outLine = (0,0,0)
        drkGry = (50,50,50)
        lgtGry = (200,200,200)
        coinOut = (197,179,88)
        coinIn = (212,175,55)
        Y = a.Y
        X = a.X
        for b in a.state:
            X += 64
            if b == 1:
                pygame.draw.rect(window.surface,lgtGry,pygame.Rect(X,Y,64,64),32)
                pygame.draw.rect(window.surface,drkGry,pygame.Rect(X + 4,Y + 4,12,12),6)
                pygame.draw.rect(window.surface,drkGry,pygame.Rect(X + 40,Y + 20,8,8),4)
                pygame.draw.rect(window.surface,drkGry,pygame.Rect(X + 24,Y + 40,16,16),8)
                pygame.draw.rect(window.surface,outLine,pygame.Rect(X,Y,64,64),1)
            if b == 2:
                pygame.draw.rect(window.surface,drkGry,pygame.Rect(X,Y,64,64),32)
                pygame.draw.rect(window.surface,lgtGry,pygame.Rect(X + 4,Y + 4,12,12),6)
                pygame.draw.rect(window.surface,lgtGry,pygame.Rect(X + 40,Y + 20,8,8),4)
                pygame.draw.rect(window.surface,lgtGry,pygame.Rect(X + 24,Y + 40,16,16),8)
                pygame.draw.rect(window.surface,outLine,pygame.Rect(X,Y,64,64),1)
            if b == 3:
                pygame.draw.circle(window.surface,coinOut,(X + 32,Y + 32),24,24)
                pygame.draw.circle(window.surface,coinIn,(X + 32,Y + 32),12,12)
                pygame.draw.circle(window.surface,outLine,(X + 32,Y + 32),1,1)
    
    #----Block Bert----
    BlockBert.Graphics(blockBert)

    #----Sun----
    Sun.Graphics(sun)
    
#----Main----------------------------------------------------------------------
#--------Initialize--------
window = Window()
bgA = 255
backGround = (bgA,bgA,bgA)
font = pygame.font.Font('freesansbold.ttf', 32)
chapter = 0
sequence = 0
time = 600
score = 0
enviornment = []
Y = 384
count = 0
while count < 5:
    Layer(Y,enviornment)
    Y += 64
    count += 1
blockBert = BlockBert(640,320)
sun = Sun(window.X/2,0 - window.X)

#--------Initial Conditions--------
run = True
#----Loop----------------------------------------------------------------------
while run == True:
    #----Event Management----
    for i in pygame.event.get():
        #----Window is Force Closed----
        if i.type == pygame.QUIT:
            run = False
        
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                direction = "Left"
                blockBert.Move(chapter,direction,enviornment)
            if i.key == pygame.K_RIGHT:
                direction = "Right"
                blockBert.Move(chapter,direction,enviornment)
             #----Break Blocks----   
            if i.key == pygame.K_DOWN:
                if chapter == 1:
                    blockBert.Break(enviornment)
        
    #------------Falling------------
        if chapter == 1:
            for a in enviornment:
                if a.Y == blockBert.Y + 64:
                    if a.state[blockBert.pos] == 0:
                        score += 1
                        sun.Y -= 64
                        for a in enviornment:
                            a.Y -= 64
                    if a.state[blockBert.pos] == 3:
                        score += 1
                        sun.Y -= 64
                        blockBert.coins += 1
                        a.state[blockBert.pos] = 0
                        for a in enviornment:
                            a.Y -= 64
    #----Graphics----
    #--------Background----
    if chapter == 0:
        Intro(backGround,sequence)
        pygame.time.wait(time)
        if sequence == 3:
            sequence = 1
        else:
            sequence += 1
        if time <= 10:
            chapter = 1
            bgA = 255
            backGround = (bgA,bgA,bgA)
        else:
            time -= 20
            bgA -= 5
            backGround = (bgA,bgA,bgA)
            
    if chapter == 1:
        #----Sun Movement----
        speed = 1 + (.5 * (score // 10))
        if score < 126:
            bgA = 255 - score * 2
        else:
            bgA = 0
        backGround = (bgA,bgA,bgA)
            
        if sun.Y + window.X >= blockBert.Y + 16:
            GameOver(score)
        elif sun.Y < blockBert.Y:
            sun.Y += speed

        if enviornment[-1].Y < 704:
            Y = enviornment[-1].Y + 64
            Layer(Y,enviornment)
            Layer.EnviornmentCleanUp(enviornment)
        ChapterOne(backGround)
            
    #----FINAL LOOP COMMAND 100% REQUIRED----
    pygame.display.update()

#----Game Over----
GameOver(score)
pygame.quit()