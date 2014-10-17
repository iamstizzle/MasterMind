def custom_code():
    customguess = []
    while len(customguess) < 4:
        validinput = True
        while validinput == True and len(customguess)<4:
            userinput = raw_input(" 1= Red, 2 = Green, 3= Blue, 4 = Black, 5 = White, 6 = Yellow :")
            print ("userinput =", userinput)
            if userinput == "1" or "2" or "3" or "4" or "5" or "6":
                customguess.append(userinput)
                print (customguess)
            else:
                print ("\nInvalid input. Please use numbers 1 to 6.")
                validinput = False
sdfadsfsadf ="asdfasdf"


userinput = 1
custom_code()



### raw_input   http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
