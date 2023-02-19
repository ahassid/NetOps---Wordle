from Printer import Printer

class Game:
    
    def __init__(self, wordsDBName):
        self.p = Printer()
        self.arrayOfWords = []
        wordsDB = open(wordsDBName, "r")
        for f in wordsDB:
            f = f.removesuffix('\n')
            if self.Validate(f):
                self.arrayOfWords.append(f)

    def Compare(self, str_a, str_b):
        
        isLetterExistsArr =  [False for i in range(26)]
        howManyTimeLetterExistsArr =  [0 for i in range(26)]
       
        for i in str_b:
            isLetterExistsArr[ord(i) - ord('a')] = True
            howManyTimeLetterExistsArr[ord(i) - ord('a')] += 1

        y = 0
        answer = [' ' for i in range(len(str_a))]
        for g in str_a:
            if(isLetterExistsArr[ord(g)-ord('a')]):
                if(g == str_b[y]):
                    answer[y] = "T"
                    howManyTimeLetterExistsArr[ord(g) - ord('a')] -= 1
            y+=1
        y = 0    
        for g in str_a:
            if(answer[y] != "T"):
                if(isLetterExistsArr[ord(g)-ord('a')] and howManyTimeLetterExistsArr[ord(g)-ord('a')] > 0):
                    answer[y] = "P"
                    howManyTimeLetterExistsArr[ord(g) - ord('a')] -= 1
                else:    
                    answer[y] = "F"
            y+=1   
        
        answer = ''.join([str(elem) for elem in answer])
        return answer

    def Validate(self, str_a):
        if len(str_a) != 5 or not str_a.isalpha() or not str_a.isascii():
            return False
        return True  

    def StartGame(self, realWord, color):
    
        resultsFile = open("Results.txt", "a")
        amountOfGames += 1
        i = 0
        while i < 5:
            guess = input("Enter your guess: ").lower()
            checkGuess = self.Validate(guess)
            if checkGuess == True:
                i += 1
                newAnswer = self.Compare(guess, realWord)
                self.p.ColourfulPrint(guess, newAnswer, color)
                if newAnswer == "TTTTT":
                    #resultsFile.write("Well Done - You Completed The Mission On Try Number " + str(i + 1) + "\n")
                    resultsFile.write(str(i + 1) + "\n")
                    resultsFile.close()
                    print ("Mission Accomplished! ")
                    break 
            else:
                print ("There Was A Problem With Your Guess, It Doesn't Count - Please Try Again")
            
        if newAnswer != "TTTTT":  
            #resultsFile.write("Too Bad - You Failed, Maybe You Will Do Better Next Time\n")
            resultsFile.write(str(0) + "\n")
            resultsFile.close()
            print ("You Are A Loser !")
        
        while True:
            try:
                _return = input ("Enter 1 If You Want Replay, Else Enter 0: ")
                return int(_return)
            except ValueError:
                    print("Sorry ! You Entered An Inappropriate Value ")

       
         
