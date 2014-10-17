
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
        

    def random_code(self):
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
        
    def custom_code(self):
        self.codereset()
        customguess = []
        userinput = []
        while len(customguess) < 4:
            validinput = True
            while validinput == True and len(customguess)<4:
                userinput =raw_input(" 1= Red, 2 = Green, 3= Blue, 4 = Black, 5 = White, 6 = Yellow :")
                ## use raw_input instead of input() http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
                print ("userinput =", userinput)
                if userinput == "1" or userinput == "2" or userinput == "3" or userinput == "4" or userinput == "5" or userinput == "6":
                    customguess.append(int(userinput))
                    print (customguess)
                else:
                    print ("\nInvalid input. Please use numbers 1 to 6.")
                    validinput = False
        self.answer = [ guessoptions[customguess[0]], guessoptions[customguess[1]], guessoptions[customguess[2]], guessoptions[customguess[3]] ]

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
secret_code.random_code()
print (secret_code.answer)
secret_code.random_code()
print (secret_code.answer)

secret_code.tally()
secret_code.custom_code()
secret_code.tally()
print (secret_code.answer)
print (secret_code.answercount)
                

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

