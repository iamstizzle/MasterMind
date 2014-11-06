#---------------------------------------
############# SETUP ####################
#---------------------------------------

from random import randint
import time
import random

def d6():
    return randint(1,6)

def shuffle(x):
    x = list(x)
    random.shuffle(x)
    return x

guessoptions = {
    1 : "Red",
    2 : "Green",
    3 : "Blue",
    4 : "Black",
    5 : "White",
    6 : "Yellow"
    }

#####----Class ---- #######

class codecreator(object):
    def __init__(self):
        self.winner = False
        self.guess = []
        self.answer = []
        self.colorpeg = []
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


    def random_code(self):
        self.answer = [ guessoptions[d6()],guessoptions[d6()],guessoptions[d6()],guessoptions[d6()] ]
        
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



    def guessing(self):
        answerguess = []
        answerfinal = []
        userinput = []
        while len(answerguess) < 4:
            validinput = True
            while validinput == True and len(answerguess)<4:
                if len(answerguess)==0:
                    print ("Your Guess options are:  1= Red, 2 = Green, 3= Blue, 4 = Black, 5 = White, 6 = Yellow ")
                userinput =raw_input("Peg %s choice: " % (len(answerguess)+1) )
                ## use raw_input instead of input() http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
                #print ("user guess  =", userinput)
                if userinput == "1" or userinput == "2" or userinput == "3" or userinput == "4" or userinput == "5" or userinput == "6":
                    answerguess.append(int(userinput))
                    print (answerguess)
                else:
                    print ("\nInvalid input. Please use numbers 1 to 6.")
                    validinput = False
        self.answerfinal = [ guessoptions[answerguess[0]], guessoptions[answerguess[1]], guessoptions[answerguess[2]], guessoptions[answerguess[3]] ]


    def tally(self):
        ##have to reset the tally first or you will miscount when called again
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
        ##have to reset the tally first or you will miscount if called again.
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
                self.guesscount["Red"] +=1
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


    """def guessing(self):
        answerguess = []
        answerfinal = []
        userinput = []
        while len(answerguess) < 4:
            validinput = True
            while validinput == True and len(answerguess)<4:
                userinput =raw_input("Your Guess options are:\n1= Red, 2 = Green, 3= Blue, 4 = Black, 5 = White, 6 = Yellow\nPlease enter a number: ")
                ## use raw_input instead of input() http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
                #print ("user guess  =", userinput)
                if userinput == "1" or userinput == "2" or userinput == "3" or userinput == "4" or userinput == "5" or userinput == "6":
                    answerguess.append(int(userinput))
                    print (answerguess)
                else:
                    print ("\nInvalid input. Please use numbers 1 to 6.")
                    validinput = False
        # Now convert those stored values into the actual guess
        self.answerfinal = [ guessoptions[answerguess[0]], guessoptions[answerguess[1]], guessoptions[answerguess[2]], guessoptions[answerguess[3]] ]
        print(self.answerfinal)"""

    def wincheck(self):
        self.winner = False
        self.colorpeg = []
        ## Win if it is a match!!!
        if self.answerfinal == self.answer:
            #print ("A Winner is YOU! All your BASE! etc...", self.answerfinal, self.answer)
            self.winner = True
            self.colorpeg = ["Black", "Black", "Black", "Black"]
            return
        
        ### Count EXACT matches first
        ### Then Decrement matches out of the tally, so you dont double count them.
        if self.answerfinal[0] == self.answer[0]:
            self.answercount[self.answerfinal[0]] -= 1
            self.guesscount[self.answerfinal[0]] -= 1
            self.colorpeg.append("Black")
        if self.answerfinal[1] == self.answer[1]:
            self.answercount[self.answerfinal[1]] -= 1
            self.guesscount[self.answerfinal[1]] -= 1
            self.colorpeg.append("Black")
        if self.answerfinal[2] == self.answer[2]:
            self.answercount[self.answerfinal[2]] -= 1
            self.guesscount[self.answerfinal[2]] -= 1
            self.colorpeg.append("Black")
        if self.answerfinal[3] == self.answer[3]:
            self.answercount[self.answerfinal[3]] -= 1
            self.guesscount[self.answerfinal[3]] -= 1
            self.colorpeg.append("Black")

        ### Check for Color Matches next
        ### do some logic. Count color matches in incorrect spots.    
        colorlooping = ["Red", "Green", "Blue", "Black", "White", "Yellow"]
        for each in colorlooping:
            if self.answercount[each] > 0 and self.answercount[each] == self.guesscount[each]:
                while self.answercount[each] > 0:
                    self.colorpeg.append("White")
                    self.answercount[each] -= 1
            elif self.answercount[each] > self.guesscount[each]:
                while self.guesscount[each] > 0:
                    self.colorpeg.append("White")
                    self.guesscount[each] -= 1
            elif self.answercount[each] > 0 and self.answercount[each] < self.guesscount[each]:
                while self.answercount[each] > 0:
                    self.colorpeg.append("White")
                    self.answercount[each] -= 1            
            
        #Shuffle isn't actually necessary. just use self.colorpeg. Since the order is always Exact first then color matches, the order can't be reverse engineered.
        shuffleclues = shuffle(self.colorpeg)
        print ("--------------------------------")
        print ("Your Hints are :", self.colorpeg )

#----------------------------------------------            
############## SETUP END ######################
#----------------------------------------------
              
########

secret_code = codecreator()
secret_code.random_code()
previousguesshint = []
trycount = 10

while trycount >0 and secret_code.winner == False:
    secret_code.guessing()
    secret_code.tally()
    secret_code.guesstally()
    secret_code.wincheck()
    trycount -= 1
    previousguesshint.append((secret_code.answerfinal, secret_code.colorpeg, trycount) )
    print ("\n------------------------------\nYour previous guesses and hints were:")
    for each in previousguesshint:
        print ("Guess #%s: %s  matches:: %s" % ((10 - each[2]), each[0], each[1]) )
    time.sleep(1)
    if secret_code.winner == False:
        print ("\nYou have %s attempts remaining." %trycount)
    if trycount ==4:
        time.sleep(1)
        print ("\n-----------\nPRO TIP: You often get more information by confirming incorrect guesses than you do with correct ones.\n-----------\n")
        time.sleep(3)


time.sleep(2)
if secret_code.winner == True:
    print ("Congratulations")
    print ("A Winner is YOU! All your BASE! etc...\nYou guessed the answer %s" % secret_code.answer)
elif secret_code.winner == False:
    print ("Sorry you suck so bad at this. Goodbye.")
time.sleep(3)
    
#########  
    


