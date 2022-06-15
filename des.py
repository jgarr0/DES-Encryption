import text
class DES:
    ############################################################################################################################
    # permutation tables and dictionaries required by the DES algorithim

    # lookup for converting hex to 4 digit binary
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

    ############################################################################################################################
    # save the key and message

    message = ""
    message_binary = ""
    key = ""
    key_binary = ""
    key_array = [0] * 16
    encrypted_message = ""
    
    ############################################################################################################################
    # intenral function definitions

    def __init__(self, message = "", key = ""): 
        self.message = text.str2hex(message, 16)
        self.key = text.str2hex(key, 16)

    # xor two strings
    def xor(self, str1, str2):
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

    # assume input string has already been converted into hex
    def str2binary(self, inputString):
        # get length of input
        inputString = str(inputString)
        strLen = len(inputString)

        # return 0 if empty
        if (strLen == 0) or (inputString == "") or (inputString.isspace()):
            return 0
        # form binary string
        else:
            binString = ""
            for i in range(0, strLen):
                binString += self.HEXDICT.get(inputString[i])

        return binString

    # function to form keys and encode data
    def permutation(self, inputString, dict):
        permutation = ""
        for i in range(0, len(dict)):
            # subtract 1 from index as python is 0 indexed
            permutation += inputString[(dict[i]-1)]

        return permutation

    # function to form C and D (right and left halves of the key)
    def genCD(self, inputString):
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
            offset = self.LSI[lsi_index]

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

    def formKeyArray(self, inputArray):
        key_array = [0] * 16

        #fill kn
        for i in range(2, 34, 2):
            temp = inputArray[i] + inputArray[i+1]
            key_array[int(i/2)-1] = self.permutation(temp, self.PC2)
        return key_array

    def calculateF(self, rString, keyString):
        # compute expansion of Rn-1
        eString = self.permutation(rString, self.E)
        # compute the key xor e
        kxe = self.xor(eString, keyString)   #kxe = B1B2B3B4B4...B8

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
                s_output += format(self.S1[row_int][col_int], "04b")
            elif(i == 1):
                s_output += format(self.S2[row_int][col_int], "04b")
            elif(i == 2):
                s_output += format(self.S3[row_int][col_int], "04b") 
            elif(i == 3):
                s_output += format(self.S4[row_int][col_int], "04b")
            elif(i == 4):
                s_output += format(self.S5[row_int][col_int], "04b")
            elif(i == 5):
                s_output += format(self.S6[row_int][col_int], "04b")
            elif(i == 6):
                s_output += format(self.S7[row_int][col_int], "04b")
            elif(i == 7):
                s_output += format(self.S8[row_int][col_int], "04b")
        
        # permutate with P
        result = self.permutation(s_output, self.P)
        return result

    #Form PermutedMsg into left and right halves 
    def genLR(self, permutedMsg, keyArray): 
        # Create empty 34x32 array for LnRn pairs. 
        LR_array = [0]*34

        # Initialize L0 and R0
        LR_array[0] = permutedMsg[0:32]         # l0
        LR_array[1] = permutedMsg[32:64]        # r0

        # Initialize remaining Ln and Rn
        for i in range(2, 34, 2): 
            LR_array[i] = LR_array[i - 1]                # ln = Rn-1
            f_result = self.calculateF(LR_array[i-1], keyArray[int(i/2)-1])
            LR_array[i + 1] = self.xor(LR_array[i-2], f_result)

        final_permutation_binary = LR_array[33] + LR_array[32]
        final_permutation = self.permutation(final_permutation_binary, self.IP_INV)

        return final_permutation

    ############################################################################################################################
    # internal decryption process

    def dec_formKeyArray(self, inputArray):
        key_array = [0] * 16
        #fill kn
        for i in range(2, 34, 2):
            temp = inputArray[i] + inputArray[i+1]
            key_array[int(i/2)-1] = self.permutation(temp, self.PC2)

            reverse_key_array = key_array[::-1]
        #print(reverse_key_array)
        return reverse_key_array

    ############################################################################################################################
    # external encrypt/decrypt function

    # encrypt function
    def encryptDES(self):
        # catch invalid message
        if(self.message == "" or self.message.isspace()):
            print("Cannot have an empty encrypted  message")
            return

        # catch invalid key
        if(self.key == "" or self.key.isspace()):
            print("Cannot have an empty key")
            return

        # begin encryption process
        self.message_binary = self.str2binary(self.message)
        self.key_binary = self.str2binary(self.key)

        print("OG Message: ", self.message_binary)
 
        # save key array and encrypted message within instance of class
        self.key_array = self.formKeyArray(self.genCD(self.permutation(self.key_binary, self.PC1)))
        #print("Keys: ", self.key_array, "\n")
        self.encrypted_message = self.genLR(self.permutation(self.message_binary, self.IP), self.key_array)

        # return encrypted message
        return self.encrypted_message

    # default tpe is binary as that is what is saved in object
    def decryptDES(self, cyphertext = '', trykey = '', cyphertexttype = 'b'):
            # use instance variables if no parameters pased
            if not trykey:
                trykey = self.key_binary
            else:
                trykey = self.str2binary(text.str2hex(trykey, 16))
            
            if not cyphertext:
                cyphertext = self.encrypted_message
            # determine if cypher text is ascii or hex or binary
            else:
                # binary does nothing
                if(cyphertexttype == 'b' or cyphertexttype == 'B'):
                    cyphertext = text.modifyLength(cyphertext, 64)
                # hex
                elif(cyphertexttype == 'h' or cyphertexttype == 'H'):
                    cyphertext = self.str2binary(text.modifyLength(cyphertext, 16))
                # ascii
                elif(cyphertexttype == 'a' or cyphertexttype == 'A'):
                    cyphertext = self.str2binary(text.str2hex(cyphertext, 16))
                else:
                    return

            # catch invalid message
            if(cyphertext == "" or cyphertext.isspace()):
                print("Cannot have an empty message")
                return

            # catch invalid key
            if(trykey == "" or trykey.isspace()):
                print("Cannot have an empty key")
                return

            # save key array and encrypted message within instance of class
            dec_key_array = self.dec_formKeyArray(self.genCD(self.permutation(trykey, self.PC1)))
            #print(dec_key_array)
            decrypted_message = self.genLR(self.permutation(cyphertext, self.IP), dec_key_array)

            # return encrypted message
            return decrypted_message