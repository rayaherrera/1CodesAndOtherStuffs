# Transposition Cipher

# original: this_is_a_secret_message_that_i_want_to_transmit
# encrypted:hsi__ertmsaeta__att_rnmtti_sasce_esg_htiwn_otasi

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

def encryptMessage():
    msg = input("Enter the message to encrypt: ")
    cipherText = scramble2Encrypt(msg)

# write a stripSpaces (text) function here
def stripSpace(text):
    print(text.replace(" ", ""))

# write a caesarEncrypt(plainText, shift)
def caesarencrypt(plainText, shift):
    result = ""
for i in range(len(plainText)):
    char = plainText[i]

    if (char.isupper()):
        result += chr((ord(char) + s - 65) % 26 + 65)
    else:
        result += chr((ord(char) + s - 97) % 26 + 97)
    return result
plainText = "CEASER CIPHER DEMO"
s = 4

print("Plain Text : " + text
print
"Shift pattern : " + str(s)
print
"Cipher: " + encrypt(text, s)

#another try
key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

text = "I committed to playing soccer at Penn State!"
offset = 5

encrypted = encrypt(offset, text)
print('Encrypted:', encrypted)

decrypted = decrypt(offset, encrypted)
print('Decrypted:', decrypted)




# write a caesarDecrypt(cipherText, shift)
