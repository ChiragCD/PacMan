import pygame,random,time
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

screen=pygame.display.set_mode((602,626))
clock=pygame.time.Clock()
pygame.display.set_caption("PACMAN")
ch=int(input("Enter map of choice: 1 or 2: "))
back=pygame.image.load(str(ch)+".png")
ch = int(input("Enter no. of ghosts : 1 to 8: "))
back=back.convert()
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Use arrow keys to move.",True,(0,255,255)),(25,50))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Blue dots enable you to send ghosts back to the centre.",True,(0,255,255)),(25,66))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("These are powerups lasting 10 seconds.",True,(0,255,255)),(25,82))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("A timer at the bottom of the screen indicates remaining powerup time.",True,(0,255,255)),(25,98))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Ghosts are sent to the centre, not removed from the game.",True,(0,255,255)),(25,114))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Objective is to eat all dots, including blue ones.",True,(0,255,255)),(25,130))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Game ends as soon as this is done.",True,(0,255,255)),(25,146))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("YOU ARE THE YELLOW CIRCLE.",True,(0,255,255)),(25,162))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Scoring system:",True,(0,255,255)),(25,194))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Normal dot: 10 pts ; Blue dot: 500 pts ; Ghost eaten: 500 pts.",True,(0,255,255)),(25,210))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("1 second played: -10 pts, so try to finish as fast as you can.",True,(0,255,255)),(25,226))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("You need not hold the key to continue motion.",True,(0,255,255)),(25,258))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("A key can be pressed before a turn, and the turn is made when possible.",True,(0,255,255)),(25,274))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("For a better challenge or higher score, try with 8 ghosts.",True,(0,255,255)),(25,306))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Be warned, the 8th ghost is black-coloured :)",True,(0,255,255)),(25,322))
screen.blit(pygame.font.SysFont("comicsansms", 16).render("Press any key to continue.",True,(0,255,255)),(25,354))
pygame.display.update()
t=True
while t==True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            t=False
screen.blit(back,(0,0))
pacdotlist=[(x,y)for x in range(13,590,24) for y in range(13,590,24)]
for i in pacdotlist[:]:
    if screen.get_at(i)!=((4,4,4)):
        pacdotlist.remove(i)
bigpacdotlist=[(13,13),(13,589),(589,13),(589,589)]
for i in pacdotlist:
    pygame.draw.circle(screen,(255,255,255),i,2)
c1=pygame.mixer.find_channel(False)
c2=pygame.mixer.find_channel(False)
backsound=pygame.mixer.Sound("Star Wars - Imperial March.mp3")
back2=pygame.mixer.Sound("back2.wav")
laser=pygame.mixer.Sound("LASER.WAV")
hammer=pygame.mixer.Sound("HAMMER.WAV")                            
# WindowsHardwareFail=pygame.mixer.Sound("Hardware_Fail.wav")
windowsding=pygame.mixer.Sound("Ding.wav")
pygame.mixer.Sound.set_volume(backsound,0.25)
pygame.mixer.Sound.set_volume(back2,0.25)
pygame.mixer.Sound.set_volume(laser,0.25)
pygame.mixer.Sound.set_volume(windowsding,0.25)
pygame.mixer.Sound.set_volume(hammer,0.25)
pygame.mixer.Sound.set_volume(windowsding,0.25)
Text=pygame.font.SysFont("comicsansms", 24).render("SCORE :",True,(0,255,255))
screen.blit(Text,(0,605))
pygame.display.update()
eat=score=a=b=c=0
backsound.play(loops=-1)
back2.play(loops=-1)
backsound1=backsound
t=True

def run():

    global c
    screen.blit(pygame.font.SysFont("comicsansms", 25).render("READY",True,(0,255,255)),(270,290))
    pygame.display.update()
    while c<500:
        clock.tick(100)
        c+=1
    
    while t:

        global eat,a,b,Text

##        if c==5500:
##            c1.stop()
##            c1.play(backsound)
##            c=0
        clock.tick(100)
        screen.blit(back,(0,0))
        event_handler()
        for i in charlist:
            if i.direc_change==True:
                i.steer()
        for i in charlist:
            mover.update(i)
        for i in pacdotlist:
            pygame.draw.circle(screen,(255,255,0),i,2)
        for i in bigpacdotlist:
            pygame.draw.circle(screen,(0,0,255),i,5)
        for i in charlist:
            i.update()
        if eat==0:
            for i in pacmanlist:
                if screen.get_at((int(i.x1+11),int(i.y1)))!=(255,255,0) or screen.get_at((int(i.x1-11),int(i.y1)))!=(255,255,0) or screen.get_at((int(i.x1),int(i.y1+11)))!=(255,255,0) or screen.get_at((int(i.x1),int(i.y1-11)))!=(255,255,0):
                    # WindowsHardwareFail.play(loops=2)
                    Text=pygame.font.SysFont("comicsansms", 24).render("OOPS!!!",True,(255,255,0))
                    print("You Lost")
                    end()
        if pacdotlist==[] and bigpacdotlist==[]:
            windowsding.play()
            Text=pygame.font.SysFont("comicsansms", 24).render("You Won!!!",True,(255,255,0))
            print("You Win")
            end()
        a+=1
        c+=1
        if eat == 1:
            for i in ghostlist:
                if i.eaten==False:
                    if screen.get_at((int(i.x1+1),int(i.y1)))==(255,255,0) or screen.get_at((int(i.x1-1),int(i.y1)))==(255,255,0) or screen.get_at((int(i.x1),int(i.y1+1)))==(255,255,0) or screen.get_at((int(i.x1),int(i.y1-1)))==(255,255,0):
                        global score
                        hammer.play()
                        score+=500
                        i.x1=i.y1=301
                        i.eaten=True
                        event_handler()
                else:
                    if screen.get_at((int(i.x1+1),int(i.y1)))==(255,255,0) or screen.get_at((int(i.x1-1),int(i.y1)))==(255,255,0) or screen.get_at((int(i.x1),int(i.y1+1)))==(255,255,0) or screen.get_at((int(i.x1),int(i.y1-1)))==(255,255,0):
                        # WindowsHardwareFail.play(loops=2)
                        Text=pygame.font.SysFont("comicsansms", 24).render("OOPS!!!",True,(255,255,0))
                        print("You Lost")
                        end()
            if a>(b+1000):
                b=0
                eat=2
                event_handler()
        screen.blit(Text,(0,605))
        screen.blit(pygame.font.SysFont("comicsansms", 24).render(str(score-((a-10)/10)),True,(0,255,255)),(100,605))
        pygame.display.update()

class mover(object):

    def __init__(self,init_x,init_y):
        
        self.x1=float(init_x)
        self.y1=float(init_y)
        self.vx=self.vy=0.0
        self.direc=None
        self.direc_change=False
    
    def update(self):
        
        self.x1+=self.vx
        self.y1+=self.vy
        x=int(self.x1)
        y=int(self.y1)
        if not self.allowed_to_move_to(int(self.x1+self.vx),int(self.y1+self.vy)):
            self.vx=self.vy=0

    def steer(self):

        x=int(self.x1)
        y=int(self.y1)
        if self.direc =="L":
            if self.allowed_to_move_to(x-1,y):
                self.vy,self.vx=0*self.v,-1*self.v
                self.direc_change=False
                self.direc=None
        elif self.direc =="R":
            if self.allowed_to_move_to(x+1,y):
                self.vy,self.vx=0*self.v,1*self.v
                self.direc_change=False
                self.direc=None
        elif self.direc =="U":
            if self.allowed_to_move_to(x,y-1):
                self.vy,self.vx=-1*self.v,0*self.v
                self.direc_change=False
                self.direc=None
        elif self.direc =="D":
            if self.allowed_to_move_to(x,y+1):
                self.vy,self.vx=1*self.v,0*self.v
                self.direc_change=False
                self.direc=None

class ghost(mover):

    def __init__(self,colour,x=301,y=301):
        
        mover.__init__(self,init_x=x,init_y=y)
        self.v=0.8
        self.colour=self.colourdefault=colour
        self.out=self.eaten=False

    def allowed_to_move_to(self,x,y):

        if screen.get_at((x,y))==((4,4,4)):
            self.out=True
        if self.out ==True:
            return screen.get_at((x,y))==((4,4,4))
        else:
            return screen.get_at((x,y))==((5,5,5))

    def update(self):

        pygame.draw.circle(screen,self.colour,(int(self.x1),int(self.y1)),12)
        # print(self,self.direc,self.direc_change)
        # if self.direc=="L":
        #     pygame.draw.circle(screen,(255,255,255),(int(self.x1)-3,int(self.y1)),2)
        # if self.direc=="R":
        #     pygame.draw.circle(screen,(255,255,255),(int(self.x1)+3,int(self.y1)),2)
        # if self.direc=="U":
        #     pygame.draw.circle(screen,(255,255,255),(int(self.x1),int(self.y1)-3),2)
        # if self.direc=="D":
        #     pygame.draw.circle(screen,(255,255,255),(int(self.x1),int(self.y1)+3),2)

    def event_handler(self):

        self.direc_change=True
        if self.vx==0 and self.vy==0:
            self.direc=random.choice(["U","D","L","R"])
        elif self.vx==0 and self.vy==-0.8:
            self.direc=random.choice(["U","L","R"])
        elif self.vx==0 and self.vy==0.8:
            self.direc=random.choice(["D","L","R"])
        elif self.vx==0.8 and self.vy==0:
            self.direc=random.choice(["U","D","R"])
        elif self.vx==-0.8 and self.vy==0:
            self.direc=random.choice(["U","L","D"])
        else:
            # print("a",self.vx,self.vy)
            pass

class pacman(mover):

    def __init__(self,x=301,y=373):

        mover.__init__(self,init_x=x,init_y=y)
        self.v=1.0

    def allowed_to_move_to(self,x,y):
        
        return screen.get_at((x,y))==((4,4,4))

    def update(self):
        
        global score
        pygame.draw.circle(screen,(255,255,0),(int(self.x1),int(self.y1)),12)
        if (self.x1,self.y1) in pacdotlist:
            pacdotlist.remove((self.x1,self.y1))
            score+=10
        if (self.x1,self.y1) in bigpacdotlist:
            laser.play()
            global eat,b,charlist
            score+=500
            eat=1
            bigpacdotlist.remove((self.x1,self.y1))
            charlist=ghostlist+pacmanlist
            for i in ghostlist:
                i.colour=((0,0,255))
            b=a
    
    def event_handler(self,key):
        
        if key == pygame.K_LEFT:
            self.direc_change=True
            self.direc="L"
        elif key == pygame.K_RIGHT:
            self.direc_change=True
            self.direc="R"
        elif key == pygame.K_UP:
            self.direc_change=True
            self.direc="U"
        elif key == pygame.K_DOWN:
            self.direc_change=True
            self.direc="D"

def event_handler():

    global eat, charlist
    for i in ghostlist:
        if i.eaten==True:
            i.out=False
            i.colour=i.colourdefault
        if i.direc_change==False or (i.vx==0 and i.vy==0):
            ghost.event_handler(i)
    if eat==1:
        screen.blit(pygame.font.SysFont("comicsansms", 24).render(str(int(10-((a-b)/100))),True,((a-b)*.255,((10-((a-b)//100))%2)*.255,((10-((a-b)//100))%2)*255)),(295,605))
    if eat==2:
        eat=0
        charlist=pacmanlist+ghostlist
        for i in ghostlist:
            i.eaten=False
            i.colour=i.colourdefault         
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pacman1.event_handler(event.key)
        elif event.type == pygame.QUIT:
            end()

def end():

    q=0
    while q<100:
        q+=1
        clock.tick(100)
    backsound.stop()
    back2.stop()
    global t,a,score
    t=False
    b=a
    score-=(a/10)
    print("Score:",score)
    screen=pygame.display.set_mode((602,626))
    screen.blit(Text,(250,300))
    ##screen.blit(pygame.font.SysFont("comicsansms", 16).render("Coming  Soon (Hopefully): Pacman level 2",True,(0,255,255)),(150,375))
    screen.blit(pygame.font.SysFont("comicsansms", 16).render("Score:",True,(0,255,255)),(250,200))
    screen.blit(pygame.font.SysFont("comicsansms", 16).render(str(score),True,(255,255,0)),(300,200))
    a=0
    teext=open('hscore.txt', 'r')
    hs=teext.readlines()
    teext.close()
    if score<=int(hs[0]):
        screen.blit(pygame.font.SysFont("comicsansms", 16).render("High Score:",True,(0,255,255)),(230,250))
        screen.blit(pygame.font.SysFont("comicsansms", 16).render(str(int(hs[0])),True,(255,255,0)),(320,250))
    else:
        screen.blit(pygame.font.SysFont("comicsansms", 16).render("New High Score !!!",True,(0,255,255)),(230,250))
        teext=open('hscore.txt', 'w+')
        teext.writelines(list(str(score)))
        teext.close()
    screen.blit(pygame.font.SysFont("comicsansms", 16).render("Press any key to exit.",True,(0,255,255)),(220,375))
    pygame.display.update()
    t=True
    while t:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                t=False
                pygame.quit()
                return

ghost1=ghost((255,0,0))
ghost2=ghost((0,255,255))
ghost3=ghost((0,255,0))
ghost4=ghost((255,0,255))
ghost5=ghost((255,255,255))
ghost6=ghost((0,127,127))
ghost7=ghost((127,0,127))
ghost8=ghost((0,0,0))
ghostlist=[]
gl=[ghost1,ghost2,ghost3,ghost4,ghost5,ghost6,ghost7,ghost8]
for i in range(ch):
    ghostlist.append(gl[i])
pacman1=pacman(301,373)
pacmanlist=[pacman1]
charlist=pacmanlist+ghostlist
run()
