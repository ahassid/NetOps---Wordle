import Bcolors

class Printer:
      word = ""
      
def S_Print(word, result ,_type):
    bc = Bcolors.Bcolors()
    i = 0
    _str = ""
    
    if _type == 1:
        while i < 5:
            for r in result:
                if r == "F":
                    _str += bc.RED + word[i]
                elif r == "T":
                    _str += bc.GREEN + word[i]
                else:
                    _str += bc.YELLOW + word[i]
                i += 1
        print (_str + bc.WHITE)        
    else:    
        print (result)
  
