#!/usr/bin/env python3
import sys
from abc import ABCMeta, abstractmethod

inputValue = ""
polarity = 1
total = 0
dataFile = open('arithmetic.txt', 'r')
errorOne = "First input character is not a digit."
errorTwo = "First input digit is not 1-9."

class InternalState(metaclass = ABCMeta):
    @abstractmethod
    def changeState(self):
        pass

class InitialState(InternalState):
    def changeState(self):
        pass

class FirstInput(InternalState):
    def changeState(self):
        pass

class DigitBuilding(InternalState):
    def changeState(self):
        pass

class SecondInput(InternalState):
    def changeState(self):
        pass

class Error(InternalState):

    def changeState(self,message):
        if message == errorOne:
            self.exit(0,errorOne)

        elif message == errorTwo:
            self.exit(0,errorTwo)

    def exit(self,status=0, message=None):
        if message:
            print("ERROR: " + message + " Exiting program.")
        sys.exit()

class EndOfFile(InternalState):
    def changeState(self):
        pass

class SimpleCalculator(InternalState):
    def __init__(self):
        self.state = None
        self.userInput = None

    def setState(self,status):
        print("Transitioning to " + str(status) + " state.")
        self.state = status
    
    def getState(self):
        return self.state

    def changeState(self,message):
        self.state = self.state.changeState(message)

    def inputCollector(self,textInput):
        self.userInput = textInput

        if int(self.userInput) in range(1,9):
            currentNumber = inputValue
            # print("Current number is: " + currentNumber)
            # go to first input state
            Calculator.setState(Initiate)
            Calculator.changeState()
            
        else:
            # go to error state and give an error code for initital state
            # ErrorState.exit("First character was not a digit from 1-9.")
            Calculator.setState(ErrorState)
            Calculator.changeState(errorTwo)


    def printInput(self):
        print("The current character being processed is: " + self.userInput)
        

if __name__ == "__main__":

    Calculator = SimpleCalculator()
    Initiate = InitialState()
    FirstInputState = FirstInput()
    ErrorState = Error()
    characters = dataFile.readlines()

    for characters in characters:    
        if characters[0].isdigit():
            inputValue = characters[0]
            Calculator.inputCollector(characters[0])
            #Calculator.printInput()

        else:
            # go to error state and give an error code for initital state
            #ErrorState.exit("First character was not a digit.")
            Calculator.setState(ErrorState)
            Calculator.changeState(errorOne)
