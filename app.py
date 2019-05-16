#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?') 
        mode = input().lower() # Turning input to all lower case characters
        if mode in ['encrypt', 'e', 'decrypt', 'd']: # If mode was equal to encrypt or e or decrypt or d then return the input
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') # Given an error and ask user to retry

def getMessage():
    print('Enter your message: ')
    return input() # Return input gotten from user
    

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) # LEss then 52
        key = int(input()) # Entering the key
        if (key >= 1 and key <= MAX_KEY_SIZE): # If the key was greater or equal to one and less than or equal to the length of symbols then return key
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd': # If decryptoin is the selected option we should go backwards
        key = -key
    translated = ''


    for symbol in message: # For each character in message (known as symbol)
        symbolIndex = SYMBOLS.find(symbol)
        #Basically checking whether symbol is a character or not
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS): # If passed the length 
            symbolIndex -= len(SYMBOLS) # Subtract
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex] # Get the real character
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key))