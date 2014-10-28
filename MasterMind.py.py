
################################### SETUP ###########################################################

from random import randint
import time

def d6():
    return randint(1,6)


guessoptions = {
    1 : "Red",
    2 : "Green",
    3 : "Blue",
    4 : "Black",
    5 : "White",
    6 : "Yellow"
    }
########

class codecreator(object):
    def __init__(self):
        self.name = 123
        self.winner = False
        self.placeholder = []
        self.guess = []
        self.answer = []
        self.answercount = {
            "Red" : 0,
            "Green" : 0,
            "Blue" : 0,
            "Black" : 0,
            "White" : 0,
            "Yellow" : 0
            }
        self.guesscount = {
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
        self.guess = []
        self.answercount = {
            "Red" : 0,
            "Green" : 0,
            "Blue" : 0,
            "Black" : 0,
            "White" : 0,
            "Yellow" : 0
            }
        self.guesscount = {
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
        ##have to reset the tally first or you will miscount when called
        ## multiple times.
        self.answercount = {
            "Red" : 0,
            "Green" : 0,
            "Blue" : 0,
            "Black" : 0,
            "White" : 0,
            "Yellow" : 0
            }
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

    def guesstally(self):
        ##have to reset the tally first or you will miscount when called
        ## multiple times.
        self.guesscount = {
            "Red" : 0,
            "Green" : 0,
            "Blue" : 0,
            "Black" : 0,
            "White" : 0,
            "Yellow" : 0
            }
        ### ANSWERFINAL is the completed guess variable ####
        for each in self.answerfinal:
            if each == "Red":
                #print (self.answercount["Red"])
                self.guesscount["Red"] +=1
                #print (self.answercount["Red"], "debug")
            elif each == "Green":
                self.guesscount["Green"] +=1
            elif each == "Blue":
                self.guesscount["Blue"] +=1
            elif each == "Black":
                self.guesscount["Black"] +=1
            elif each == "White":
                self.guesscount["White"] +=1
            elif each == "Yellow":
                self.guesscount["Yellow"] +=1


    def guessing(self):
        answerguess = []
        answerfinal = []
        userinput = []
        while len(answerguess) < 4:
            validinput = True
            while validinput == True and len(answerguess)<4:
                userinput =raw_input("Your Guess options are:  1= Red, 2 = Green, 3= Blue, 4 = Black, 5 = White, 6 = Yellow :")
                ## use raw_input instead of input() http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
                print ("user guess  =", userinput)
                if userinput == "1" or userinput == "2" or userinput == "3" or userinput == "4" or userinput == "5" or userinput == "6":
                    answerguess.append(int(userinput))
                    print (answerguess)
                else:
                    print ("\nInvalid input. Please use numbers 1 to 6.")
                    validinput = False
        self.answerfinal = [ guessoptions[answerguess[0]], guessoptions[answerguess[1]], guessoptions[answerguess[2]], guessoptions[answerguess[3]] ]
        

    def wincheck(self):
        self.winner = False
        colorpeg = []
        if self.answerfinal == self.answer:
            print ("youwon", self.answerfinal, self.answer)
            self.winner = True
            return
        ### only tally EXACT MATCHES FIRST then decriment  answercount and guesscount accordingly
        ### the removal of answer count tally and guess count tally is necessary to compute color matches that aren't exact.
        ##
        #print ( "Before computation ran the tally of answer is :", self.answercount, "\n     and the tally of guess is ", self.guesscount)
        ##
        ### Check for EXACT MATCHES. remove from count tally so they arent double counted as ###
        if self.answerfinal[0] == self.answer[0]:
            self.answercount[self.answerfinal[0]] -= 1
            self.guesscount[self.answerfinal[0]] -= 1
            colorpeg.append("Black")
        if self.answerfinal[1] == self.answer[1]:
            self.answercount[self.answerfinal[1]] -= 1
            self.guesscount[self.answerfinal[1]] -= 1
            colorpeg.append("Black")
        if self.answerfinal[2] == self.answer[2]:
            self.answercount[self.answerfinal[2]] -= 1
            self.guesscount[self.answerfinal[2]] -= 1
            colorpeg.append("Black")
        if self.answerfinal[3] == self.answer[3]:
            self.answercount[self.answerfinal[3]] -= 1
            self.guesscount[self.answerfinal[3]] -= 1
            colorpeg.append("Black")

        ### Check for color specific matches

            ###Just loop through
        colorlooping = ["Red", "Green", "Blue", "Black", "White", "Yellow"]
        for each in colorlooping:
            if self.answercount[each] > 0 and self.answercount[each] == self.guesscount[each]:
                while self.answercount[each] > 0:
                    colorpeg.append("White")
                    self.answercount[each] -= 1
            elif self.answercount[each] > self.guesscount[each]:
                while self.guesscount[each] > 0:
                    colorpeg.append("White")
                    self.guesscount[each] -= 1
            elif self.answercount[each] > 0 and self.answercount[each] < self.guesscount[each]:
                while self.answercount[each] > 0:
                    colorpeg.append("White")
                    self.answercount[each] -= 1            
            
        ########  I think there is a count bug in here somewhere ##
        print ("the matches are\n: ", colorpeg, "\n\n")

### Guessing code ###

              
#####################

secret_code = codecreator()
secret_code.random_code()

trycount = 10
while trycount >0 and secret_code.winner == False:
    secret_code.guessing()
    secret_code.tally()
    secret_code.guesstally()
    secret_code.wincheck()
    trycount -= 1
    
    
    
  
#----------------------------------------------------------------------------------
            
################################### SETUP END ###########################################################

#----------------------------------------------------------------------

