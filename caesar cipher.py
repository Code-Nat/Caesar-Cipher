def encrypt(plaintext, key):
    key_as_int = int(key)
    plaintext_int = [ord(i)-65 for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        if (plaintext_int[i] != -33):
            value = (plaintext_int[i] + key_as_int) % 26
        else:
            value = -33
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_as_int = int(key)
    ciphertext_int = [ord(i)-65 for i in ciphertext] 
    plaintext = ''
    for i in range(len(ciphertext_int)):
        if (ciphertext_int[i] != -33):
            value = (ciphertext_int[i] - key_as_int) % 26
        else:
            value = -33
        plaintext += chr(value + 65)
    return plaintext

inputKey = input ("Please type in e for encrypting and d for decripting: ")
if (inputKey == 'e'):
    print("Your encrypted text is: " + encrypt(input("Please enter plain text: "), input ("Please enter Key: ")))
if (inputKey == 'd'):
    inputKey = input ("Do you know the key? leave blank to try all, or enter key to decrypet")
    if (inputKey == ""):
	    text = input("Please enter encrypted text: ")
	    for i in range(27):
		    print("Your dencrypted text for key "+ str(i) + " is: " + encrypt(text, str(i+33)))
    else:
        print("Plain text is: " + decrypt(input("Please enter text: "), input ("Please enter Key: ")))