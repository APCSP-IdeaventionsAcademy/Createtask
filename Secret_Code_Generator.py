# Natalie Gainer
# Create task

import string
import random

global alfbet
global numbers

# Cite referenced to import the alphabet
# https://stackoverflow.com/questions/16060899/alphabet-range-python
alfbet = list(2*string.ascii_lowercase)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def Start():
    global t
    global coded
    global nrword
    global encode
    global randnum
    global mcoded
    global play_again
    global can_be_coded
    
    t = ''
    coded = ''
    nrword = ''
    encode = ''
    mcoded = ''
    play_again = 'y'
    can_be_coded = False

    randnum = random.randint(2,25)


def Encode():
    global encode
    global can_be_coded
    
    can_be_coded = False   
    while can_be_coded == False:
        
        encode = input('''Enter how you would like your message to be encoded. You may choose more than one.
c = cypher; r = letter rearrangement; m = morse code : ''')
        encode = encode.lower()
                
        if 'c' in encode or 'r' in encode or 'm' in encode:
            ch = 0
            for c in encode:
                if c not in alfbet:
                    ch += 1        
                else:
                    if c == 'c' or c == 'r' or c == 'm':
                        ch = ch
                    else:
                        ch += 1

            if ch > 0:
                print(encode, 'is not an option')
                print('')
            else:
                if len(encode) > 0 and 'm' in encode:
                    if 'c' in encode:
                        if encode.index('m') < encode.index('c'):
                            print('Cannot cypher the message after it has been translated to morse code.')  
                            print('')
                        else:
                            can_be_coded = True
                                
                    elif 'r' in encode:
                            if encode.index('m') < encode.index('r'):
                                print('Cannot rearrange the message after it has been translated to morse code.')
                                print('')
                            else:
                                can_be_coded = True
                    else:
                        can_be_coded = True
                else:
                    can_be_coded = True     
        else:
            print(encode, 'is not an option')
            print('')
            
            can_be_coded = False
    

# Main function            
def secret_code():
    global t
    global coded
    global randnum
    global encode
    global nrword
    global mcoded
    global can_be_coded
    
    t = input('Enter a message to be encoded : ')

    Encode()
    
    for l in encode:
        if l == 'c':
            Cypher()
            if len(encode) == 1:
                print(coded)

        elif l == 'r':
            Rearrange()
            if 'm' not in encode:
                print(nrword)
                
        elif l == 'm':
            Morsecode()
            print(mcoded)
        
    if 'c' in encode and 'r' not in encode:           
        print('Each character was moved forwards by', randnum, 'spaces.')


# Cypher
def Cypher():
    global alfbet
    global t
    global coded
    global randnum

    t = t.lower()
    coded = coded.lower()
    
    for l in t:
        if l == ' ':
            coded = coded + ' '
        elif l in numbers:
            l = int(l)
            l = l + randnum
            l = str(l)
            coded = coded + l
        elif l not in alfbet and l not in numbers:
            coded = coded + l
        else:
            # Cite referenced to find index of element
            # https://stackoverflow.com/questions/43102861/finding-an-element-from-one-list-in-another-list-in-python
            i = alfbet.index(l)
                
            i = i + randnum
            c = alfbet[i]
            coded = coded + (c)


def Rearrange():
    global t
    global coded
    global nrword
    
    t = t.lower()
    coded = coded.lower()
    nrword = nrword.lower()


    t = t + ' '
    word = ''
    
    for c in t:
        if c != ' ':
            if c in alfbet or c in numbers:    
                word = str(word)
                
                word = word.replace("[","")
                word = word.replace("]","")
                    
                c = str(c)
                word = word + (c)
            else:
                c = ''
        else:
            for l in range(len(word)):
                
                # Cite referenced to choose random character from string 
                # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
                randletter = random.choice(word)
                randletter = str(randletter)

                word = list(word)
                nrword = nrword + randletter
                letind = word.index(randletter)
                del word[letind]
                
            nrword = nrword + ' '
        if nrword == t:
            nrword = ''
            Rearrange()

    word = str(word)
                    
                                          
def Morsecode():
    global nrword
    global coded
    global encode
    global t
    global mcoded
    nrword = nrword.lower()
    coded = coded.lower()
    encode = encode.lower()
    t = t.lower()
    mcoded = mcoded.lower()

    iterm = ''
    if len(nrword) > 0:
        iterm = nrword
    elif len(encode) == 1:
        iterm = t
    else:
        iterm = coded
  
    for l in iterm:
        if l == ' ':
            mcoded = mcoded + '  '
        elif l == 'a':
            mcoded = mcoded + '●- '
        elif l == 'b':
            mcoded = mcoded + '-●●● '
        elif l == 'c':
            mcoded = mcoded + '-●-● '
        elif l == 'd':
            mcoded = mcoded + '-●● '
        elif l == 'e':
            mcoded = mcoded + '● '
        elif l == 'f':
            mcoded = mcoded + '●●-● '
        elif l == 'g':
            mcoded = mcoded + '--● '
        elif l == 'h':
            mcoded = mcoded + '●●●● '
        elif l == 'i':
            mcoded = mcoded + '●● '
        elif l == 'j':
            mcoded = mcoded + '●--- '
        elif l == 'k':
            mcoded = mcoded + '-●- '
        elif l == 'l':
            mcoded = mcoded + '●-●● '
        elif l == 'm':
            mcoded = mcoded + '-- '
        elif l == 'n':
            mcoded = mcoded + '-● '
        elif l == 'o':
            mcoded = mcoded + '--- '
        elif l == 'p':
            mcoded = mcoded + '●--● '
        elif l == 'q':
            mcoded = mcoded + '--●- '
        elif l == 'r':
            mcoded = mcoded + '●-● '
        elif l == 's':
            mcoded = mcoded + '●●● '
        elif l == 't':
            mcoded = mcoded + '- '
        elif l == 'u':
            mcoded = mcoded + '●●- '
        elif l == 'v':
            mcoded = mcoded + '●●●- '
        elif l == 'w':
            mcoded = mcoded + '●-- '
        elif l == 'x':
            mcoded = mcoded + '-●●- '
        elif l == 'y':
            mcoded = mcoded + '-●-- '
        elif l == 'z':
            mcoded = mcoded + '--●● '
        elif l == '1':
            mcoded = mcoded + '●---- '
        elif l == '2':
            mcoded = mcoded + '●●--- '
        elif l == '3':
            mcoded = mcoded + '●●●-- '
        elif l == '4':
            mcoded = mcoded + '●●●●- '
        elif l == '5':
            mcoded = mcoded + '●●●●● '
        elif l == '6':
            mcoded = mcoded + '-●●●● '
        elif l == '7':
            mcoded = mcoded + '--●●● '
        elif l == '8':
            mcoded = mcoded + '---●● '
        elif l == '9':
            mcoded = mcoded + '----● '
        elif l == '0':
            mcoded = mcoded + '----- '
        else:
            mcoded = mcoded + ''


def Replay():
    global play_again

    while play_again != 'n':
        print('')
        play_again = input('Would you like to encode another message? (y or n) : ')
        play_again = play_again.lower()
        print('')
        
        if play_again == 'y':
            Start()
            secret_code()
            
        elif play_again != 'n':
            print('invalid input')

        else:
            play_again = 'n'

            
# Runs starting function
Start()
secret_code()
Replay()

        









            
