# creating a caesar cipher
def encrypt(string, shift_by):
    """
    Encrypt the string into a new string
    """
    numList = [(ord(s) - shift_by) for s in string]
    encrypted_string = ''
    for i in numList:
        encrypted_string += chr(i)
    return encrypted_string


encryptedSentence = encrypt('This is a sentence for my people and It Has Weird CapitalS EvErywhere', 23)

print(encryptedSentence)
