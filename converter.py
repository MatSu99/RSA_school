import file_taker
import cipher_rsa


def to_bin(a):  # It will take integer a and convert it into string of binary notation of a
    b = bin(a).replace("0b", "")

    return b


def make_x_bit(a, b):   # a - binary number as string, b - number of bits User wants extend to
    c = len(a)          # It will extend binary number to required number of bits

    if c == b:
        return a
    d = b - c
    while d > 0:
        a = "0" + a
        d = d-1

    return a


def to_dec(binary):  # it will take binary number (int NOT STRING) and convert do decimal notation
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def char_to_num(a):  # It will take character and return its corresponding number defined in alphab defined in coverter
    b = ord(a)
    print(a)
    print(b)
    return b


def num_to_char(a):  # It will take number and return its corresponding character defined in alphnum defined in coverter
    b = chr(a)
    print(a)
    print(b)
    return b


def the_xor(a, b): # XOR GATE, for strings only
    if a == '0':
        if b == '0':
            return '0'  # a = 0, b = 0, a XOR b = 0
        else:
            return '1'  # a = 0, b = 1, a XOR b = 1
    else:
        if b == '0':
            return '1'  # a = 1, b = 0, a XOR b = 1
        else:
            return '0'  # a = 1, b = 1, a XOR b = 0


def conv_char_num(a): # It will take string and convert into corresponding number, then will put it into the list num[]
    num = []
    for i in range(len(a)):
        num.append(char_to_num(a[i]))
    return num


def blocks_to_num(a): # It will transform blocks of strings, into blocks of numbers
    blocks = []
    for i in range(len(a)):
        blocks.append(conv_char_num(a[i]))
    return blocks

def conv_num_char(a):  # It will convert numbers to character
    char = []
    for i in range(len(a)):
        char.append(num_to_char(a[i]))
    #print(char)
    return char



def blocks_to_char(a):  # It will convert numbers to character
    blocks = []
    for i in range(len(a)):
        blocks.append(conv_num_char(a[i]))
    return blocks


def create_blocks(message): # It will divide string into block of four characters
    length = len(message)
    over = length % 4
    count = 0
    count2 = 0
    blocks = []
    while count < (length - over):
        tech1 = ""

        for j in range(4):
            tech1 = tech1 + message[count]
            count += 1
            #  print(tech1)
        blocks.append(tech1)
        #  print(blocks)
        count2 += 1
    if over != 0:
        tech1 = ""
        if over == 1:
            tech1 = tech1 + message[count] + "   "
            blocks.append(tech1)
        elif over == 2:
            tech1 = tech1 + message[count] + message[count + 1] + "  "
            blocks.append(tech1)
        else:
            tech1 = tech1 + message[count ] + message[count + 1] + message[count + 2] + " "
            blocks.append(tech1)
    return blocks


def code_blocks(blocks, n, e):  # It will code numbers from blocks based on public key, it will return coded blocks
    blocks_cod = []
    for i in range(len(blocks)):
        tech1 = blocks[i]
        tech2 = []


        for j in range(4):
            tech2.append(cipher_rsa.rsa_encrypt(tech1[j], n, e))


        blocks_cod.append(tech2)
    return blocks_cod


def code_one_block(block, n, e):  # It will code ONE block using RSA algorithm
    block_cod = []

    for i in range(4):
        block_cod.append(cipher_rsa.rsa_encrypt(block[i], n, e))

    return block_cod


def decode_one_block(block, n, d):  # It will decode ONE block using RSA algorithm
    block_decod = []
    for i in range(4):
        block_decod.append(cipher_rsa.rsa_decrypt(block[i], n , d))

    return block_decod


def block_in_binary(a,b):  # It will convert block of data into string of binary data a = block, b = number of bits
    bin_string = ""

    for i in range(len(a)):
        bin_string = bin_string + make_x_bit(to_bin(a[i]), b)

    #print("BLOCK : ", bin_string)
    #if len(bin_string) != 128:
        #print("Error 28")
    return bin_string


def blocks_in_binary(blocks):  # It will create list of strings of binary data
    bit_blocks = []
    for i in range(len(blocks)):
        bit_blocks.append(block_in_binary(blocks[i], 32))

    return bit_blocks


def blocks_in_decimal(blocks):  # Blocks from binary to decimal notation, transform
    blocks_decimal = []

    for i in range(len(blocks)):
        blocks_decimal.append(block_in_decimal(blocks[i]))

    return blocks_decimal


def block_in_decimal(block):  # Block from binary to decimal notation, transform
    leng = len(block)
    block_dec = []
    bit_tracker = 0

    for i in range(4):
        letter = ""
        for j in range(32):
            letter = letter + block[bit_tracker]
            bit_tracker += 1
        #print("Letter = ", letter, " Num = ", bit_tracker)
        letter2 = reduce_msb(letter)
        numb = to_dec(int(letter2))
        block_dec.append(numb)

    return block_dec


def in_decimal_e(number):  # from binary to decimal, for every length
    reduced = reduce_msb(number)
    numb = to_dec(int(reduced))
    return numb


def reduce_msb(bin_num):   # Reducing binary number to its MSB, important for transformation bin->decimal
    a = bin_num.find("1")
    b = len(bin_num) - a + 1
    reduced = ""

    while b != 1:
        reduced = reduced + bin_num[a]
        a = a + 1
        b = b - 1

    return reduced


def decode_blocks(blocks, n, d):    # It will decode numbers from blocks based on private key, it will return
    blocks_decod = []               # decoded blocks
    for i in range(len(blocks)):
        tech1 = blocks[i]
        tech2 = []


        for j in range(4):
            tech2.append(cipher_rsa.rsa_decrypt(tech1[j], n, d))


        blocks_decod.append(tech2)
    return blocks_decod


def merge_blocks(blocks):  # Merging block of decrypted message into final message
    message = ""
    for i in range(len(blocks)):
        for j in range(4):
            message = message + blocks[i][j]

    return message


def xor_block(block1, block2):  # XOR of two blocks
    if len(block1) != len(block2):
        print("ERROR 14;Length of vector doesn't match block of message")
        return
    else:
        xor_block = ""
        for i in range(len(block1)):
            xor_block = xor_block + the_xor(block1[i],block2[i])

    #print(xor_block)
    return xor_block


def iv_xor_ver(iv, block, n):   # XOR in case of IV and first block of ciphertest
    iv_checked = ""             # In case of situation when after XOR m will be bigger then N, it perform adjustments
    iv_under_inv = ""
    block_under_inv = ""

    for i in range(4):

        a = 32*i
        b = 32 * (i+1)
        iv_under_inv = iv[a:b]

        block_under_inv = block[a:b]

        while True:
            xor = xor_block(iv_under_inv,block_under_inv)

            xor_deci = in_decimal_e(xor)
            if xor_deci < n:

                iv_checked = iv_checked + iv_under_inv
                break
            else:
                iv_under_inv = ""
                iv_under_inv = cipher_rsa.initial_vect_generator(32)

    return iv_checked


def iv_ver(iv, n):  # Checks if created IV will not result in situation m > N, proper adjustments in case of it
    iv_checked = ""
    for i in range(4):

        a = 32*i
        b = 32 * (i+1)
        iv_under_inv = iv[a:b]
        while True:
            iv_deci = in_decimal_e(iv_under_inv)
            if iv_deci < n:
                iv_checked = iv_checked + iv_under_inv
                break
            else:
                iv_under_inv = ""
                iv_under_inv = cipher_rsa.initial_vect_generator(32)

    return iv_checked


def number_of_char():
    print(len(alph))

def number_of_num():
    print(len(alph_num))


def cover_key(n, ed): # Converting key into one string
    n_1 = str(n)
    ed_1 = str(ed)
    l1 = len(n_1)
    l2 = len(ed_1)
    n_2 = ""
    ed_2 = ""
    final_key = ""

    for i in range(l1):
        n_2 = n_2 + num_to_char(int(n_1[i])+15)


    for i in range(l2):
        ed_2 = ed_2 + num_to_char(int(ed_1[i])+35)

    #print(n_2)
    #print(ed_2)
    final_key =  n_2 +"|" + ed_2
    #print(final_key)
    return final_key



def decover_key(ned):  # Converting key into one stream

    tech1 = ned.find("|")
    l1 = len(ned)
    n = ned[0:tech1]
    ed = ned[tech1+1: l1]
    #print(n)
    #print(ed)
    n_1 = ""
    ed_1 = ""

    for i in range(len(n)):
        n_1 = n_1 + str(char_to_num(n[i])-15)

    for i in range(len(ed)):
        ed_1 = ed_1 + str(char_to_num(ed[i])-35)

    #print(n_1)
    #print(ed_1)

    return int(n_1), int (ed_1)









#
alph = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'o', 'u', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'O', 'U', 'W', 'X', 'Y', 'Z',
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '-', '/', '.', ' ', ',', 'v', 'V', '<',
        '>', '?', ';', ':', '"', "'", '|', '[', '{', ']', '}', '\n', 'err')

alph_num =(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
           57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83 ,
           84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96)

