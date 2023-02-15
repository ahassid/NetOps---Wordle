import Printer

class Game:
    
    @staticmethod
    def compare(str_a, str_b):
        y = 0
        Answer = ""
        for g in str_a:
            x = 0
            flag = False
            flag2 = False
            for e in str_b:
                if g == e or abs(ord(g) - ord(e)) == 32:
                    flag = True
                    if x == y:
                        flag2 = True
                        Answer += "T"
                        break
                        
                x+=1
            if flag == False:
                Answer += "F"
            elif flag2 == False:
                Answer += "P"
            y+=1   
    
        return Answer

    @staticmethod
    def compareV2(str_a, str_b):
        
        AlphaBetaArr =  [False for i in range(26)]
        for i in str_b:
            AlphaBetaArr[ord(i) - ord('a')] = True
        y = 0
        Answer = ""
        for g in str_a:
            if(AlphaBetaArr[ord(g)-ord('a')]):
                if(g == str_b[y]):
                    Answer += "T"
                else:
                    Answer += "P"
            else:
                Answer += "F"
            y+=1   
    
        return Answer

    @staticmethod
    def Validate(str_a):
        if len(str_a) != 5 or str_a.isalpha() != True:
            return False
        return True    
    
    def startGame(MJ, realWord, color):
        
        i = 0
        while i < 5:
            
            Guess = input("Enter your guess: ")
            check = MJ.Validate(Guess)
            if check == True:
                i += 1
                NewAnswer = MJ.compareV2(Guess, realWord)
                Printer.S_Print (Guess, NewAnswer, color)
                if NewAnswer == "TTTTT":
                    print ("Mission Accomplished! ")
                    break
            else:
                print ("There Was A Problem With Your Guess, It Doesn't Count - Please Try Again")
            
        if i == 5:    
            print ("You Are A Loser !")
        
        while True:
            try:
                _return = input ("Enter 1 If You Want Replay, Else Enter 0: ")
                return int(_return)
            except ValueError:
                    print("Sorry ! You Entered An Inappropriate Value ")

         
