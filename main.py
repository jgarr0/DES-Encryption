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

# using sample message and key from https://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
# to ensure tha tthe algorithim is working correctly

sample_message  = "0123456789ABCDEF"
sample_key      = "133457799BBCDFF1"

# convert key and message to binary
print(str2binary(sample_message))
print(str2binary(sample_key))