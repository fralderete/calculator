#!/usr/bin/env python3
#
#
#   Simple calculator to show a state design pattern, can only add or subtract
#   By: Francisco E. Alderete, Richard Padilla, Karl Dill, Venkata Surya Dasari
#
#

import sys
from abc import ABCMeta, abstractmethod
from states import *

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



# error handling and exit
class Error(SimpleCalculator):

    def changeState(self,message):
        if message:
            self.exit(0,message)

    def exit(self,status=0, message=None):
        if message:
            print("\nERROR: " + message + " Check you input file, exiting program.")
        sys.exit()

# performs the final operation without decrementing the string so we don't
# hit an error, then exits the program
class EndOfFile(SimpleCalculator):
    def __init__(self, newString,current,userInput,total,operator):
        print("\nEND OF FILE STATE")
        total = operation(operator, int(current), total)
        print("End of file reached. The final total is: " + str(total))
        sys.exit()

    def changeState(self):
        pass

# this class is necessary to have a digit 1-9 check after
# an operator since we can have no leading zeroes
# also resets the current variable between math symbols
class SecondInput(SimpleCalculator):
    def __init__(self,newString,current,userInput,total,operator):
        print("\nSECOND INPUT STATE")

        # strings MSB is removed 
        newString = newString[1:]
        userInput = newString[0]
        current = userInput
        printInput(userInput)
        printCurrentCharacter(current)
        printTotal(total)
        
        if userInput.isdigit() and int(userInput) in range(1,10):
            self.setState(FirstInput(newString,current,userInput,total,operator))

        else:
            self.setState(Error())
            self.changeStateError(errorThree)  
            

    def changeState(self):
        pass

# since we are going character by character this class builds numbers up between operators
class DigitBuilding(SimpleCalculator):
    def __init__(self,newString,current,userInput,total,operator):
        print("\nDIGIT BUILDING STATE")
        current = str(current) + str(userInput)
        print("Building digit... " + current)
        self.setState(FirstInput(newString,current,userInput,total,operator))

        
    def changeState(self):
        pass

# the main input processor, also checks for end of file
# handles the adding and subtracting
class FirstInput(SimpleCalculator):
    def __init__(self,newString, current, userInput,total,operator):
        print("\nFIRST INPUT STATE")
        length = len(newString)
        
        #check for end of string then change states to EOF
        if length == 1:
            self.setState(EndOfFile(newString,current,userInput,total,operator))

        else:
            # string has leading character removed every iteration
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

# program always begins here, and check for the first digit in the file
# if it's not a digit 1-9 it errors out
class InitialState(SimpleCalculator):
    
    def __init__(self):
        SimpleCalculator.__init__(self)
        # store the input file
        newString = dataFile.readlines()
        # remove the list and convert to string
        newString = ' '.join(str(e) for e in newString)
        # remove all whitespace (not a feature we made in diagram)
        # "".join(newString.split())

        userInput = newString[0]
        current = userInput
        operator = "+"
        print(userInput)

        print("\nINITIAL STATE")

        if userInput.isdigit() and int(userInput) in range(1,10):
            printInput(userInput)
            printCurrentCharacter(current)
            self.setState(FirstInput(newString, current, userInput,total,operator))
            
        else:
            # go to error state and give an error code for initital state
            self.setState(Error())
            self.changeStateError(errorOne)
    
    def changeState(self):
        pass

if __name__ == "__main__":
    InitialState()
    
