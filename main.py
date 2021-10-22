#!/usr/bin/env python3
import sys
from abc import ABCMeta, abstractmethod

dataFile = open('arithmetic.txt', 'r')
errorOne = "First input character is not a digit, or is a zero."
errorTwo = "Symbol not recognized. Looking for a + or - or a digit."

def printInput(userInput):
    print("The current character is: " + str(userInput))
def printCurrentCharacter(userInput):
    print("The input character is: " + str(userInput))
def printTotal(userInput):
    print("The current total is: " + str(userInput))
def strip(userInput):
    userInput = userInput[1:0]
    return userInput

class SimpleCalculator:
    @abstractmethod
    def __init__(self):
        self.state = None
        self.currentNumber = None

    def setState(self,status):
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

class SecondInput(SimpleCalculator):
    def __init__(self,userInput):
        pass

    def changeState(self):
        pass

class EndOfFile(SimpleCalculator):
    def changeState(self):
        pass

class DigitBuilding(SimpleCalculator):
    def __init__(self,newString,userInput):
        character = newString
        print("DIGIT BUILDING STATE")

        if character[0].isdigit():
            printInput(userInput)
            printCurrentCharacter(character[0])
            userInput = str(userInput) + str(character[0])
            strip(character)
            print("Building digit... " + userInput)
            self.setState(FirstInput(character,userInput))

        else:
            pass
        
    def changeState(self):
        pass

class FirstInput(SimpleCalculator):
    def __init__(self,newString, userInput):
        character = newString
        userInput = str(userInput)
        print("FIRST INPUT STATE")
        
        if character[0].isdigit():
            printInput(userInput)
            printCurrentCharacter(character[0])
            character = character[1:]
            self.setState(DigitBuilding(character,userInput))

        elif character[0] == "+" or character[0] == "-":
            printInput(userInput)
            printCurrentCharacter(character[0])
            character = character[1:]
            self.setState(SecondInput(character,userInput))
            
        else:
            # go to error state and give an error code for initital state
            self.printInput(character[0])
            self.setState(Error())
            self.changeStateError(errorTwo)


    def changeState(self,inputValue):
        pass

class InitialState(SimpleCalculator):
    
    def __init__(self):
        SimpleCalculator.__init__(self)
        # convert list to string
        character = dataFile.readlines()
        character = ' '.join(str(e) for e in character)
        print("INITIAL STATE")

        if character[0].isdigit() and int(character[0]) in range(1,9):
            userInput = character[0]
            printInput(userInput)
            printCurrentCharacter(character[0])
            # remove MSB from the string were processing so that the next state has an updated string to work from
            # input collector stores character 0 as the currentNumber
            self.setState(FirstInput(character, userInput))
            
        else:
            # go to error state and give an error code for initital state
            self.printInput(character[0])
            self.setState(Error())
            self.changeStateError(errorOne)
    
    def changeState(self):
        pass

if __name__ == "__main__":
    InitialState()
    
