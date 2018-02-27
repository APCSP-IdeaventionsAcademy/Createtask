# Natalie
# Create task

import string
import random

global t
global coded
global ncoded
global nrword
global encode
global randnum

t = ''
coded = ''
ncoded = ''
nrword = ''
encode = ''
randnum = random.randint(2,100)
   
def secret_code():
    global t
    global coded
    global ncoded
    global randnum
    global encode
    global nrword
    t = input('Enter a message to be encoded : ')
    encode = input('Now enter how you would like your message to be encoded in. You may choose more than one. c = Cypher; r = letter rearrangement; m = morse code : ')

    for l in encode:
        if l == 'c':
            if len(encode) == 1:
                Cypher()
                print(coded)
            else:
                Cypher()
            print('Each letter was moved forwards by', randnum, 'spaces.')

        elif l == 'r':
            Rearrange()
        elif l == 'm':
            Morsecode()
            if len(encode) == 1:
                print(coded)
            else:
                print(ncoded)
        else:
            print('invalid encoder')

# Cypher
def Cypher():
    global t
    global coded
    global randnum

    t = t.lower()
    
    # https://stackoverflow.com/questions/16060899/alphabet-range-python
    alfbet = list(2*string.ascii_lowercase)

    for l in t:
        if l == ' ':
            coded = coded + ' '
        else:
            # https://stackoverflow.com/questions/43102861/finding-an-element-from-one-list-in-another-list-in-python
            i = alfbet.index(l)
            
            i = int(i) + 5
            c = alfbet[i]
            c = str(c)
            coded = coded + (c)
            

# rearrangement
def Rearrange():
    global t
    global coded
    global ncoded
    global nrword
    if len(ncoded) > 0:
        coded = ncoded

    t = t + ' '
    
    word = ''
    for c in t:
        if c != ' ':
            word = str(word)
            
            word = word.replace("[","")
            word = word.replace("]","")
                
            c = str(c)
            word = word + (c)
        else:
            for l in range(len(word)):
                # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
                randletter = random.choice(word)
                randletter = str(randletter)

                word = list(word)
                
                nrword = nrword + randletter

                # https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
                letind = word.index(randletter)
                
                del word[letind]
            nrword = nrword + ' '

    word = str(word)
    print(nrword)
                    
                                          


# morsecode
def Morsecode():
    global coded
    global encode
    global ncoded
    global t
    t = t.lower()
    if len(encode) == 1:
        for l in t:
            if l == ' ':
                coded = coded + '  '
            elif l == 'a':
                coded = coded + '●- '
            elif l == 'b':
                coded = coded + '-●●● '
            elif l == 'c':
                coded = coded + '-●-● '
            elif l == 'd':
                coded = coded + '-●● '
            elif l == 'e':
                coded = coded + '● '
            elif l == 'f':
                coded = coded + '●●-● '
            elif l == 'g':
                coded = coded + '--● '
            elif l == 'h':
                coded = coded + '●●●● '
            elif l == 'i':
                coded = coded + '●● '
            elif l == 'j':
                coded = coded + '●--- '
            elif l == 'k':
                coded = coded + '-●- '
            elif l == 'l':
                coded = coded + '●-●● '
            elif l == 'm':
                coded = coded + '-- '
            elif l == 'n':
                coded = coded + '-● '
            elif l == 'o':
                coded = coded + '--- '
            elif l == 'p':
                coded = coded + '●--● '
            elif l == 'q':
                coded = coded + '--●- '
            elif l == 'r':
                coded = coded + '●-● '
            elif l == 's':
                coded = coded + '●●● '
            elif l == 't':
                coded = coded + '- '
            elif l == 'u':
                coded = coded + '●●- '
            elif l == 'v':
                coded = coded + '●●●- '
            elif l == 'w':
                coded = coded + '●-- '
            elif l == 'x':
                coded = coded + '-●●- '
            elif l == 'y':
                coded = coded + '-●-- '
            elif l == 'z':
                coded = coded + '--●● '
            elif l == '1':
                coded = coded + '●---- '
            elif l == '2':
                coded = coded + '●●--- '
            elif l == '3':
                coded = coded + '●●●-- '
            elif l == '4':
                coded = coded + '●●●●- '
            elif l == '5':
                coded = coded + '●●●●● '
            elif l == '6':
                coded = coded + '-●●●● '
            elif l == '7':
                coded = coded + '--●●● '
            elif l == '8':
                coded = coded + '---●● '
            elif l == '9':
                coded = coded + '----● '
            elif l == '0':
                coded = coded + '----- '
            else:
                coded = coded + '? '
    else:
        for l in coded:
            global ncoded
            if l == ' ':
                ncoded = ncoded + '  '
            elif l == 'a':
                ncoded = ncoded + '●- '
            elif l == 'b':
                ncoded = ncoded + '-●●● '
            elif l == 'c':
                ncoded = ncoded + '-●-● '
            elif l == 'd':
                ncoded = ncoded + '-●● '
            elif l == 'e':
                ncoded = ncoded + '● '
            elif l == 'f':
                ncoded = ncoded + '●●-● '
            elif l == 'g':
                ncoded = ncoded + '--● '
            elif l == 'h':
                ncoded = ncoded + '●●●● '
            elif l == 'i':
                ncoded = ncoded + '●● '
            elif l == 'j':
                ncoded = ncoded + '●--- '
            elif l == 'k':
                ncoded = ncoded + '-●- '
            elif l == 'l':
                ncoded = ncoded + '●-●● '
            elif l == 'm':
                ncoded = ncoded + '-- '
            elif l == 'n':
                ncoded = ncoded + '-● '
            elif l == 'o':
                ncoded = ncoded + '--- '
            elif l == 'p':
                ncoded = ncoded + '●--● '
            elif l == 'q':
                ncoded = ncoded + '--●- '
            elif l == 'r':
                ncoded = ncoded + '●-● '
            elif l == 's':
                ncoded = ncoded + '●●● '
            elif l == 't':
                ncoded = ncoded + '- '
            elif l == 'u':
                ncoded = ncoded + '●●- '
            elif l == 'v':
                ncoded = ncoded + '●●●- '
            elif l == 'w':
                ncoded = ncoded + '●-- '
            elif l == 'x':
                ncoded = ncoded + '-●●- '
            elif l == 'y':
                ncoded = ncoded + '-●-- '
            elif l == 'z':
                ncoded = ncoded + '--●● '
            elif l == '1':
                ncoded = ncoded + '●---- '
            elif l == '2':
                ncoded = ncoded + '●●--- '
            elif l == '3':
                ncoded = ncoded + '●●●-- '
            elif l == '4':
                ncoded = ncoded + '●●●●- '
            elif l == '5':
                ncoded = ncoded + '●●●●● '
            elif l == '6':
                ncoded = ncoded + '-●●●● '
            elif l == '7':
                ncoded = ncoded + '--●●● '
            elif l == '8':
                ncoded = ncoded + '---●● '
            elif l == '9':
                ncoded = ncoded + '----● '
            elif l == '0':
                ncoded = ncoded + '----- '
            else:
                ncoded = ncoded + '? '

# Runs starting function
secret_code()









            
