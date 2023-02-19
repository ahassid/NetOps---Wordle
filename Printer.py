
class Printer:
      
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m' 

    def ColourfulPrint(self, word, result ,_type):
        i = 0
        _str = ""
    
        if _type == 1:
            while i < 5:
                for r in result:
                    if r == "F":
                        _str += self.RED + word[i]
                    elif r == "T":
                        _str += self.GREEN + word[i]
                    else:
                        _str += self.YELLOW + word[i]
                    i += 1
            print (_str + self.WHITE)        
        else:    
            print (result)
  
  
  
