import unicodedata
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
# results = db.collection("Letters").document("blah").get()
# print(results.to_dict())

results = db.collection("Letters").document("A").get()
results.to_dict()["Cirth"]

def print_key():
    print('a = \u16A2\tb = \u16B1\tch = \u16B3')
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

def prompt_input():
    print("\nWhat text would you like to convert?\n > ", end = "")
    text = input()
    print("")
    return text

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
                        results = db.collection("Letters").document("AND").get()
                        cirth.append(results.to_dict()["Cirth"])
                        i += 2
                    elif [text[i+3] == " " or text[i+3] == "!" or text[i+3] == "." 
                        or text[i+3] == "?" or text[i+3] == ","]:
                        results = db.collection("Letters").document("AND").get()
                        cirth.append(results.to_dict()["Cirth"])
                        i += 2
            # defaults to regular A
            else:
                results = db.collection("Letters").document("A").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="B":
            results = db.collection("Letters").document("B").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="C":
            #checks for CH
            if len(text) - 1 == (i+1):
                results = db.collection("Letters").document("K").get()
                cirth.append(results.to_dict()["Cirth"])
            elif text[i+1] == "H":
                results = db.collection("Letters").document("CH").get()
                cirth.append(results.to_dict()["Cirth"])
            # checks if it makes a s sound
            elif text[i+1] == "I" or text[i+1] == "E" or text[i+1] == "Y":
                results = db.collection("Letters").document("S").get()
                cirth.append(results.to_dict()["Cirth"])
            #defaults to k(no c in language)
            else: 
                results = db.collection("Letters").document("K").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="D":
            results = db.collection("Letters").document("D").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="E":
            #if e is at the end of a word, it's silent
            if len(text) - 1 == (i):
                results = db.collection("Letters").document("Silent E").get()
                cirth.append(results.to_dict()["Cirth"])
            elif text[i+1] == " ":
                results = db.collection("Letters").document("Silent E").get()
                cirth.append(results.to_dict()["Cirth"])
            # seperate character for EE
            elif text[i+1] == "E":
                results = db.collection("Letters").document("EE").get()
                cirth.append(results.to_dict()["Cirth"])
                i += 1
            #defaults to regular E
            else:
                results = db.collection("Letters").document("E").get()
                cirth.append(results.to_dict()["Cirth"])        
        elif text[i] =="F":
            results = db.collection("Letters").document("F").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="G":
            results = db.collection("Letters").document("G").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="H":
            # Modifier H only comes after consenants, so checks that it isn't after a vowel or space
            if i == 0:
                results = db.collection("Letters").document("H").get()
                cirth.append(results.to_dict()["Cirth"])
                continue
            if (text[i-1] == "B" or text[i-1] == "D" or text[i-1] == "F" or text[i-1] == "G" or text[i-1] == "J" 
                or text[i-1] == "K" or text[i-1] == "L" or text[i-1] == "M" or text[i-1] == "N"or text[i-1] ==  "P"
                or text[i-1] ==  "Q" or text[i-1] == "R" or text[i-1] == "S" or text[i-1] == "V" or text[i-1] == "W"
                or text[i-1] == "X" or text[i-1] == "Z"):
                results = db.collection("Letters").document("H Mod").get()
                cirth.append(results.to_dict()["Cirth"])
            # defaults to regular H
            else:
                results = db.collection("Letters").document("H").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="I":
            results = db.collection("Letters").document("I").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="J":
            results = db.collection("Letters").document("J").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="K":
            results = db.collection("Letters").document("K").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="L":
            results = db.collection("Letters").document("L").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="M":
            results = db.collection("Letters").document("M").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="N":
            # ND Symbol
            if len(text) - 1 == (i+1):
                results = db.collection("Letters").document("N").get()
                cirth.append(results.to_dict()["Cirth"])
            elif text[i+1] == "D":
                results = db.collection("Letters").document("ND").get()
                cirth.append(results.to_dict()["Cirth"])
                i += 1
            elif text[i+1] == "G":
                results = db.collection("Letters").document("NG").get()
                cirth.append(results.to_dict()["Cirth"])
                i += 1
            #defaults to N
            else: 
                results = db.collection("Letters").document("N").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="O":
            #OO? 
            if len(text) - 1 == (i+1):
                results = db.collection("Letters").document("O").get()
                cirth.append(results.to_dict()["Cirth"])
            elif text[i+1] == "O":
                results = db.collection("Letters").document("OO").get()
                cirth.append(results.to_dict()["Cirth"])
                i += 1
            # OU?
            elif text[i+1] == "U":
                results = db.collection("Letters").document("OU").get()
                cirth.append(results.to_dict()["Cirth"])
                i += 1
            # Defaults to O
            else: 
                results = db.collection("Letters").document("O").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="P":
            results = db.collection("Letters").document("P").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="Q":
            #JUST FOR RECOGNIZING IF THERES A U AFTER OR NOT
            if len(text) - 1 == (i+1):
                results = db.collection("Letters").document("QU").get()
                cirth.append(results.to_dict()["Cirth"])
            elif text[i+1] == "U":
                i += 1
            else:
                results = db.collection("Letters").document("QU").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="R":
            results = db.collection("Letters").document("R").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="S":
            results = db.collection("Letters").document("S").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="T":
            # TH?
            if len(text) - 1 == (i+1):
                results = db.collection("Letters").document("T").get()
                cirth.append(results.to_dict()["Cirth"])
            elif text[i+1] == "H":
                results = db.collection("Letters").document("TH").get()
                cirth.append(results.to_dict()["Cirth"])
                i += 1
            # Defaults to T
            else:
                results = db.collection("Letters").document("T").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="U":
            #UU?
            if len(text) - 1 == (i+1):
                results = db.collection("Letters").document("U").get()
                cirth.append(results.to_dict()["Cirth"])
            elif text[i+1] == "U":
                results = db.collection("Letters").document("UU").get()
                cirth.append(results.to_dict()["Cirth"])
                i += 1
            # defaults to U
            else:
                results = db.collection("Letters").document("U").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="V":
            results = db.collection("Letters").document("V").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="W":
            results = db.collection("Letters").document("V").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] == "X":
            #X makes Z sound at the beginning of a word ---UNLESS IT'S ON IT"S OWN--- FIX THAT
            if text[i-1] == " " or i == 0:
                results = db.collection("Letters").document("Z").get()
                cirth.append(results.to_dict()["Cirth"])
            # Default: There is no X, so replaces with KS for similar sound
            else:
                results = db.collection("Letters").document("K").get()
                cirth.append(results.to_dict()["Cirth"])
                results = db.collection("Letters").document("S").get()
                cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="Y":
            results = db.collection("Letters").document("Y").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="Z":
            results = db.collection("Letters").document("Z").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] ==" ":
            results = db.collection("Letters").document("Space").get()
            cirth.append(results.to_dict()["Cirth"])
        elif text[i] =="." or text[i] =="," or text[i] =="!" or text[i] =="?":
            results = db.collection("Letters").document("Punctuation").get()
            cirth.append(results.to_dict()["Cirth"])
        else:
            # if symbol doesn't exist, gives a filler symbol
            cirth.append("_")
        i += 1
    if cirth[len(cirth) - 1] != "\u16EC" or cirth[len(cirth) - 1] != "\u16EB":
        cirth.append("\u16EC")
    return cirth
        

def print_text(finished_text):
    for letter in finished_text:
        print(letter, end = "")
    print("\n")

def add_character():
    doc = input("What letter does the character represent? > ")
    character = input("What is the unicode for the character > ")
    new = {"Cirth" : character}
    success = db.collection("Letters").document(doc).set(new)
    if success:
        print("Character added successfully!\n")
    else:
        print("Error: unable to add Character")

def update_character():
    doc = input("What letter character are you wanting to update? > ")
    character = input("What is the unicode for the character > ")
    print(character)
    success = db.collection("Letters").document(doc).update({"Cirth" : character})
    if success:
        print("")

def menu():
    print("NOTE: Option 4 and 5 do not add the printable unicode to the database.")
    print("\tOption 4 creates the document with the Cirth Unicode, and Option 5 saves the code too.")
    print("\tAny characters added through those options will need to be manually updated later.")
    print("<Option 1> Display the Key.")
    print("<Option 2> Display Example Text.")
    print("<Option 3> Convert Text.")
    print("<Option 4> Add Character.")
    print("<Option 5> Update Character.")
    print("<Option 6> Quit.\n")

    print("<Type # here> ", end = "")
    option = input()
    return option

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
        return False
    else:
        print("None existant option Please try again.")
    return True

#
play = True
while play:
    option = menu()
    play = interface(option)
print('\nThanks for playing!\n')

