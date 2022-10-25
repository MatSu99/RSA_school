import converter
import file_taker
import cipher_rsa


def keys_generator():  # Function will generate keys for RSA algorithm based on function from cipher_rsa.py file
    print("Keys will be generated and provided in text file")

    while True:
        pq = cipher_rsa.pq_gen(2)
        if pq[0] * pq[1] < 4294967295:
            break
    ned = cipher_rsa.rsa_components(pq[0], pq[1])

    file_taker.creat_file("keys")

    p = str(pq[0])
    q = str(pq[1])
    n = str(ned[0])
    e = str(ned[1])
    d = str(ned[2])
    te1 = "Used primes: p = "

    to_input = ""
    to_input = to_input + te1 + p + "\nq = " + q + "\nPublic key = [n = " + n + ", e = " + e
    to_input = to_input + "]\nPrivate key = [n = " + n + ", d = " + d + "]\n"
    covered_public = converter.cover_key(ned[0], ned[1])
    covered_priv   = converter.cover_key(ned[0], ned[2])
    to_input = to_input + "Public: "+ covered_public + "\n" +"Private: " +covered_priv
    file_taker.insert_text(to_input, "keys")

    print("Public and private key has been created, do You want to display them now? [Y/N]")
    while True:
        option = input("> ")
        if option == "Y" or option == "y":
            print("Public key [n,e] = [" + n + ", " + e + "]")
            print(covered_public)
            print("Private key [n,d] = [" + n + ", " + d + "]")
            print(covered_priv)
            break
        elif option == "N" or option == "n":
            print("Keys not displayed")
            break
        else:
            print("Invalid command")
            print("Public and private key has been created, do You want to display them now? [Y/N]")

    print("WARNING\n Please remember to save keys before generating next set of keys")
    print("File with keys can be found in folder containing this program")


def coding_rsa_ecb(text, name, n, e):  # Coding message using rsa algorithm by ECB method
    if text == "":
        print("Nothing to code !")
        return
    blocks = converter.create_blocks(text)
   # print("Blocks     :", blocks)
    blocks_num = converter.blocks_to_num(blocks)
    #print("blocks_num :", blocks_num)
    blocks_cod = converter.code_blocks(blocks_num, n, e)
   # print("blocks_cod :", blocks_cod)
    blocks_bin = converter.blocks_in_binary(blocks_cod)
   # print("blocks_bin :", blocks_bin)
    file_taker.insert_blocks(blocks_bin, name)
    print("Message coded and saved in file named: ", name)
    print("Encrypted by RSA algorithm using ECB technique")


def decoding_rsa_ecb(name, n, d):  # Decoding message using rsa algorithm by ECB method
    extracted_blocks_bin = file_taker.extract_blocks(name)
    blocks_decimal = converter.blocks_in_decimal(extracted_blocks_bin)
    #print(blocks_decimal)
    blocks_decod = converter.decode_blocks(blocks_decimal, n, d)
   # print(blocks_decod)
    blocks_trans = converter.blocks_to_char(blocks_decod)
    #print(blocks_trans)
    blocks_merged = converter.merge_blocks(blocks_trans)
    #print(blocks_merged)
    print("Message from file ", name, " decoded")
    print("Message: ", blocks_merged)
    print("Decrypted by RSA algorithm using ECB technique")


def coding_rsa_cbc(text ,name, n, e):  # Coding message using rsa algorithm by CBC method
    if text == "":
        print("Nothing to code !")
        return
    iv = cipher_rsa.initial_vect_generator(128)
    blocks = converter.create_blocks(text)
    blocks_num = converter.blocks_to_num(blocks)
    blocks_bin1 = converter.blocks_in_binary(blocks_num)
    iv = converter.iv_xor_ver(iv, blocks_bin1[0],n)
    modifier = iv
    modified = blocks_bin1[0]
    blocks_cod = [iv]

    for i in range(len(blocks_bin1)):
        curr = converter.xor_block(modifier ,modified)
        to_code = converter.block_in_decimal(curr)
        coded = converter.code_one_block(to_code, n, e)
        binary_again = converter.block_in_binary(coded, 32) # Checked
        blocks_cod.append(binary_again)
        if i == len(blocks_bin1)-1:
            break
        modifier = binary_again
        modified = blocks_bin1[i+1]
    file_taker.insert_blocks(blocks_cod, name)
    print("Message coded and saved in file named: ", name)
    print("Encrypted by RSA algorithm using CBC technique")


def decoding_rsa_cbc(name, n, d):  # Decoding message using rsa algorithm by CBC method
    extracted_blocks_bin = file_taker.extract_blocks(name)

    iv = extracted_blocks_bin[0]
    iv = iv[0:128]
    modified = extracted_blocks_bin[1]
    modified = modified[0:128]

    modifier = iv
    blocks_dec = []



    for i in range(len(extracted_blocks_bin)-1):
        blck_num = converter.block_in_decimal(modified)  #block into numbers
        blck_dec = converter.decode_one_block(blck_num, n, d)
        blck_bin_again = converter.block_in_binary(blck_dec, 32)


        #print(blck_bin_again, "Place B1")
        #print((type(blck_bin_again)))
        #print(modifier, "Place B2")
        #print((type(modifier)))
        #print(len(modifier))


        blck_xor = converter.xor_block(modifier, blck_bin_again)
        blck_num_again = converter.block_in_decimal(blck_xor)
        blck_trans = converter.conv_num_char(blck_num_again)
        blocks_dec.append(blck_trans)

        if i == len(extracted_blocks_bin)-2:
            break
        modifier = extracted_blocks_bin[i+1]
        modifier = modifier[0:128]
        modified = extracted_blocks_bin[i+2]
        modified = modified[0:128]

    message = converter.merge_blocks(blocks_dec)
    print("Message from file ", name, " decoded")
    print("Message: ", message)
    print("Decrypted by RSA algorithm using CBC technique")


def coding_rsa_cfb(text,name, n, e):  # Coding message using rsa algorithm by CFB method
    if text == "":
        print("Nothing to code !")
        return
    iv = cipher_rsa.initial_vect_generator(128)
    iv = converter.iv_ver(iv, n)
    blocks = converter.create_blocks(text)
    blocks_num = converter.blocks_to_num(blocks)
    blocks_bin1 = converter.blocks_in_binary(blocks_num)
    modified = iv
    modifier = blocks_bin1[0]
    blocks_cod = []

    for i in range(len(blocks_bin1)):
        to_code = converter.block_in_decimal(modified)
        coded = converter.code_one_block(to_code, n, e)
        binary_again = converter.block_in_binary(coded, 32)
        xor = converter.xor_block(binary_again, modifier)
        blocks_cod.append(xor)
        if i == len(blocks_bin1) - 1:
            break
        modifier = blocks_bin1[i+1]
        modified = xor
    file_taker.insert_blocks(blocks_cod,name)
    file_taker.insert_IV(iv,"IV_CFB")
    print("Message coded and saved in file named: ", name)
    print("Encrypted by RSA algorithm using CFB technique")
    print("IV generated, transfer it by secure channels")


def decoding_rsa_cfb(name, n , e):  # Decoding message using rsa algorithm by CFB method
    extracted_blocks_bin = file_taker.extract_blocks(name)

    iv = file_taker.extract_text("IV_CFB")
    if iv == "NO TEXT":
        print("Error during IV extraction, decoding ended unsuccessfully")
        return 10

    iv = iv[0:128]
    modifier = extracted_blocks_bin[0]
    modifier = modifier[0:128]

    modified = iv
    blocks_dec = []

    for i in range(len(extracted_blocks_bin)):
        to_dec = converter.block_in_decimal(modified)
        to_bin = converter.code_one_block(to_dec,n ,e)
        to_xor = converter.block_in_binary(to_bin, 32)
        xor = converter.xor_block(to_xor, modifier)
        to_dec_ag = converter.block_in_decimal(xor)
        to_tra = converter.conv_num_char(to_dec_ag)
        blocks_dec.append(to_tra)
        if i == len(extracted_blocks_bin)-1:
            break
        modified = extracted_blocks_bin[i]
        modifier = extracted_blocks_bin[i+1]
        modifier = modifier[0:128]
        modified = modified[0:128]

    message = converter.merge_blocks(blocks_dec)
    print("Message from file ", name, " decoded")
    print("Message: ", message)
    print("Decrypted by RSA algorithm using CFB technique")


def coding_rsa_ofb(text, name, n, e):  # Coding message using rsa algorithm by OFB method
    if text == "":
        print("Nothing to code !")
        return
    iv = cipher_rsa.initial_vect_generator(128)
    iv = converter.iv_ver(iv, n)
    blocks = converter.create_blocks(text)
    blocks_num = converter.blocks_to_num(blocks)
    blocks_bin1 = converter.blocks_in_binary(blocks_num)
    modified = iv
    modifier = blocks_bin1[0]
    blocks_cod = []
    for i in range(len(blocks_bin1)):
        to_code = converter.block_in_decimal(modified)
        coded = converter.code_one_block(to_code, n, e)
        binary_again = converter.block_in_binary(coded,32)
        xor = converter.xor_block(binary_again, modifier)
        blocks_cod.append(xor)
        if i == len(blocks_bin1) - 1:
            break
        modifier = blocks_bin1[i+1]
        modified = binary_again
    file_taker.insert_blocks(blocks_cod,name)
    file_taker.insert_IV(iv, "IV_OFB")
    print("Message coded and saved in file named: ", name)
    print("Encrypted by RSA algorithm using OFB technique")
    print("IV generated, transfer it by secure channels")


def decoding_rsa_ofb(name, n , e):  # Decoding message using rsa algorithm by OFB method
    extracted_blocks_bin = file_taker.extract_blocks(name)
    iv = file_taker.extract_text("IV_OFB")
    if iv == "NO TEXT":
        print("Error during IV extraction, decoding ended unsuccessfully")
        return 10


    iv = iv[0:128]
    modifier = extracted_blocks_bin[0]
    modifier = modifier[0:128]

    modified = iv
    blocks_dec = []

    for i in range(len(extracted_blocks_bin)):
        to_dec = converter.block_in_decimal(modified)
        to_bin = converter.code_one_block(to_dec,n ,e)
        to_xor = converter.block_in_binary(to_bin, 32)
        xor = converter.xor_block(to_xor, modifier)
        to_dec_ag = converter.block_in_decimal(xor)
        to_tra = converter.conv_num_char(to_dec_ag)
        blocks_dec.append(to_tra)
        if i == len(extracted_blocks_bin)-1:
            break
        modified = to_xor
        modifier = extracted_blocks_bin[i+1]
        modifier = modifier[0:128]


    message = converter.merge_blocks(blocks_dec)
    print("Message from file ", name, " decoded")
    print("Message: ", message)
    print("Decrypted by RSA algorithm using OFB technique")









