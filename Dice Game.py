# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:42:14 2023

@author: ikank
"""
import random, simpleGE, pygame
"""
dice image original: https://opengameart.org/content/dice-4
game background: https://wallpaper.mob.org/gallery/tag=tavern/
game background music: https://opengameart.org/content/woodland-fantasy
"""
class Die(simpleGE.SuperSprite):
    #initialize
    def __init__(self, scene):
        super().__init__(scene)
         
        self.setImage("1_dot.png")
        self.setSize(60,60)
        
        self.images = [pygame.image.load("blank.png"),
                       pygame.image.load("1_dot.png"),                      
                       pygame.image.load("2_dots.png"),
                       pygame.image.load("3_dots.png"),
                       pygame.image.load("4_dots.png"),
                       pygame.image.load("5_dots.png"),
                       pygame.image.load("6_dots.png"),                      
                       ]
        
        for i in range(1, 7):
            self.images[i] = pygame.transform.scale(self.images[i], (60, 60))
            
    def roll(self):
        self.value = random.randint(1,6)
        self.imageMaster = self.images[self.value]


class ExtraDie(simpleGE.SuperSprite):
    #initialize
    def __init__(self, scene):
        super().__init__(scene)
         
        self.setImage("blank.png")
        self.setSize(60,60)
        
        self.images = [pygame.image.load("blank.png"),
                       pygame.image.load("1_dot.png"),                      
                       pygame.image.load("2_dots.png"),
                       pygame.image.load("3_dots.png"),
                       pygame.image.load("4_dots.png"),
                       pygame.image.load("5_dots.png"),
                       pygame.image.load("6_dots.png"),                      
                       ]
        
        for i in range(1, 7):
            self.images[i] = pygame.transform.scale(self.images[i], (60, 60))
            
    def roll(self):
        self.value = random.randint(1,6)
        self.imageMaster = self.images[self.value]
        
class BtnHigher(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.center = ((1600, 2900))
        self.text = "Roll Again"

class BtnFold(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.center = ((4800, 2900))
        self.text = "Fold"

class BtnRoll(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.center = ((320, 240))
        self.text = "Roll 'em"

class LabelWin(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Dice Blackjack"
        self.center = (320,40)
        self.size = (170,40)
        
class CompWin(simpleGE.Label):
    """
    class label computer score
    """
    def __init__(self):
        super().__init__()
        self.text = "Basic Text"
        self.center = (88,40)
        self.size = (170,40)

class ScoreTotal(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Total Score: 4"
        self.center = (320,370)
        self.size = (170,40)
        
class Game(simpleGE.Scene):
    
    def __init__(self):
        super().__init__()
        
        pygame.init()
         
        # Initializing surface
        surface = pygame.display.set_mode((640, 480))
         
        # Initializing RGB Color
        color = (255, 0, 0)
        
        #tavern background
        self.background = pygame.image.load("tavern.png")
        self.background = pygame.transform.scale(self.background, (640, 480))
        self.setCaption("Dice Blackjack")
        
        #dice roll sound effect
        self.sndRoll = simpleGE.Sound("diceRoll.ogg")
        
        pygame.mixer.music.load("tavern_music.ogg")
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1)
        
        # Changing surface color
        surface.fill(color)
        pygame.display.flip() 
        self.btnRoll = BtnRoll()
        self.btnHigher = BtnHigher()
        self.btnFold = BtnFold()
        self.score = ScoreTotal()
        self.winnerLabel = LabelWin()
        self.compLabel = CompWin()
        self.dice = []
        self.newDice = []
        self.tries = 0
        self.compTries = 0
        self.totalValue = 0
        self.rollAgainValue = 0 
        self.compScore = 0
        self.totalComp = 0
        self.rollAgainDice = []
        self.thirdDice = []
        
        for i in range(4):
            self.compScore = random.randint(1,6)
            print(self.compScore)
            self.totalComp += self.compScore
        print(f"Comp Score: {self.totalComp}")
        
        for i in range(4):
            newDie = Die(self)
            newDie.setPosition((80 + (i * 160), 120))
            self.dice.append(newDie)
        
        for i in range(1):
            newDie = ExtraDie(self)
            newDie.setPosition((157 + (i *160), 220))
            self.rollAgainDice.append(newDie)
        
        for i in range(1):
            newDie = ExtraDie(self)
            newDie.setPosition((320, 220))
            self.thirdDice.append(newDie)
        
        self.sprites = [self.dice, self.thirdDice, self.rollAgainDice, self.btnRoll, self.btnHigher, self.btnFold,
                        self.score,self.compLabel,self.winnerLabel]
        self.winnerLabel.hide()
        #self.sprites.remove(self.rollAgainDice)
    
    def update(self):
        self.compLabel.text = (f"Comp Score: {self.totalComp}")
        differenceValue = 21 - self.totalValue
        differenceComp = 21 - self.totalComp
        
        if self.totalValue == 21:
            self.winnerLabel.show((320,40))
            self.winnerLabel.text = ("You win!")
            self.score.bgColor = (34,139,34)
            self.compLabel.bgColor = (255,0,0)
            self.btnHigher.hide()
            self.btnFold.hide()
        if self.totalValue >= 22:
            self.winnerLabel.show((320,40))
            self.winnerLabel.text = ("You bust!")
            self.compLabel.bgColor = (34,139,34)
            self.score.bgColor = (255,0,0)
            self.btnHigher.hide()
            self.btnFold.hide()
        
        if self.totalComp == 21:
            self.winnerLabel.show((320,40))
            self.winnerLabel.text = ("You lose!")
            self.compLabel.bgColor = (34,139,34)
            self.score.bgColor = (255,0,0)
            self.btnRoll.hide()
            self.btnHigher.hide()
            self.btnFold.hide()
            
        if self.totalComp >= 22:
            self.winnerLabel.show((320,40))
            self.winnerLabel.text = ("You win!")
            self.score.bgColor = (34,139,34)
            self.compLabel.bgColor = (255,0,0)
            self.btnRoll.hide()
            self.btnHigher.hide()
            self.btnFold.hide()
            
        if self.btnRoll.clicked:
            self.sndRoll.play()
            self.tries += 1
            self.compTries += 1
            self.btnRoll.hide()
            self.btnHigher.show((160,290))
            self.btnFold.show((480,290))
            for die in self.dice:
                die.roll()
                self.totalValue += die.value
            self.score.text = (f"Total Score: {self.totalValue}")
        if self.btnFold.clicked:
            """
            when fold button is clicked the game should ensure that the 
            computer can still mathematically win
            """
            differenceValue = 21 - self.totalValue
            differenceComp = 21 - self.totalComp
            if differenceComp >= 1:
                if differenceComp <= 12:
                    for tries in range(3 - self.compTries):
                        print("The computer can still win!")
                        self.compTries += 1
                        self.compScore = random.randint(1,6)
                        self.totalComp += self.compScore
                        print(f"Comp Score: {self.totalComp}")
                if differenceValue >= 0:
                    if differenceValue > differenceComp:
                        self.winnerLabel.show((320,40))
                        self.winnerLabel.text = ("You lose!")
                        self.score.bgColor = (34,139,34)
                        self.compLabel.bgColor = (255,0,0)
                    if self.totalValue < self.totalComp:
                        self.winnerLabel.show((320,40))
                        self.winnerLabel.text = ("You win!")
                        self.score.bgColor = (34,139,34)
                        self.compLabel.bgColor = (255,0,0)
                        self.btnHigher.hide()
                        self.btnFold.hide()
                if differenceComp == differenceValue:
                    self.winnerLabel.show((320,40))
                    self.winnerLabel.text = ("Tie!")
                    self.score.bgColor = (255,255,153)
                    self.compLabel.bgColor = (255,255,153)
                    self.btnHigher.hide()
                    self.btnFold.hide()
            else:
                self.winnerLabel.show((320,40))
                self.winnerLabel.text = ("You lose!")
                self.compLabel.bgColor = (34,139,34)
                self.score.bgColor = (255,0,0)
            if differenceComp >= 0:
                if differenceValue < differenceComp:
                    self.winnerLabel.show((320,40))
                    self.winnerLabel.text = ("You lose!")
                    self.score.bgColor = (34,139,34)
                    self.compLabel.bgColor = (255,0,0)
                    self.btnFold.hide()
            else:
                self.winnerLabel.show((320,40))
                self.winnerLabel.text = ("You win!")
                self.score.bgColor = (34,139,34)
                self.compLabel.bgColor = (255,0,0)
                self.btnRoll.hide()
                self.btnHigher.hide()
                self.btnFold.hide()
            self.btnHigher.hide()
            differenceValue = 21 - self.totalValue
            differenceComp = 21 - self.totalComp
            if differenceValue >= 0:
                if self.totalComp >= 0:
                    print(differenceValue)
                    print(differenceComp)
                    if differenceValue < differenceComp:
                        self.winnerLabel.show((320,40))
                        self.winnerLabel.text = ("You win!")
                        self.score.bgColor = (34,139,34)
                        self.compLabel.bgColor = (255,0,0)
                    if differenceValue > differenceComp:
                        self.winnerLabel.show((320,40))
                        self.winnerLabel.text = ("You lose!")
                        self.compLabel.bgColor = (34,139,34)
                        self.score.bgColor = (255,0,0)
            else:
                self.winnerLabel.show((320,40))
                self.winnerLabel.text = ("You bust!")  
        
            
        if self.btnHigher.clicked:
            """
            if roll again button is pressed the game adds tries to each player's
            turn
            """
            self.sndRoll.play()
            if self.totalComp == 21:
                self.winnerLabel.show((320,40))
                self.winnerLabel.text = ("You lost!")
                self.compLabel.bgColor = (34,139,34)
                self.score.bgColor = (255,0,0)
                self.btnHigher.hide()
                self.btnFold.hide()
            else:
                self.tries += 1
                if len(self.dice) >= 5:
                    self.sprites.remove(self.dice)     
                if self.tries <= 3:
                    if self.tries <= 2:
                        for die in self.rollAgainDice:
                            self.sndRoll.play()
                            die.roll()
                            print(len(self.rollAgainDice))
                            print(f"Total: {self.totalValue}")
                            self.rollAgainValue += die.value
                            print(self.rollAgainValue)
                            self.totalValue += self.rollAgainValue
                            self.score.text = (f"Total Score: {self.totalValue}")
                            self.rollAgainValue = 0
                        if self.totalValue > 21:
                            self.winnerLabel.show((320,40))
                            self.winnerLabel.text = ("You bust!")
                            self.compLabel.bgColor = (34,139,34)
                            self.score.bgColor = (255,0,0)
                            self.btnHigher.hide()
                            self.btnFold.hide()
                        else:
                            for i in range(1):
                                self.compScore = random.randint(1,6)
                                self.totalComp += self.compScore
                                print(f"Comp Score: {self.totalComp}")
                                self.compTries += 1
                    if self.tries == 3:
                        for die in self.thirdDice:
                            self.sndRoll.play()
                            die.roll()
                            print(len(self.thirdDice))
                            print(f"Total: {self.totalValue}")
                            self.rollAgainValue += die.value
                            print(self.rollAgainValue)
                            self.totalValue += self.rollAgainValue
                            self.score.text = (f"Total Score: {self.totalValue}")
                            self.rollAgainValue = 0                                
                else:
                    print("Max tries reached!")
                    differenceValue = 21 - self.totalValue
                    differenceComp = 21 - self.totalComp
                    if differenceComp == differenceValue:
                        self.winnerLabel.show((320,40))
                        self.winnerLabel.text = ("It's a tie!")
                        self.score.bgColor = (255,255,153)
                        self.compLabel.bgColor = (255,255,153)
                        self.btnHigher.hide()
                        self.btnFold.hide()
                    if differenceComp < differenceValue:
                        self.winnerLabel.show((320,40))
                        self.winnerLabel.text = ("You lose!")
                        self.compLabel.bgColor = (34,139,34)
                        self.score.bgColor = (255,0,0)
                        self.btnHigher.hide()
                        self.btnFold.hide()
                    if differenceComp > differenceValue:
                        self.winnerLabel.show((320,40))
                        self.winnerLabel.text = ("You win!")
                        self.score.bgColor = (34,139,34)
                        self.compLabel.bgColor = (255,0,0)
                        self.btnHigher.hide()
                        self.btnFold.hide()
                    if self.totalValue == 21:
                        self.winnerLabel.show((320,40))
                        self.winnerLabel.text = ("You win!")
                        self.score.bgColor = (34,139,34)
                        self.compLabel.bgColor = (255,0,0)
                        self.btnHigher.hide()
                        self.btnFold.hide()
                    
                
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()