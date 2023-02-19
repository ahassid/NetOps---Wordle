import random
import Game

G = Game.Game("Words.txt")
#wordsArray = ["hello", "crate", "shade", "resin", "alert", "media", "flood", "award", "bully", "orate", "legal", "boost"]

while True:
    
    try:
        color = int(input ("Enter 1 if you want colors in your game, Else enter 0: "))
        chosenWord = G.arrayOfWords [random.randint(0, 11)]
        print ("The Real Word is: " + chosenWord)
        if G.StartGame(chosenWord, int(color)) == 0:
            break
    except ValueError:
        print("Sorry ! You Entered An Inappropriate Value ")
