
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
        self.answercount = {
            "Red" : 0,
            "Green" : 0,
            "Blue" : 0,
            "Black" : 0,
            "White" : 0,
            "Yellow" : 0
            }
        

    def newcode(self):
        self.answer = [ guessoptions[d6()],guessoptions[d6()],guessoptions[d6()],guessoptions[d6()] ]
        
    def codereset(self):
        self.answer = []
        self.answercount = {
            "Red" : 0,
            "Green" : 0,
            "Blue" : 0,
            "Black" : 0,
            "White" : 0,
            "Yellow" : 0
            }
        
    def customcode(self):
        validinput = 0
        while len(self.answer) < 4:
            userinput = int(input(" 1= Red, 2 = Green, 3= Blue, 4 = Black, 5 = White, 6 = Yellow :"))
            self.answer.append(guessoptions[userinput])

    def tally(self):
        for each in self.answer:
            if each == "Red":
                #print (self.answercount["Red"])
                self.answercount["Red"] +=1
                #print (self.answercount["Red"], "debug")
            elif each == "Green":
                self.answercount["Green"] +=1
            elif each == "Blue":
                self.answercount["Blue"] +=1
            elif each == "Black":
                self.answercount["Black"] +=1
            elif each == "White":
                self.answercount["White"] +=1
            elif each == "Yellow":
                self.answercount["Yellow"] +=1

        
    

##secret_code = [ guessoptions[d6()],guessoptions[d6()],guessoptions[d6()],guessoptions[d6()] ]


secret_code = codecreator()

print (secret_code.answer)
secret_code.newcode()
print (secret_code.answer)
secret_code.newcode()
print (secret_code.answer)

secret_code.tally()
secret_code.codereset()
secret_code.customcode()
secret_code.tally()
print ("New secret code is ", secret_code.answer, "the tally is ", secret_code.answercount)


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

