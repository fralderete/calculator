#!/usr/bin/env python3
import sys
from abc import ABCMeta, abstractmethod

errorOne = "First input character is not a digit."
errorTwo = "First input digit is not 1-9."

class SimpleCalculator:
    @abstractmethod
    def __init__(self):
        dataFile = open('arithmetic.txt', 'r')
        self.state = None
        self.userInput = dataFile.readlines()
        self.currentNumber = None

    def setState(self,status):
        print("Transitioning to " + str(status) + " state.")
        self.state = status
    
    def getState(self):
        return self.state

    def changeState(self):
        self.state = self.state.changeState()

    def changeStateError(self,message):
        self.state = self.state.changeState(message)

    def inputCollector(self,userInput):
        self.currentNumber = userInput
        self.printInput(self.currentNumber)

    def printInput(self,userInput):
        print("The input character is: " + str(userInput))

    def printCurrentNumber(self, userInput):
        print("The current character is: " + str(userInput))

    def printTotal(self, userInput):
        print("The current total is: " + str(userInput))

class Error(SimpleCalculator):

    def changeState(self,message):
        if message == errorOne:
            self.exit(0,errorOne)

        elif message == errorTwo:
            self.exit(0,errorTwo)

    def exit(self,status=0, message=None):
        if message:
            print("ERROR: " + message + " Exiting program.")
        sys.exit()

class FirstInput(SimpleCalculator):
    def changeState(self,inputValue):
        pass

class DigitBuilding(SimpleCalculator):
    def changeState(self):
        pass

class SecondInput(SimpleCalculator):
    def changeState(self):
        pass

class EndOfFile(SimpleCalculator):
    def changeState(self):
        pass

class InitialState(SimpleCalculator):
    
    def __init__(self):
        SimpleCalculator.__init__(self)
        character = self.userInput

        for character in character:
            if character[0].isdigit():
                inputValue = int(character[0])

                if inputValue in range(1,9):
                    #self.printCurrentNumber(inputValue)
                    #input collector stores character 0 as the currentNumber
                    self.inputCollector(inputValue)
                    self.setState(FirstInput())
                    self.changeState()

                else: 
                    # go to error state and give an error code for initital state
                    self.printInput(inputValue)
                    self.setState(Error())
                    self.changeStateError(errorTwo)
                
            else:
                # go to error state and give an error code for initital state
                self.printInput(character[0])
                self.setState(Error())
                self.changeStateError(errorOne)

    
    def changeState(self):
        pass

if __name__ == "__main__":
    print("Starting at initial state, and checking first character input.")
    InitialState()
    
