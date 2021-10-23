# Assignment 3 Readme 

Using: 
1. Python version 3.9.7
2. Python interpreter 3.8.2
3. Visual Studio Code extension Python Intellisense


Run with: `$python3 main.py`

Notes about the file structure:

- main.py is the Context
- /States directory holds all of the states
- states are implemented as Singletons(). This is ensured by taking advantage of the __init()__ dunder function in Python that gets run when the class is initialized
- States are created using the factory design pattern