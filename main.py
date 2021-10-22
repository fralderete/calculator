#!/usr/bin/env python3
import sys
from abc import ABCMeta, abstractmethod

dataFile = open('arithmetic.txt', 'r')
errorOne = "First input character is not a digit, or is a zero."
errorTwo = "Symbol not recognized. Looking for a + or - or a digit."
errorThree = "Repeat symbols, leading zero, or whitespace recognized after a + or -."
total = 0

def printInput(userInput):
    print("The input character is: " + str(userInput))
def printCurrentCharacter(userInput):
    print("The current character is: " + str(userInput))
def printTotal(userInput):
    print("The current total is: " + str(userInput))

def strip(userInput):
    userInput = userInput[1:0]
    return userInput

def operation(operator, current, total):
    if operator == "+":
        print("Adding: " + str(total) + "+" + str(current) )
        total = total + current
    elif operator == "-":
        print("Subtracting: " + str(total) + "-" + str(current) )
        total = total - current

    return total

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

class Error(SimpleCalculator):

    def changeState(self,message):
        if message == errorOne:
            self.exit(0,errorOne)

        elif message == errorTwo:
            self.exit(0,errorTwo)

        elif message == errorThree:
            self.exit(0,errorThree)

    def exit(self,status=0, message=None):
        if message:
            print("\nERROR: " + message + " Check you input file, exiting program.")
        sys.exit()

class EndOfFile(SimpleCalculator):
    def __init__(self, newString,current,userInput,total,operator):
        print("\nEND OF FILE STATE")
        total = operation(operator, int(current), total)
        print("End of file reached. The final total is: " + str(total))
        sys.exit()

    def changeState(self):
        pass

class SecondInput(SimpleCalculator):
    def __init__(self,newString,current,userInput,total,operator):
        print("\nSECOND INPUT STATE")
        newString = newString[1:]
        userInput = newString[0]
        current = userInput
        printInput(userInput)
        printCurrentCharacter(current)
        printTotal(total)
        
        if userInput.isdigit() and int(userInput) in range(1,9):
            self.setState(FirstInput(newString,current,userInput,total,operator))

        else:
            self.setState(Error())
            self.changeStateError(errorThree)  
            

    def changeState(self):
        pass

class DigitBuilding(SimpleCalculator):
    def __init__(self,newString,current,userInput,total,operator):
        print("\nDIGIT BUILDING STATE")
        current = str(current) + str(userInput)
        print("Building digit... " + current)
        self.setState(FirstInput(newString,current,userInput,total,operator))

        
    def changeState(self):
        pass

class FirstInput(SimpleCalculator):
    def __init__(self,newString, current, userInput,total,operator):
        print("\nFIRST INPUT STATE")
        length = len(newString)
        
        #check for end of string then change states to EOF
        if length == 1:
            self.setState(EndOfFile(newString,current,userInput,total,operator))

        else:
            newString = newString[1:]
            userInput = newString[0]
            printInput(userInput)
            printCurrentCharacter(current)
            printTotal(total)

            if userInput.isdigit():
                self.setState(DigitBuilding(newString,current,userInput,total,operator))

            elif userInput == "+":
                total = operation(operator, int(current), total)
                operator = userInput
                self.setState(SecondInput(newString, current ,userInput,total,operator))

            elif userInput == "-":
                total = operation(operator, int(current), total)
                operator = userInput
                self.setState(SecondInput(newString, current ,userInput,total,operator))

            else:
                # go to error state and give an error code for initital state
                self.setState(Error())
                self.changeStateError(errorTwo)


    def changeState(self,inputValue):
        pass

class InitialState(SimpleCalculator):
    
    def __init__(self):
        SimpleCalculator.__init__(self)
        # convert list to string
        newString = dataFile.readlines()
        newString = ' '.join(str(e) for e in newString)
        userInput = newString[0]
        current = newString[0]
        operator = "+"

        print("\nINITIAL STATE")

        if userInput.isdigit() and int(userInput) in range(1,9):
            printInput(userInput)
            printCurrentCharacter(current)
            # remove MSB from the string were processing so that the next state has an updated string to work from
            # input collector stores character 0 as the currentNumber
            self.setState(FirstInput(newString, current, userInput,total,operator))
            
        else:
            # go to error state and give an error code for initital state
            self.printInput(newString[0])
            self.setState(Error())
            self.changeStateError(errorOne)
    
    def changeState(self):
        pass

if __name__ == "__main__":
    InitialState()
    
