#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

def displayIntro():
    print("Topic:  TEXT-Based Adventure Game")
    print("Python is an interpreted, high-level, general-purpose programming language.")
    print("Python is considered a scripting language.")
    
    
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an asteroid nearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But your skin begins to tingle...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That tingling was just the feeling of admiration from the citizens of the galaxy!")
        print("Welcome home!")
    else:
        print("An extremely energetic burst of gamma rays pass through you")
        print("causing all of the atoms in your body to dissociate")
        print("there is no record left of your existence.")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")


# In[ ]:




