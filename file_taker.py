import os


def line_number(a):   # It will return number of line in file; a = string, name of file
    a = a  # + ".txt"
    count = 0
    for line in open(a).readlines():
        count +=1
    #print("Number of lines: ", count)
    return count


def creat_file(name):  # It creates file called name.txt; name = string, name of file
    name = name + ".txt"
    if os.path.exists(name):
        os.remove(name)

    f = open(name, "w+")
    f.close()
    print("File ", name, " has been created")
    return name


def insert_blocks(blocks, name):    # It will insert blocks to text file, one block in one line; blocks= list of strings
    creat_file(name)                # of binary coded, blocks; name = name of text file name.txt
    name = name + ".txt"
    f = open(name, "a")
    for i in range(len(blocks)):
        f.write(blocks[i] + "\n")
    f.close()
    return True


def insert_IV(IV, name):    # It will insert blocks to text file, one block in one line; blocks= list of strings
    creat_file(name)                # of binary coded, blocks; name = name of text file name.txt
    name = name + ".txt"
    f = open(name, "a")
    f.write(IV)
    f.close()
    return True


def extract_blocks(name):           # It will extract block from text file, and create list of the block
    name = name + ".txt"
    if os.path.exists(name):
        f = open(name, "rt")
        blocks = f.readlines()
        f.close()
        return blocks
    else:
        print("Error 6; No file named: ", name, " extraction failed")
        return "NO BLOCKS"


def insert_text(text, name):  # Inserting test into text file
    name = name + ".txt"
    if os.path.exists(name):
        f = open(name, "a")
        f.write(text)
        f.close()
        return
    else:
        print("ERROR 6.1; ", name, " insert failed")


def extract_text(name):
    #print("I WAS HERE!")
    name = name + ".txt"
    if os.path.exists(name):
        #blocks = []
        #a = line_number(name)
        f = open(name, "rt")
        text = f.readlines()
        f.close()
        text2 = ""
        for i in range(len(text)):
            text2 = text2 + text[i]
        #print(text2)
        return text2
    else:
        #print("Error 6.1; No file named: ", name, " extraction failed")
        return "NO TEXT"
