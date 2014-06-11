#########################################################
#                Mastermind v2.1                        #
#                      by                               #
#                Karl Hirschhorn                        #
#                                                       #
#                Copyright 2011                         #
#########################################################                 

import pygame, sys, os, random
from pygame.locals import *

pygame.init()

screen_width = 380
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Mastermind!')
GREY = (127,127,127)
BLACK = (0,0,0)
DKGREY = (65,65,65)
WHITE = (255,255,255)
font = pygame.font.SysFont('agencyfb', 24)
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Button(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image)
    def setCords(self,x,y):
        self.rect.topleft = x,y
        screen.blit(self.image, (x,y))
    def pressed(self,mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
      

class Board:
    def __init__(self):
        self.board = ["e  e  e  e",
                      "e  e  e  e",
                      "e  e  e  e",
                      "e  e  e  e",
                      "e  e  e  e",
                      "e  e  e  e",
                      "e  e  e  e",
                      "e  e  e  e",]
        self.bwboard = ["e  e  e  e",
                        "e  e  e  e",
                        "e  e  e  e",
                        "e  e  e  e",
                        "e  e  e  e",
                        "e  e  e  e",
                        "e  e  e  e",
                        "e  e  e  e",]
        self.guess = ["e", "e", "e", "e"]
        self.gx = 270
        self.gy = 260
        self.gby = 420
        self.bluebut = Button('bluepeg.png')
        self.redbut = Button('redpeg.png')
        self.yelbut = Button('yellowpeg.png')
        self.orbut = Button('orangepeg.png')
        self.purpbut = Button('purppeg.png')
        self.greenbut = Button('greenpeg.png')
        self.submitbut = Button('submit.png')
        self.font = pygame.font.SysFont('agencyfb', 18)
        self.font2 = pygame.font.SysFont('agencyfb', 24)
        
        
    def drawboard(self):
        self.guessline = 1
        self.bx = 30
        self.by = 100
        for row in self.board:
            self.g = str(self.guessline)
            self.text = self.font.render(self.g, 1, (10, 10, 10))
            screen.blit(self.text, (self.bx - 15, self.by))
            self.guessline += 1
            pygame.display.update()
            for col in row:
                if col == "e":
                    screen.blit(empty_peg, (self.bx, self.by))
                elif col == "r":
                    screen.blit(red_peg, (self.bx, self.by))
                elif col == "b":
                    screen.blit(blue_peg, (self.bx, self.by))
                elif col == "g":
                    screen.blit(green_peg, (self.bx, self.by))
                elif col == "p":
                    screen.blit(purple_peg, (self.bx, self.by))
                elif col == "y":
                    screen.blit(yellow_peg, (self.bx, self.by))
                elif col == "o":
                    screen.blit(orange_peg, (self.bx, self.by))
                else:
                    continue
                self.bx += 35
            self.by += 35
            self.bx = 30
            pygame.display.flip()
       
       
        

    def drawbw(self):
        self.bwx = 175
        self.bwy = 110
        for row in self.bwboard:
            for col in row:
                if col == "e":
                    screen.blit(bw_empty, (self.bwx, self.bwy))
                elif col == "b":
                    screen.blit(bw_black, (self.bwx, self.bwy))
                elif col == "w":
                    screen.blit(bw_white, (self.bwx, self.bwy))
                else:
                    continue
                self.bwx += 18
            self.bwy += 35
            self.bwx = 175
            pygame.display.flip()
            

    def colorbin(self):
        pygame.draw.rect(screen, BLACK, (self.gx + 3, self.gy + 3, 90,110))
        pygame.draw.rect(screen, GREY, (self.gx,self.gy,90,110))
        self.redbut.setCords(self.gx+10,self.gy+5)
        self.orbut.setCords(self.gx+50,self.gy+5)
        self.yelbut.setCords(self.gx+10, self.gy +40)
        self.greenbut.setCords(self.gx+50, self.gy+40)
        self.bluebut.setCords(self.gx+10, self.gy+75)
        self.purpbut.setCords(self.gx+50, self.gy+75)
        pygame.display.update()

    def guessdisplay(self):
        self.bx = 30
        for row in self.guess:
            if row == "e":
                screen.blit(empty_peg, (self.bx, self.gby))
            elif row == "r":
                screen.blit(red_peg, (self.bx, self.gby))
            elif row == "b":
                screen.blit(blue_peg, (self.bx, self.gby))
            elif row == "g":
                screen.blit(green_peg, (self.bx, self.gby))
            elif row == "p":
                screen.blit(purple_peg, (self.bx, self.gby))
            elif row == "y":
                screen.blit(yellow_peg, (self.bx, self.gby))
            elif row == "o":
                screen.blit(orange_peg, (self.bx, self.gby))
            else:
                continue
            self.bx += 35
            pygame.display.flip()       
            
    def pegcheck(self, guess):
        self.strikes1 = []
        self.strikes2 = []
        self.blackpeg=0
        self.whitepeg=0
        self.bwcount = []
        for i in range(len(guess)):
            if guess[i] == solution[i]:
                self.blackpeg += 1
                self.strikes1.append(i)
                self.strikes2.append(i)
                self.bwcount.append("b")
        for x in range(len(solution)):
            for y in range(len(solution)):
                if x not in self.strikes1 and y not in self.strikes2:
                    if guess[x] == solution[y]:
                        self.whitepeg += 1
                        self.strikes1.append(x)
                        self.strikes2.append(i)
                        self.bwcount.append("w")
            self.bwboard[turn] = self.bwcount

    def win(self):
        screen.blit(winbg, (0,0))
        pygame.display.flip()
        pygame.time.delay(5000)
        exit()

    def lose(self):
        screen.blit(losebg, (0,0))
        self.bx = 115
        for row in solution:
            if row == "e":
                screen.blit(empty_peg, (self.bx, 400))
            elif row == "r":
                screen.blit(red_peg, (self.bx, 400))
            elif row == "b":
                screen.blit(blue_peg, (self.bx, 400))
            elif row == "g":
                screen.blit(green_peg, (self.bx, 400))
            elif row == "p":
                screen.blit(purple_peg, (self.bx, 400))
            elif row == "y":
                screen.blit(yellow_peg, (self.bx, 400))
            elif row == "o":
                screen.blit(orange_peg, (self.bx, 400))
            else:
                continue
            self.bx += 35
        pygame.display.update()
        pygame.time.delay(5000)
        exit()

def getanswer():
    #generates the solution which the player must guess
    availcolors = ("r", "o", "y", "g", "b", "p")
    answer = [random.choice(availcolors) for i in range(4)]
    return answer

def drawbg():
    background, bg_rect = load_image('mmbg2.jpg')
    screen.blit(background, (0,0))
    pygame.draw.line(screen, BLACK, (30, 55), (350, 55), 2)
    pygame.draw.line(screen, DKGREY, (32,57), (352, 57), 2)
    pygame.draw.line(screen, BLACK, (30, 380), (350, 380), 2)
    pygame.draw.line(screen, DKGREY, (32,382), (352, 382), 2)
    heading_text = font.render("Guesses", 1, (10, 10, 10))
    heading_textpos = (67, 65)
    current_guess_text = font.render('Current Guess', 1, (10,10,10))
    current_guesspos = (44, 385)
    screen.blit(current_guess_text, current_guesspos)
    screen.blit(heading_text, heading_textpos)
    pygame.display.update()

empty_peg, empty_rect = load_image('mmempty.png')
red_peg, red_peg_rect = load_image('redpeg.png')
blue_peg, blue_peg_rect = load_image('bluepeg.png')
green_peg, green_peg_rect = load_image('greenpeg.png')
purple_peg, purple_peg_rect = load_image('purppeg.png')
yellow_peg, yellow_peg_rect = load_image('yellowpeg.png')
orange_peg, orange_peg_rect = load_image('orangepeg.png')
bw_empty, bw_empty_rect = load_image('bwempty1.png')
bw_white, bw_white_rect = load_image('bwwhite.png')
bw_black, bw_black_rect = load_image('bwblack.png')
winbg, winbg_rect = load_image('mmbgwin.jpg')
losebg, losebg_rect = load_image('mmbglose.jpg')

#Main Loop

drawbg()

board = Board()

solution = getanswer()
print solution
turn = 0
board.drawboard()
board.colorbin()
board.drawbw()
board.guessdisplay()
deltat = clock.tick(10)
guessnum = 0
guessresult = []
pos = pygame.mouse.get_pos()

while turn <= 8:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif turn == 8:
            board.lose()
        elif event.type == MOUSEBUTTONDOWN and guessnum < 4:
            pos = pygame.mouse.get_pos()
            if board.bluebut.pressed(pos) == True:
                board.guess[guessnum] = "b"
                board.guessdisplay()
                guessnum += 1
            elif board.yelbut.pressed(pos) == True:
                board.guess[guessnum] = "y"
                board.guessdisplay()
                guessnum += 1
                
            elif board.orbut.pressed(pos) == True:
                board.guess[guessnum] = "o"
                board.guessdisplay()
                guessnum += 1
                
            elif board.purpbut.pressed(pos) == True:
                board.guess[guessnum] = "p"
                board.guessdisplay()
                guessnum += 1
                
            elif board.greenbut.pressed(pos) == True:
                board.guess[guessnum] = "g"
                board.guessdisplay()
                guessnum += 1
                
            elif board.redbut.pressed(pos) == True:
                board.guess[guessnum] = "r"
                board.guessdisplay()
                guessnum += 1
            else:
                continue
        elif guessnum == 4:
            board.board[turn] = board.guess
            board.drawboard()
            board.pegcheck(board.guess)
            board.drawbw()
            board.guess = ["e", "e", "e", "e"]
            turn += 1
            board.guessdisplay()
            board.drawbw()
            guessnum = 0
            if board.blackpeg == 4:
                board.win()
                break   
        else:
            continue
        
