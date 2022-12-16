f = open("Huffmandata.txt", "r")
# Since the program does not ask for the file title, the title
# of any file wanted to be read but be renamed to "Huffmandata"

filelen = 0 # The number of lines in the text file
while f.read(1) != "": # Finds the number of lines in the file
    filelen += 1
    f.readline()

f.seek(0) # Seeks the file pointer back to the beginning of the file
minp = [] # List used to hold the min-priority queue

# Source: https://pythonguides.com/priority-queue-in-python/
# Used for creating min-priority queue
i = 0
while i < filelen: # Extracts the data from the file and arranges it in tuples in a list
    x = f.read(1)
    f.read(1)
    y = int(float(f.read(4))*100)
    minp.append((y, x))
    f.readline()
    i += 1

minp.sort() # Sorts the list in ascending order, creating a min-priority queue
print(minp)

class HuffmanNode:
# A class describing each node of the Huffman tree
# Includes the value/weight of the node, and the children it points to (if any)
    def __init__(self, value, child1 = "NULL", child2 = "NULL", chars = ''):
        self.value = value
        self.child1 = child1
        self.child2 = child2
        self.chars = chars

tree = minp
while tree[0][0] != 100:
    c = ''
    if type(tree[0][1]) == str:
        c = c + tree[0][1]
    else:
        c = c + tree[0][1].chars
    if type(tree[1][1]) == str:
        c = c + tree[1][1]
    else:
        c = c + tree[1][1].chars

    x = HuffmanNode(tree[0][0] + tree[1][0], tree[0][1], tree[1][1], c)
    # Creates an instance of the HuffmanNode class with the value being the weight of the first two
    # nodes of the min-priority queue summed and the children being the nodes themselves

    tree.pop(0)
    tree.pop(0)
    # Removes the first 2 elements of the min-priority queue as they are now children of the
    # newly created HuffmanNode instance
    tree.append((x.value, x))
    tree.sort() # Reorders the queue with the new node so that the process can be repeated

print("Huffman tree created")
def endecode(): # Determines if user wants to encode or decode, hence endecode
    num = int(input("Input 1 for encoding a string of characters\nInput 2 for decoding a string of binary digits\n"))
    if num == 1 or num == 2: # Only acceptable answers are 1 and 2
        return num
    else:
        print("Invalid input, try again")
        return endecode()

def treedecode(node, dir, repeat):
    # Function for decoding bits to characters using tree
    # Node is the node the function will be searching through
    # Dir is the direction it will search in, using the first character of the string
    # Repeat keeps track of how many times the function calls itself so that the same
    # number of characters can be removed from bits when the function returns
    if int(dir[0]) == 0:
        # Navigates given node using the first character in the dir (direction) string
        # If 0, search left child (child1), if 1, search right child (child2)
        if type(node.child1) == str: # If the child is a string and not a class, return it
            return node.child1, repeat
        else:
            dir = dir[:0] + dir[1:]
            # Else, remove first character from dir and repeat recursively, searching the next node
            return treedecode(node.child1, dir, repeat+1)
    else:
        if type(node.child2) == str: # If the child is a string and not a class, return it
            return node.child2, repeat
        else:
            dir = dir[:0] + dir[1:]
            # Else, remove first character from dir and repeat recursively, searching the next node
            return treedecode(node.child2, dir, repeat+1)

def treeencode(node, nchar, track = ''):
    # Node is the HuffmanNode being searched for the character
    # nchar is the character being searched for
    # track keeps track of the current bits found for the character being searched for (return value)
    if type(node.child1) == str:
        if node.child1 == nchar:
            return track + '0'
    # If left child is match, return current tracked bits + 0
    else:
        if nchar in node.child1.chars:
            return treeencode(node.child1, nchar, track + '0')
    # If left child is node containing match, search it recursively
    if type(node.child2) == str:
        if node.child2 == nchar:
            return track + '1'
    # If right child is match, return current tracked bits + 1
    else:
        if nchar in node.child2.chars:
            return treeencode(node.child2, nchar, track + '1')
    # If right child is node containing match, search it recursively



num = endecode()
result = '' # String where the resulting characters/bits will be stored

if num == 1:
    char = input("Input the characters. Do not separate them\n").upper() # The characters to be encoded
    length = len(char)
    k = 0
    while k < length:
        result = result + treeencode(tree[0][1], char[0])
        char = char[:0] + char[1:]
        k += 1
        # Removes the already searched for characters and repeats the search for the rest
        # The overall while loop repeats until all characters are removed

elif num == 2:

    bits = input("Input the bits\n") # The bits to be decoded

    while bits != '':
        z = treedecode(tree[0][1], bits, 0)
        result = result + z[0] # Appends the resulting character found from treedecode to the result string
        a = 0
        while a < z[1]+1:
            bits = bits[:0] + bits[1:]
            a += 1
            # Removes the already searched for bits and repeats the search for the rest
            # The overall while loop repeats until all bits are removed
print(result)
