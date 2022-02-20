from tkinter.tix import InputOnly
import unicodedata
from xml.sax.xmlreader import InputSource
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
# results = db.collection("Letters").document("blah").get()
# print(results.to_dict())


# Creates a dictionary
table = dict()
results = db.collection("Letters").get()
for result in results:
    key = result.id
    value = (result.to_dict())["Cirth"]
    table[key] = value

# Prints a key for all english letter's and their Cirth Counterparts
def print_key():
    print('\na = \u16A2\tb = \u16B1\tch = \u16B3')
    print('d = \u16A8\te = \u16BA\tee = \u16BB')
    print('f = \u16E9\tg = \u16A0\th = \u16E6')
    print('i = \u16C1\tj = \u16AD\tk = \u16B4')
    print('l = \u16C5\tm = \u16D2\tn = \u16C9')
    print('o = \u16A3\tp = \u16B9\tqu = \u16A9')
    print('r = \u16CF\ts = \u16B2\tt = \u16DA')
    print('u = \u16DF\tuu = \u16DD\tv = \u16D5')
    print('w = \u16C4\ty = \u16CB\tz = \u16E3')

    print('\nand = \u16C7Modifying h = \u16E7')
    print('ou = \u16DE\tnd = \u16EF\tth = \u16D0')
    print('oo = \u16A4\tng = \u16B7')
    print('space = \u16EB\tpunctuation = \u16EC\tSilent e = \u16BF\n')
    print('Warning, this key is not 100% accurate to Cirth. The symbols used are from the Runic Unicode ', end = '')
    print('Library, which does not always have the perfect character. So the symbol that looked the closest is used.\n')

# Simply displays a series of strings, first in english, then in Cirth/Dwarvish
def display_example():
    print('\nbalin\nfundinul\nuzbad khazadduumu\nbalin son ov fundin lord ov moria\n')
    print('\u16EB\u16B1\u16A2\u16C5\u16C1\u16C9\u16EB')
    print('\u16EB\u16E9\u16DF\u16EF\u16C1\u16C9\u16DF\u16C5\u16EB')
    print('\u16EB\u16DF\u16E3\u16B1\u16A2\u16A8\u16EB\u16B4\u16E7\u16A2\u16E3\u16A2\u16A8\u16A8\u16DD\u16D2\u16DF\u16EB')
    print('\u16EB\u16B1\u16A2\u16C5\u16C1\u16C9\u16EB', end = '')
    print('\u16B2\u16A3\u16C9\u16EB\u16A3\u16B7\u16EB\u16E9\u16DF\u16EF\u16C1\u16C9\u16EB', end = '')
    print('\u16C5\u16A3\u16CF\u16A8\u16EB\u16A3\u16B7\u16EB\u16D2\u16A3\u16CF\u16C1\u16A2\u16EC\n')
    cirth_library = db.collection("Letters").get()
    # print(cirth_library, "\n")

# Prompts specifically for the User input for conversion of a string
def prompt_input():
    print("\nWhat text would you like to convert?\n > ", end = "")
    text = input()
    print("")
    return text


# This function handles the long, complicated process of Converting a user-given string into dwarvish
def convert_text(text):
    #Convert to all uppercase
    text = text.upper()
    cirth = ["\u16EB"]
    # db.collection("Letters").document("OO")
    i = 0
    while i < len(text):
        # checks for a
        if text[i] == "A":
            #checks for the word and, making sure it's not part of a word and is on it's own
            if i == 0 or text[i-1] == " ":
                if text[i+1] == "N" and text[i+2] == "D":
                    if len(text) - 1 == (i+2):
                        cirth.append(table["AND"])
                        i += 2
                    elif [text[i+3] == " " or text[i+3] == "!" or text[i+3] == "." 
                        or text[i+3] == "?" or text[i+3] == ","]:
                        cirth.append(table["AND"])
                        i += 2
            # defaults to regular A
            else:
                cirth.append(table["A"])
        elif text[i] =="B":
            cirth.append(table["B"])
        elif text[i] =="C":
            # Checks if C is last in string
            if len(text) - 1 == (i+1):
                cirth.append(table["K"])
            #checks for CH
            elif text[i+1] == "H":
                cirth.append(table["CH"])
            # checks if it makes a s sound
            elif text[i+1] == "I" or text[i+1] == "E" or text[i+1] == "Y":
                cirth.append(table["S"])
            #defaults to k(no c in language)
            else: 
                cirth.append(table["K"])
        elif text[i] =="D":
            cirth.append(table["D"])
        elif text[i] =="E":
            #if e is at the end of a word, it's silent
            if len(text) - 1 == (i):
                cirth.append(table["Silent E"])
            elif text[i+1] == " ":
                cirth.append(table["Silent E"])
            # seperate character for EE
            elif text[i+1] == "E":
                cirth.append(table["EE"])
                i += 1
            #defaults to regular E
            else:
                cirth.append(table["E"])        
        elif text[i] =="F":
            cirth.append(table["F"])
        elif text[i] =="G":
            cirth.append(table["G"])
        elif text[i] =="H":
            # Chacks if the h is at the beginning of the string
            if i == 0:
                cirth.append(table["H"])
            # Modifier H only comes after consenants, so checks that it isn't after a vowel or space
            elif (text[i-1] == "B" or text[i-1] == "D" or text[i-1] == "F" or text[i-1] == "G" or text[i-1] == "J" 
                  or text[i-1] == "K" or text[i-1] == "L" or text[i-1] == "M" or text[i-1] == "N"or text[i-1] ==  "P"
                  or text[i-1] ==  "Q" or text[i-1] == "R" or text[i-1] == "S" or text[i-1] == "V" or text[i-1] == "W"
                  or text[i-1] == "X" or text[i-1] == "Z"):
                cirth.append(table["H Mod"])
            # defaults to regular H
            else:
                cirth.append(table["H"])
        elif text[i] =="I":
            cirth.append(table["I"])
        elif text[i] =="J":
            cirth.append(table["J"])
        elif text[i] =="K":
            cirth.append(table["K"])
        elif text[i] =="L":
            cirth.append(table["L"])
        elif text[i] =="M":
            cirth.append(table["M"])
        elif text[i] =="N":
            # Checks if N is at the end of a string
            if len(text) - 1 == (i+1):
                cirth.append(table["N"])
            # ND Symbol    
            elif text[i+1] == "D":
                cirth.append(table["ND"])
                i += 1
            # Checks for NG
            elif text[i+1] == "G":
                cirth.append(table["NG"])
                i += 1
            # defaults to N
            else: 
                cirth.append(table["N"])
        elif text[i] =="O":
            # Checks if O is at the end
            if len(text) - 1 == (i+1):
                cirth.append(table["O"])
            # OO?    
            elif text[i+1] == "OO":
                cirth.append(table["OO"])
                i += 1
            # OU?
            elif text[i+1] == "U":
                cirth.append(table["OU"])
                i += 1
            # Defaults to O
            else: 
                cirth.append(table["O"])
        elif text[i] =="P":
            cirth.append(table["P"])
        elif text[i] =="Q":
            # Checks if the Q is at the end of the string
            if len(text) - 1 == (i+1):
                cirth.append(table["QU"])
            #JUST FOR RECOGNIZING IF THERES A U AFTER OR NOT TO SKIP FOR THE LOOP   
            elif text[i+1] == "U":
                i += 1
            else:
                cirth.append(table["QU"])
        elif text[i] =="R":
            cirth.append(table["R"])
        elif text[i] =="S":
            cirth.append(table["S"])
        elif text[i] =="T":
            # Checks if T is at the end of the string
            if len(text) == (i+1):
                cirth.append(table["T"])
            # TH?    
            elif text[i+1] == "H":
                cirth.append(table["TH"])
                i += 1
            # Defaults to T
            else:
                cirth.append(table["T"])
        elif text[i] =="U":
            # Checks if U is at the end of the string
            if len(text) - 1 == (i+1):
                cirth.append(table["U"])
            # UU?    
            elif text[i+1] == "U":
                cirth.append(table["UU"])
                i += 1
            # defaults to U
            else:
                cirth.append(table["U"])
        elif text[i] =="V":
            cirth.append(table["V"])
        elif text[i] =="W":
            cirth.append(table["W"])
        elif text[i] == "X":
            #X makes Z sound at the beginning of a word ---UNLESS IT'S ON IT"S OWN--- FIX THAT
            if text[i-1] == " " or i == 0:
                cirth.append(table["Z"])
            # Default: There is no X, so replaces with KS for similar sound
            else:
                cirth.append(table["K"])
                cirth.append(table["S"])
        elif text[i] =="Y":
            cirth.append(table["Y"])
        elif text[i] =="Z":
            cirth.append(table["Z"])
        elif text[i] ==" ":
            cirth.append(table["Space"])
        elif text[i] =="." or text[i] =="," or text[i] =="!" or text[i] =="?":
            cirth.append(table["Punctuation"])
            # Checks if punctuation is at the end, so no error happens when checking for a space
            if len(text) - 1 == i:
                break
            # skips the space that often comes after the punctuation
            elif text[i+ 1] == " ":
                i += 1
        else:
            # if symbol doesn't exist, gives a filler symbol
            cirth.append("_")
        i += 1
    punctuation = table["Punctuation"]
    space = table["Space"]
    end = cirth[len(cirth) - 1]
    if end == punctuation or end == space:
        return cirth
    else:
        cirth.append("\u16EC")
        return cirth
        
# Prints converted Text
def print_text(finished_text):
    for letter in finished_text:
        print(letter, end = "")
    print("\n")

# Prompts user for a letter to add and the special unicode associated with it, then adds it to the database
def add_character():
    doc = input("What letter does the character represent? > ")
    character = input("What is the unicode for the character > ")
    new = {"Cirth" : character}
    success = db.collection("Letters").document(doc).set(new)
    if success:
        # downloaded database needs to be updated
        results = db.collection("Letters").get()
        for result in results:
            key = result.id
            value = (result.to_dict())["Cirth"]
            table[key] = value
        print(table[doc])
        print("Character added successfully! Database Updated\n")
    else:
        print("Error: unable to add Character")

# Prompts user for a character in the database to alter, it's new unicode, and then updates it.
def update_character():
    doc = input("What letter character are you wanting to update? > ")
    character = input("What is the unicode for the character > ")
    try :
        db.collection("Letters").document(doc).update({"Cirth" : character})
        # downloaded database needs to be updated
        results = db.collection("Letters").get()
        for result in results:
            key = result.id
            value = (result.to_dict())["Cirth"]
            table[key] = value
        print("Character updated successfully! Database Updated!\n")
    except :
        print("Error! Either Character Does not exist or some other Error was given!\n")

def delete_character():
    doc = input("What letter character are you wanting to delete? > ")
    success = db.collection("Letters").document(doc).delete()
    if success:
        # downloaded database needs to be updated
        results = db.collection("Letters").get()
        for result in results:
            key = result.id
            value = (result.to_dict())["Cirth"]
            table[key] = value
        print("Character Deleted successfully! Database Updated!\n")

# Main menu, displays the options and get's the users input
def menu():
    print("NOTE: Option 4 and 5 do not add the printable unicode to the database.")
    print("\tOption 4 creates the document with the Cirth Unicode, and Option 5 saves the code too.")
    print("\tAny characters added through those options will need to be manually updated later.")
    print("<Option 1> Display the Key.")
    print("<Option 2> Display Example Text.")
    print("<Option 3> Convert Text.")
    print("<Option 4> Add Character.")
    print("<Option 5> Update Character.")
    print("<Option 6> Delete Character.")
    print("<Option 7> Quit.\n")

    print("<Type # here> ", end = "")
    option = input()
    return option

# Where the menu options are processed- calls correct series of functions for whichever option the user chose
def interface(option):
    if option == "1":
        print_key()
    elif option == "2":
        display_example()
    elif option == "3":
        text = prompt_input()
        finished_text = convert_text(text)
        print_text(finished_text)
    elif option == "4":
        add_character()
    elif option == "5":
        update_character()
    elif option == "6":
        delete_character()
    elif option == "7":
        return False
    else:
        print("None existant option Please try again.")
    return True

# Main, calls menu and interface until user quits.
play = True
while play:
    option = menu()
    play = interface(option)
print('\nThanks for playing!\n')

