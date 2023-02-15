import Printer
import random
import Game

wordsArray = ["hello", "crate", "shade", "resin", "alert", "media", "flood", "award", "bully", "orate", "legal", "boost"]
G = Game.Game()

while True:
    realWord = wordsArray [random.randint(0, 11)]
    print ("The Real Word is: " + realWord)
    
    try:
        color = input ("Enter 1 if you want colors in your game, Else enter 0: ")
        if G.startGame(realWord, int(color)) == 0:
            break
    except ValueError:
        print("Sorry ! You Entered An Inappropriate Value ")
                    
    
