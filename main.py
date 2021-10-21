#!/usr/bin/env python3
import sys
from abc import abstractmethod, ABCMeta

inputValue = ""
polarity = 1
total = 0
dataFile = open('arithmetic.txt', 'r')

class InternalState(metaclass = ABCMeta):
    @abstractmethod
    def changeState(self):
        pass

class InitialState(InternalState):
    def changeState(self):
        print("InitialState")

class FirstInput(InternalState):
    def changeState(self):
        print("First input state")

class DigitBuilding(InternalState):
    def changeState(self):
        print("Digit building state")

class SecondInput(InternalState):
    def changeState(self):
        print("Second input state")

class Error(InternalState):
    def changeState(self):
        print("Exit program.")

    def exit(status=0, message=None):
        if message:
            print(message + " Exiting program.")
        sys.exit()

class EndOfFile(InternalState):
    def changeState(self):
        print("End of file state")


class SimpleCalculator(InternalState):
    def __init__(self):
        self.state = None

    def setState(self,status):
        self.state = status
    
    def getState(self):
        return self.state

    def changeState(self):
        self.state = self.state.changeState()
        

if __name__ == "__main__":

    Calculator = SimpleCalculator()
    Initiate = InitialState()
    FirstInputState = FirstInput()
    ErrorState = Error()

    characters = dataFile.readlines()

    for characters in characters:    
        if characters[0].isdigit():
            inputValue = characters[0]
            if int(inputValue) in range(1,9):
                currentNumber = inputValue
                print("Current number is: " + currentNumber)
                # go to first input state
                Calculator.setState(Initiate)
                Calculator.changeState()
    
        else:
            # go to error state and give an error code for initital state
            ErrorState.exit("First character was not a digit from 1-9.")