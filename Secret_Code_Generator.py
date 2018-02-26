# Natalie
# Create task

global t
global coded
t = ''
coded = ''
    
def secret_code():
    global t
    global coded
    t = input('Enter a message to be encoded : ')
    encode = input('Now enter how you would like your message to be encoded in. You may choose more than one. c = Cyper; r = letter rearrangement; m = morse code : ')

    for l in encode:
        if l == 'c':
            Cypher()
        elif l == 'r':
            Rearrange()
        elif l == 'm':
            Morsecode()
        else:
            print('invalid encoder')
    print(coded)

# Cypher
def Cypher():
    global t


# rearrangement
def Rearrange():
    global t
    


# morsecode
def Morsecode():
    global coded 
    global t
    t = t.lower()

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
        
        
# Runs starting function
secret_code()









            
