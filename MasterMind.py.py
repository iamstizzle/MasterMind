
################################### SETUP ###########################################################

from random import randint
import time

def d6():
    return randint(1,6)

### DICE TABLES ####
guessoptions = {
    1 : "Red",
    2 : "Green",
    3 : "Blue",
    4 : "Black",
    5 : "White",
    6 : "Yellow"
    }


class codecreator(object):
    def __init__(self):
        self.name = 123
        self.placeholder = []
        self.answer = []
        

    def newcode(self):
        self.answer = [ guessoptions[d6()],guessoptions[d6()],guessoptions[d6()],guessoptions[d6()] ]

    def tally(self):
        for each in self.answer:
            print (each)

    

##secret_code = [ guessoptions[d6()],guessoptions[d6()],guessoptions[d6()],guessoptions[d6()] ]


secret_code = codecreator()

print (secret_code.answer)
secret_code.newcode()
print (secret_code.answer)
secret_code.newcode()
print (secret_code.answer)

secret_code.tally()


#####################

class playerfuction(object):
    def __init__(self):
        self.name = "Player 1"
        self.guess = []

    def guesscheck(self):
        for each in self.guess:
            print ("hello")
            
        
        
    def scorecheck(self):
        pass

  
#----------------------------------------------------------------------------------
            
################################### SETUP END ###########################################################

#----------------------------------------------------------------------

