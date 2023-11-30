# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:42:14 2023

@author: ikank
"""
import random, simpleGE, pygame
"""
dice image original: https://opengameart.org/content/dice-4
"""
class Die(simpleGE.SuperSprite):
    #initialize
    def __init__(self, scene):
        super().__init__(scene)
         
        self.setImage("1_dot.png")
        self.setSize(100,100)
        
        self.images = [None,
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
        self.text = "You Win!"
        self.center = (320,240)
        self.size = (100,100)
        
class ScoreTotal(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Total Score: 4"
        self.center = (320,370)
        self.size = (170,70)
        
class Game(simpleGE.Scene):
    
    def __init__(self):
        super().__init__()
        
        pygame.init()
         
        # Initializing surface
        surface = pygame.display.set_mode((640, 480))
         
        # Initializing RGB Color
        color = (255, 0, 0)
         
        # Changing surface color
        surface.fill(color)
        pygame.display.flip() 
        self.btnRoll = BtnRoll()
        self.btnHigher = BtnHigher()
        self.btnFold = BtnFold()
        self.score = ScoreTotal()
        self.dice = []
        self.newDice = []
        self.tries = 0
        self.totalValue = 0
        self.rollAgainValue = 0 
        self.compScore = 0
        self.totalComp = 0
        self.rollAgainDice = []
        self.rollAgain = Die(self)
        
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
            rollAgain = Die(self)
            rollAgain.setPosition((320 + (i * 100), 250))
            self.rollAgainDice.append(rollAgain)
        
        self.sprites = [self.dice, self.rollAgainDice, self.btnRoll, self.btnHigher, self.btnFold,self.score]
        self.sprites.remove(self.rollAgainDice)
    def update(self):
        if self.btnRoll.clicked:
            self.tries += 1
            self.btnRoll.hide()
            self.btnHigher.show((160,290))
            self.btnFold.show((480,290))
            for die in self.dice:
                die.roll()
                self.totalValue += die.value
            self.score.text = (f"Total Score: {self.totalValue}")
        if self.btnFold.clicked:
            self.btnHigher.hide()
            for die in self.dice:
                self.score.text = (f"Total Score: {self.totalValue}")
            self.totalValue = 21 - self.totalValue
            self.totalComp = 21 - self.totalComp
            if self.totalValue >= 0:
                if self.totalValue < self.totalComp:
                    print("You win!")
                elif self.totalValue > 21:
                    print("You bust!")
            else:
                print("You bust!")
        if self.btnHigher.clicked:
            self.rollAgain.setPosition((320,250))
            self.tries += 1
            if len(self.dice) >= 5:
                self.sprites.remove(self.dice)
                self.sprites.append(self.rollAgainDice)
                
            if self.tries <= 3:  
                    for i in range(1):
                        rollAgain = Die(self)
                        #self.rollAgainDice.append(rollAgain)
                    for die in self.rollAgainDice:
                        die.roll()
                        self.rollAgainDice.clear()
                        print(f"Total: {self.totalValue}")
                        print(die.value)
                        self.rollAgainValue += die.value
                        self.totalValue += self.rollAgainValue
                        self.score.text = (f"Total Score: {self.totalValue}")
            else:
                print("Max tries reached!") 
            if self.totalValue == 21:
                print("You win!")
                self.btnHigher.hide()
                self.btnFold.hide()
            if self.totalValue >= 22:
                print("You bust!")
                self.btnHigher.hide()
                self.btnFold.hide()
            if self.rollAgainValue >= 22:
                print("You bust!")
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()