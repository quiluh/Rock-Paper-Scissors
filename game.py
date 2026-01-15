import numpy as np
import matplotlib.pyplot as plt

class ChoiceTracker:
    def __init__(self):
        self._choices = {"r":0,"p":0,"s":0}
    
    @property
    def Choices(self) -> dict:
        return self._choices
    
    def addChoice(self,playerInput:str) -> bool:
        if playerInput.strip().replace(" ","") in self._choices:
            self._choices[playerInput.strip().replace(" ","")] += 1
            return True
        else:
            return False

class Visualizer:
    pass

class Game:
    def __init__(self):
        self.tracker = ChoiceTracker()
    
    def endGame(self):
        pass

    def play(self):
        if choice.lower().replace(" ","") in self.tracker.Choices:
            self.tracker.Choices[choice.lower().replace(" ","")] += 1
        elif choice.lower().replace(" ","") == "e":
            self.endGame()
        
        self.play()


while True:
    choice = input("Input your choice: ")
    if choice.lower().replace(" ","") in choices:
        choices[choice.lower().replace(" ","")] += 1
    elif choice.lower().replace(" ","") == "e":
        break

plt.bar(choices.keys(),choices.values())
plt.show()