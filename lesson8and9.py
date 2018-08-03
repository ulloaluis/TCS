import random

def encrypt_message(msg):
    # Add in random characters in every other location
    # we want to reverse the string
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#!@,\"\\:;/}][{-_=+`~$ "
    new_str = ""

    for letter in msg:  # "dog" -> "dAopgI" -> "IgpoAd"
        new_str = new_str + letter + random.choice(letters)

    return new_str[::-1]


def decrypt_message(msg):
    return msg[::-2]


# want a loop that keeps prompting user for either "encrypt" or "decrypt"
# until the user enters the word "stop"
# ask user if they want to encrypt or decrypt, but can enter stop to end program
# if they say stop, break out of while loop
# elif they say encrypt, let's prompt them for an encryption message + level
# elif they say decrypt, let's prompt them for a decryption message + level
# else, they entered something we haven't covered, let's remind them that they
# can only enter the words "encrypt" "decrypt" and "stop"

cont_prog = True
while cont_prog:
    keyword = input("Enter whether you want to encrypt or decrypt a message: ")

    if keyword == "stop":
        cont_prog = False
    elif keyword == 'encrypt':  # enter the message you wish to encrypt
        msg = input("Enter a message and I'll encrypt it for you: ")
        encrypt_level = int(input("Layers of security: "))

        for i in range(encrypt_level):
            msg = encrypt_message(msg)
        print("Here's your encrypted message: ", msg)

    elif keyword == 'decrypt':  # enter the message you wish to decrypt
        msg = input("Enter an encrypted message and I'll decrypt it for you: ")
        decrypt_level = int(input("What was the encryption level? "))
        for i in range(decrypt_level):
            msg = decrypt_message(msg)

        print("Here's your decrypted message: ", msg)

    else:
        print("Invalid request.")

