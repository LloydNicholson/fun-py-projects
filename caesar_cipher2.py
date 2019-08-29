allLetters = f'{"abcdefghijklmnopqrstuvwxyz!@#%*?$"}{"abcdefghijklmnopqrstuvwxyz ".upper()}'

letters = [item for item in allLetters]


# creating a caesar cipher with a different method of using the indexes
def encrypt(string, shift_by):
    encryptedString = ''
    for s in string:
        letterIndex = letters.index(s)
        if letterIndex + shift_by < len(letters):
            encryptedString += letters[letterIndex + shift_by]
        else:
            lengthToEnd = len(letters) - letterIndex
            fromStart = shift_by - lengthToEnd
            newChar = letters[fromStart]
            encryptedString += newChar
            # newLetters.append(letters[letterIndex + self.shift_by])
    return encryptedString


# print(letters[letters.index(s)])

# using imported file of my own caesar cipher
newEncryptedString = encrypt('Another random sentence with A big X and Z and these !%$', 5)
print(newEncryptedString)
