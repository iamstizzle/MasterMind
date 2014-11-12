#---------------------------------------
############# SETUP ####################
#---------------------------------------

from random import randint
import time
import random

def d6():
    return randint(1,6)

def shuffle(x):
    return random.shuffle(list(x))

colors = [ "Red", "Green", "Blue", "Black", "White", "Yellow" ]

guessoptions = dict(zip(range(1, 7), colors))

#####----Class ---- #######

class codecreator(object):
    def __init__(self):
        self.winner = False
        self.guess = []
        self.answer = []
        self.colorpeg = []
        self.answercount = dict([(x, 0) for x in colors])
        self.guesscount = dict([(x, 0) for x in colors])


    # May not need this as we can just create a new object
    # and use the initializer to set these values
    def codereset(self):
        self.answer = []
        self.guess = []
        self.answercount = dict([(x, 0) for x in colors])
        self.guesscount = dict([(x, 0) for x in colors])


    # We probably shouldn't have to zero out these -- we should be able to
    # create a new object instead
    def zero_out_dict(self, d):
        for k in d.keys():
            d[k] = 0

    def random_code(self):
        self.answer = [ guessoptions[d6()] for x in range(4) ]

    def custom_code(self):
        self.codereset()
        customguess = []
        userinput = []
        while len(customguess) < 4:
            validinput = True
            while validinput and len(customguess)<4:
                userinput =raw_input(" 1= Red, 2 = Green, 3= Blue, 4 = Black, 5 = White, 6 = Yellow :")
                ## use raw_input instead of input() http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
                print ("userinput =", userinput)
                try:
                    userinput = int(userinput)
                except ValueError:
                    print ("\nInvalid input. Please use numbers 1 to 6.")
                    validinput = False
                if userinput in range(1, 7):
                    customguess.append(int(userinput))
                    print (customguess)
                else:
                    print ("\nInvalid input. Please use numbers 1 to 6.")
                    validinput = False
        self.answer = [ guessoptions[customguess[x]] for x in range(4)]



    def guessing(self):
        answerguess = []
        answerfinal = []
        userinput = []
        while len(answerguess) < 4:
            validinput = True
            while validinput and len(answerguess)<4:
                if len(answerguess)==0:
                    print ("Your Guess options are:  1= Red, 2 = Green, 3= Blue, 4 = Black, 5 = White, 6 = Yellow ")
                userinput =raw_input("Peg %s choice: " % (len(answerguess)+1) )
                ## use raw_input instead of input() http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
                #print ("user guess  =", userinput)
                try:
                    userinput = int(userinput)
                except ValueError:
                    print ("\nInvalid input. Please use numbers 1 to 6.")
                    validinput = False
                if userinput in range(1, 7):
                    answerguess.append(int(userinput))
                    print (answerguess)
                else:
                    print ("\nInvalid input. Please use numbers 1 to 6.")
                    validinput = False
        self.answerfinal = [ guessoptions[answerguess[x]] for x in range(4)]


    def tally(self):
        ##have to reset the tally first or you will miscount when called again
        self.zero_out_dict(self.answercount)
        for each in self.answer:
            self.answercount[each] += 1

    def guesstally(self):
        ##have to reset the tally first or you will miscount if called again.
        self.zero_out_dict(self.guesscount)
        ### ANSWERFINAL is the completed guess variable ####
        for each in self.answerfinal:
            self.guesscount[each] +=1

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
        for x in range(4):
            if self.answerfinal[x] == self.answer[x]:
                self.answercount[self.answerfinal[x]] -= 1
                self.guesscount[self.answerfinal[x]] -= 1
                self.colorpeg.append("Black")

        ### Check for Color Matches next
        ### do some logic. Count color matches in incorrect spots.
        for each in colors:
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

def main():
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


# Hide the main game functionality in a main() function
# This allows us to import the same code as a module without
# the game executing.  This will be useful for testing functions later.
if __name__ == '__main__':
    main()
