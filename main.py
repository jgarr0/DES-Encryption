# xor two strings
def xor(str1, str2):
    # empty result string
    res = ""
    if(len(str1) == len(str2)):
        for i in range(0, len(str1)):
            if(str1[i] == '0' and str2[i] == '0'):
                res += '0'
            elif(str1[i] == '1' and str2[i] == '1'):
                res += '0'
            else:
                res += "1"
        return res

    else:
        return 0

# lokup for converting hex to 4 digit binary
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

# Expansion table from 32 bit input to 48 bit output
E = [32, 1, 2, 3, 4, 5, 
     4, 5, 6, 7, 8, 9, 
     8, 9, 10, 11, 12, 13, 
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 
     20, 21, 22, 23, 24, 25, 
     24, 25, 26, 27, 28, 29, 
     28, 29, 30, 31, 32, 1]

# substitution boxes
S1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
       [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
       [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
      [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

S2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
       [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
       [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
      [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

S3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
      [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
      [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
       [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

S4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
     [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
     [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
      [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

S5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
     [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
      [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
     [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
      [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
       [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
       [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
     [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
      [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
      [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

S8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
       [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
       [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
       [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

# Permutation to calculate f
P = [16, 7, 20, 21, 
     29, 12, 28, 17, 
     1, 15, 23, 26, 
     5, 18, 31, 10, 
     2, 8, 24, 14, 
     32, 27, 3, 9, 
     19, 13, 30, 6, 
     22, 11, 4, 25]

# Final permutaiton for the result
IP_INV = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27, 
          34, 2, 42, 10, 50, 18, 58, 26, 
          33, 1, 41, 9, 49, 17, 57, 25]

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
        permutation += inputString[(dict[i]-1)]
        #print(permutation)

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

    #fill kn
    for i in range(2, 34, 2):
        temp = inputArray[i] + inputArray[i+1]
        key_array[int(i/2)-1] = permutation(temp, PC2)
    return key_array

def calculateF(rString, keyString):
    # compute expansion of Rn-1
    eString = permutation(rString, E)
    # compute the key xor e
    kxe = xor(eString, keyString)   #kxe = B1B2B3B4B4...B8

    # initialize substituion output
    s_output = ""

    # generate substrings
    # intiialize 8 elements to 0
    substrings = [0] * 8

    for i in range(0, 8):
        substrings[i] = kxe[(i*6):((i+1)*6)]
        
        # find row and column
        row_binary = "00"
        row_binary += substrings[i][0]
        row_binary += substrings[i][5]
        row_int = int(row_binary, 2)

        # column
        col_binary = substrings[i][1:5]
        col_int = int(col_binary, 2)

        if(i == 0):
            s_output += format(S1[row_int][col_int], "04b")
        elif(i == 1):
            s_output += format(S2[row_int][col_int], "04b")
        elif(i == 2):
            s_output += format(S3[row_int][col_int], "04b") 
        elif(i == 3):
            s_output += format(S4[row_int][col_int], "04b")
        elif(i == 4):
            s_output += format(S5[row_int][col_int], "04b")
        elif(i == 5):
            s_output += format(S6[row_int][col_int], "04b")
        elif(i == 6):
            s_output += format(S7[row_int][col_int], "04b")
        elif(i == 7):
            s_output += format(S8[row_int][col_int], "04b")
    
    # permutate with P
    result = permutation(s_output, P)
    return result

#Form PermutedMsg into left and right halves 
def genLR(permutedMsg, keyArray): 
    # Create empty 34x32 array for LnRn pairs. 
    LR_array = [0]*34

    # Initialize L0 and R0
    LR_array[0] = permutedMsg[0:32]         # l0
    LR_array[1] = permutedMsg[32:64]        # r0

    # Initialize remaining Ln and Rn
    for i in range(2, 34, 2): 
        LR_array[i] = LR_array[i - 1]                # ln = Rn-1
        f_result = calculateF(LR_array[i-1], keyArray[int(i/2)-1])
        LR_array[i + 1] = xor(LR_array[i-2], f_result)

    final_permutation_binary = LR_array[33] + LR_array[32]
    final_permutation = permutation(final_permutation_binary, IP_INV)

    return final_permutation

    

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
    if(known_key_aray[i] == key_array[i]):
        print("KEY", int(i+1), " MATCH")
    else:
         print("KEY", int(i+1), " ERROR")

print('\n')
permutedMsg = permutation(message_binary, IP)

result = genLR(permutedMsg, key_array)
print("Encrypted Message: " + result)