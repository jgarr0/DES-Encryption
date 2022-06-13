# lokup for converting hex to 4 digit binary
from re import I


HEXDICT = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'a' : '1010',
    'A' : '1010',
    'b' : '1011',
    'B' : '1011',
    'c' : '1100',
    'C' : '1100',
    'd' : '1101',
    'D' : '1101',
    'e' : '1110',
    'E' : '1110',
    'f' : '1111',
    'F' : '1111',
}

# left shifts per iteration
LSI = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# permutations to form the first key
PC1 = [57, 49, 41,33, 25, 17, 9,
        1, 58, 50,42, 34, 26, 18,
        10, 2, 59,51, 43, 35, 27,
        19, 11, 3,60, 52, 44, 36,
        63, 55, 47,39, 31, 23, 15,
        7, 62, 54,46, 38, 30, 22,
        14, 6, 61,53, 45, 37, 29,
        21, 13, 5,28, 20, 12, 4]

# permutations to form the nth key
PC2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]

# Initial Permutation to the message data
IP  =  [58, 50, 42, 34, 26, 18, 10, 2, 
        60, 52, 44, 36, 28, 20, 12, 4, 
        62, 54, 46, 38, 30, 22, 14, 6, 
        64, 56, 48, 40, 32, 24, 16, 8, 
        57, 49, 41, 33, 25, 17, 9, 1, 
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]

# Exansion table from 32 bit input to 48 bit output
E = [32, 1, 2, 3, 4, 5, 
     4, 5, 6, 7, 8, 9, 
     8, 9, 10, 11, 12, 13, 
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 
     20, 21, 22, 23, 24, 25, 
     24, 25, 26, 27, 28, 29, 
     28, 29, 30, 31, 32, 1]

# assume input string has already been converted into hex
def str2binary(inputString):
    # get length of input
    strLen = len(inputString)

    # return 0 if empty
    if (strLen == 0) or (inputString == "") or (inputString.isspace()):
        return 0
    # form binary string
    else:
        binString = ""
        for i in range(0, strLen):
            binString += HEXDICT.get(inputString[i])

    return binString

# function to form keys and encode data
def permutation(inputString, dict):
    permutation = ""
    for i in range(0, len(dict)):
        # subtract 1 from index as python is 0 indexed
        permutation += inputString[dict[i]-1]

    return permutation

# function to form C and D (right and left halves of the key)
def genCD(inputString):
    # create empty 34x28 array for Cn Dn pairs:
    # c0[0], c0[1], ... c0[27]
    # d0[0], d0[1], ... d0[27]
    # . 
    # . 
    # . 
    # c16[0], c16[1], ... c16[27]
    # d16[0], d16[1], ... d16[27]

    CD_array = [0] * 34

    # initalize c0 and d0
    #print(inputString[0:28])
    #print(inputString[28:56])
    CD_array[0] = inputString[0:28]
    CD_array[1] = inputString[28:56]

    # initalize remaining cn and dn
    for i in range(2, 33, 2):
        # get shifts in LSI
        lsi_index = int((i-2)/2)
        offset = LSI[lsi_index]

        # compute c
        cn = CD_array[i-2]
        LHS = cn[0:offset]
        RHS = cn[-(28-offset):]
        CD_array[i] = RHS + LHS

        # compute d
        dn = CD_array[i-1]
        LHS = dn[0:offset]
        RHS = dn[-(28-offset):]
        CD_array[i+1] = RHS + LHS

    return CD_array

def formKeyArray(inputArray):
    key_array = [0] * 17
    # fill k0
    key_array[0] = inputArray[0] + inputArray[1]

    #fill kn
    for i in range(2, 33, 2):
        temp = inputArray[i] + inputArray[i+1]
        key_array[int(i/2)] = permutation(temp, PC2)

    return key_array

# #Form PermutedMsg into left and right halves 
# def genLR(permutedMsg, key): 
#     # Create empty 34x32 array for LnRn pairs.  
#     LR_array = [0]*34; 

#     # Initialize L0 and R0
#     LR_array[0] = permutedMsg[0:32]
#     LR_array[1] = permutedMsg[32:64]

#     # Initialize remaining Ln and Rn
#     for i in range(2, 33, 2): 
#         Ln = LR_array[i - 1]; 
#         Rn = Ln[i-1] 


    

# using sample message and key from https://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
# to ensure tha tthe algorithim is working correctly

sample_message          = "0123456789ABCDEF"
sample_message_binary   = "0000000100100011010001010110011110001001101010111100110111101111"
sample_key              = "133457799BBCDFF1"
sample_key_binary       = "0001001100110100010101110111100110011011101111001101111111110001"
sample_KP_binary        = "11110000110011001010101011110101010101100110011110001111"

# convert key and message to binary
message_binary = str2binary(sample_message)
print(message_binary)
print("test message binary == known message binary: ", sample_message_binary == message_binary, "\n")

key_binary = str2binary(sample_key)
print(key_binary)
print("test key binary == known key binary: ", sample_key_binary == key_binary, "\n")

KP_binary = permutation(key_binary, PC1)
print(KP_binary)
print("test KP binary == known KP binary: ", sample_KP_binary == KP_binary, "\n")

# generate cn and dn
key_parts = genCD(KP_binary)

# check that cn and dn match the provided values
known_cd = ["1111000011001100101010101111", "0101010101100110011110001111", "1110000110011001010101011111", "1010101011001100111100011110", "1100001100110010101010111111", "0101010110011001111000111101",
           "0000110011001010101011111111", "0101011001100111100011110101", "0011001100101010101111111100", "0101100110011110001111010101", "1100110010101010111111110000", "0110011001111000111101010101",
           "0011001010101011111111000011", "1001100111100011110101010101", "1100101010101111111100001100", "0110011110001111010101010110", "0010101010111111110000110011", "1001111000111101010101011001",
           "0101010101111111100001100110", "0011110001111010101010110011", "0101010111111110000110011001", "1111000111101010101011001100", "0101011111111000011001100101", "1100011110101010101100110011", 
           "0101111111100001100110010101", "0001111010101010110011001111", "0111111110000110011001010101", "0111101010101011001100111100", "1111111000011001100101010101", "1110101010101100110011110001",
           "1111100001100110010101010111", "1010101010110011001111000111", "1111000011001100101010101111", "0101010101100110011110001111"]

for i in range(2, 34, 2):
    if(key_parts[i] == known_cd[i] and key_parts[i+1] == known_cd[i+1]):
        print("c", int(i/2), " d", int(i/2), " MATCH")
    else:
        print("c", int(i/2), " d", int(i/2), " ERROR")

# combine cn and dn and form their respective keys
key_array = formKeyArray(key_parts)

# check compared to provided keys
known_key_aray = ["000110110000001011101111111111000111000001110010",
                  "011110011010111011011001110110111100100111100101",
                  "010101011111110010001010010000101100111110011001",
                  "011100101010110111010110110110110011010100011101",
                  "011111001110110000000111111010110101001110101000",
                  "011000111010010100111110010100000111101100101111",
                  "111011001000010010110111111101100001100010111100",
                  "111101111000101000111010110000010011101111111011",
                  "111000001101101111101011111011011110011110000001",
                  "101100011111001101000111101110100100011001001111",
                  "001000010101111111010011110111101101001110000110",
                  "011101010111000111110101100101000110011111101001",
                  "100101111100010111010001111110101011101001000001",
                  "010111110100001110110111111100101110011100111010",
                  "101111111001000110001101001111010011111100001010",
                  "110010110011110110001011000011100001011111110101"]

print('\n')

for i in range(0, 16):
    if(known_key_aray[i] == key_array[i+1]):
        print("KEY", int(i+1), " MATCH")
    else:
         print("KEY", int(i+1), " ERROR")

print('\n')
permutedMsg = permutation(message_binary, IP)
print(permutedMsg)

