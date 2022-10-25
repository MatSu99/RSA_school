import math
import converter
import random
import cipher_rsa
import options
import file_taker
from datetime import date  # importing date


def welcome():
    print("> Welcome to RSA coder")  # Initial message of program
    print("> Version 0.3")
    today = date.today()
    print("> Today's date:", today)
    print("PLEASE MAKE SURE THAT INPUT IS PROPERLY COPIED AND PASTED")
    print("ANY IMPROPER INPUT MAY RESULT IN FATAL ERROR OF PROGRAM")


def menu():  # Menu options
    print("Menu")
    print("[1] Encrypt message")
    print("[2] Decrypt message")
    print("[3] Generate set of keys")
    print("[4] Manual keys generator")
    print("[5] About")
    print("[9] Exit")
    print("Please enter proper option")


def menu_enc():
    print("Mode of encryption")
    print("[1] EBC")
    print("[2] CBC")
    print("[3] CFB")
    print("[4] OFB")
    print("Please enter proper option")


def menu_dec():
    print("Mode of decryption")
    print("[1] EBC")
    print("[2] CBC")
    print("[3] CFB")
    print("[4] OFB")
    print("Please enter proper option")


def about_me():
    print("RSA CODER")
    print("by Mateusz Sudak")
    print("1 Goal")
    print("Main goal of this program is to present implementation of RSA cipher algorithm")
    print("2 How to use")
    print("* To properly use this program for coding and decoding messages two people that want to exchange messages")
    print("  must have the same version of this program. It is specifically designed to handle files with this way")
    print("  of encryption and decryption")
    print("* It is important to entered files to code/decode in folder with files of this program(where main.py file")
    print("  is located)")
    print("* It is crucial for user to make sure that he/she and receiver/sender of message used the same")
    print("  MODE OF OPERATION")
    print("* Not every character is available to encrypt ! Please check documentation for more details")
    print("* Before user decide to use CFB or OFB he or she should get familiar with documentation ")
    print("  part: [CFB mode] and [OFB mode]")
    print("* In case of entering name of text file DO NOT enter type of file")
    print("  If file is named message.txt enter only: message")


def input_type():
    while True:
        print("Please select type of input: ")
        print("[1] Message will be entered by command line")
        print("[2] Message will be entered by text file")
        option_type = input("> ")
        if option_type == '1':
            print("Please write Your message: ")
            message = input("> ")
            return message
        elif option_type == '2':
            print("Remember, file has to be in folder with program !")
            print("Please write name of text file [without .txt]")
            name = input("> ")
            message = file_taker.extract_text(name)
            print("Your message: ")
            print(message)
            return message
        else:
            print("Invalid input, please try again")



def manual_rsa():  # Function to manually establish keys
    print("Entering incorrect number will result in error")
    print("Insert two PRIME number")
    p = int(input("p = "))
    q = int(input("q = "))
    n = p * q
    totient = (p - 1) * (q - 1)

    while True:  # Loop to insert e, will not end 'till proper e is provided
        e = int(input("Insert e > 1, COPRIME to " + str(totient) + "\n > "))  # input of user, e as an integer

        if e <= 1:  # e must be an integer bigger than 1, guard
            print("Insert e BIGGER than 1")
            continue

        if math.gcd(e, totient) == 1:  # Checking if it is coprime, guard
            break
        else:
            print("Inserted e is NOT a COPRIME, try again")

    while True:  # Loop to insert d, will not end 'till proper d is provided
        d = int(input("Insert d, which satisfy d*e mod tatien = 1"))  # input of user, d as an integer

        if d <= 1:  # Guard
            print("Incorrect d")
            continue

        tech1 = d * e
        if tech1 % totient == 1:  # Checking condition ed mod(tonteint) = 1, guard
            break
        else:
            print("Inserted d does NOT satisfy condition")
    print("Input values: ")
    print("p = ", p)
    print("q = ", q)
    print("e = ", e)
    print("d = ", d)
    print("Calculated values: ")
    print("totient = ", totient)
    print("n = ", n)
    print("Public key: n = ", n, "e = ", e)
    print("Private key: n = ", n, "d = ", d)
    m = int(input("Insert number\n"))
    c = pow(m, e) % n
    print("coded number = ",c)
    mdec = pow(c, d) % n
    print("decoded number = ", mdec)
    if m == mdec:
        print("Decoded correctly !")
    else:
        print("Something went wrong")


def rsa_program():
    while True:
        menu()
        option1 = input("> ")
        if option1 == '1':
            print("Please enter RSA public key components")
            #n = int(input("n > "))
            #e = int(input("e > "))
            ne = input("Public key >")
            ne_2 = converter.decover_key(ne)
            menu_enc()
            while True:
                option2 = input("> ")
                if option2 == '1':
                    text = input_type()
                    print("Please enter how You want to name file with encrypted message")
                    name = input("> ")
                    options.coding_rsa_ecb(text, name, ne_2[0], ne_2[1])
                    input("Press Enter to continue...")
                    break
                elif option2 == '2':
                    text = input_type()
                    print("Please enter how You want to name fail with encrypted message")
                    name = input("> ")
                    options.coding_rsa_cbc(text, name, ne_2[0], ne_2[1])
                    input("Press Enter to continue...")
                    break
                elif option2 == '3':
                    text = input_type()
                    print("Please enter how You want to name fail with encrypted message")
                    name = input("> ")
                    options.coding_rsa_cfb(text, name, ne_2[0], ne_2[1])
                    input("Press Enter to continue...")
                    break
                elif option2 == '4':
                    text = input_type()
                    print("Please enter how You want to name fail with encrypted message")
                    name = input("> ")
                    options.coding_rsa_ofb(text, name, ne_2[0], ne_2[1])
                    input("Press Enter to continue...")
                    break
                else:
                    print("Improper input, please try again")

        elif option1 == '2':
            menu_dec()
            while True:
                option3 = input("> ")
                if option3 == '1':
                    print("Please enter RSA private key")
                    #n = int(input("n > "))
                    #d = int(input("d > "))
                    ne = input("Private key >")
                    ne_2 = converter.decover_key(ne)
                    print("Please enter name of file with encrypted message")
                    name = input("> ")
                    options.decoding_rsa_ecb(name, ne_2[0], ne_2[1])
                    input("Press Enter to continue...")
                    break
                elif option3 == '2':
                    print("Please enter RSA private key")
                    #n = int(input("n > "))
                    #d = int(input("d > "))
                    ne = input("Private key >")
                    ne_2 = converter.decover_key(ne)
                    print("Please enter name of file with encrypted message")
                    name = input("> ")
                    options.decoding_rsa_cbc(name, ne_2[0], ne_2[1])
                    input("Press Enter to continue...")
                    break
                elif option3 == '3':
                    print("Please enter RSA key used during encryption: ")
                    #n = int(input("n > "))
                    #e = int(input("e > "))
                    ne = input("Private key >")
                    ne_2 = converter.decover_key(ne)
                    print("Please enter name of file with encrypted message")
                    name = input("> ")
                    options.decoding_rsa_cfb(name, ne_2[0], ne_2[1])
                    input("Press Enter to continue...")
                    break
                elif option3 == '4':
                    print("Please enter RSA key used during encryption: ")
                    #n = int(input("n > "))
                    #e = int(input("e > "))
                    ne = input("Private key >")
                    ne_2 = converter.decover_key(ne)
                    print("Please enter name of file with encrypted message")
                    name = input("> ")
                    options.decoding_rsa_ofb(name, ne_2[0], ne_2[1])
                    input("Press Enter to continue...")
                    break
                else:
                    print("Improper input, please try again")

        elif option1 == '3':
            options.keys_generator()
            input("Press Enter to continue...")
        elif option1 == '4':
            manual_rsa()
            input("Press Enter to continue...")
        elif option1 == '5':
            about_me()
            input("Press Enter to continue...")
        elif option1 == '6':
            print("Nothing here")
        elif option1 == '9':
            print("Goodbye !")
            break
        else:
            print("Improper input, please try again")












welcome()
rsa_program()



"""
# Test of encrpytione / decryption  modes
print("ECB")

my_text = "ECB test for RSA\n la la la"
options.coding_rsa_ecb(my_text, "Z_ecb", 1311846509, 676113407)
options.decoding_rsa_ecb("Z_ecb", 1311846509, 1130342879)
print("")
print("CBC")
text1 = "CBC test has been done. \n !@#$%^&*()|||"
options.coding_rsa_cbc(text1,"Z_cbc", 971144117, 542091251)
options.decoding_rsa_cbc("Z_cbc", 971144117, 502476923)
print("")
print("CFB")
text2 = "Cfb implemented correctly !!! <>"
options.coding_rsa_cfb(text2,"Z_cfb", 852901669, 268268013)
options.decoding_rsa_cfb("Z_cfb", 852901669, 268268013)
print("")
print("OFB")
text3 = "TEST OF OFB IS HERE ?;'"
options.coding_rsa_ofb(text3, "Z_ofb", 2792215441, 60846251)
options.decoding_rsa_ofb("Z_ofb", 2792215441, 60846251)

# Test of rsa components

test1 = cipher_rsa.key_generator()
m = 10
c = cipher_rsa.rsa_encrypt(m, test1[0], test1[1])

print("Ciphertext = ", c)
m_dec = cipher_rsa.rsa_decrypt(c, test1[0], test1[2])
print("Decrypted text = ", m_dec)

"""



