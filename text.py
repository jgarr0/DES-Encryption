# check that a string is a set length
# pad or trim the string as necessary to achieve the desired length
def modifyLength(inputString, length):
    # get length of input
    inputLength = len(inputString)
    lengthDiff = length - inputLength
    # if negative difference, trim input
    if(lengthDiff < 0):
        return inputString[0:length]
    # if positive difference, pad input
    elif(lengthDiff > 0):
        for i in range(0, lengthDiff):
            inputString += '0'
        return inputString
    # no modification necessary if string length = desired length
    else:
        return inputString

# convert ascii to hex
def str2hex(inputString, length):
    x = inputString.encode('utf-8').hex()
    return modifyLength(x, length)

