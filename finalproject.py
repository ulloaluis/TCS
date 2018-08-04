#!/usr/bin/env python3
import random


def encrypt_message_1(msg):
    # Add in random characters in every other location
    # we want to reverse the string
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#!@,\"\\:;/}][{-_=+`~$ "
    new_str = ""

    for letter in msg:  # "dog" -> "dAopgI" -> "IgpoAd"
        new_str = new_str + letter + random.choice(letters)

    return new_str[::-1]


def decrypt_message_1(msg):
    return msg[::-2]


def encrypt_message_2(msg):
    # random characters remain
    # substitute msg character for different character
    for k, letter in enumerate(msg):
        # i  be the index of letter

        msg = msg[:k] + chr(ord(letter) - 9) + msg[k+1:]

    return encrypt_message_1(msg)


def decrypt_message_2(msg):
    # same thing, but
    # back-substitute characters
    for k, letter in enumerate(msg):
        msg = msg[:k] + chr(ord(letter) + 9) + msg[k+1:]

    return decrypt_message_1(msg)


def encrypt_flow(msg):
    cont = True
    while cont:
        encrypt_type = int(input("Encryption 1 or 2: "))

        if encrypt_type == 1:
            msg = encrypt_message_1(msg)
            print("Here's your encrypted message: ", msg)
            cont = False
        elif encrypt_type == 2:
            msg = encrypt_message_2(msg)
            print("Here's your encrypted message: ", msg)
            cont = False
        else:
            print("Invalid request")


def decrypt_flow(msg):
    cont = True
    while cont:
        encrypt_type = int(input("Encryption 1 or 2: "))

        if encrypt_type == 1:
            msg = decrypt_message_1(msg)
            print("Here's your encrypted message: ", msg)
            cont = False
        elif encrypt_type == 2:
            msg = decrypt_message_2(msg)
            print("Here's your encrypted message: ", msg)
            cont = False
        else:
            print("Invalid request")


cont_prog = True
while cont_prog:
    keyword = input("Enter whether you want to encrypt or decrypt a message: ")

    if keyword == "stop":
        cont_prog = False
    elif keyword == 'encrypt':  # enter the message you wish to encrypt
        msg = input("Enter a message and I'll encrypt it for you: ")
        encrypt_flow(msg)

    elif keyword == 'decrypt':  # enter the message you wish to decrypt
        msg = input("Enter an encrypted message and I'll decrypt it for you: ")
        decrypt_flow(msg)

    else:
        print("Invalid request.")
