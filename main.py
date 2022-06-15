import des
import text

#sample_message          = "0123456789ABCDEF"
#sample_key              = "133457799BBCDFF1"

sample_message          = "catareok"
sample_key              = "ilikedog"

encryptme = des.DES(sample_message, sample_key)
encryptedMessage = encryptme.encryptDES()
print("Encrypted Message: ", encryptedMessage, "\n")


decryptedMessage = encryptme.decryptDES()
print("Decrypt attempt 1: ", decryptedMessage)

decryptedMessage2 = encryptme.decryptDES(encryptedMessage, sample_key)
print("Decrypt attempt 2: ", decryptedMessage2)


test = des.DES("ilikedog", "12345678")
test.encryptDES()
print("ENCRYPTED TEST: ", test.encrypted_message)
print("DECRYPT  TEST1: ", test.decryptDES())
print("DECRYPT  TEST2: ", test.decryptDES(test.encrypted_message, "12345678"))
print("DECRYPT  TEST3: ", test.decryptDES('1111000010100001111101000001100011001000011100101101111011000001', "12345678", 'B'))
print("DECRYPT  TEST4: ", test.decryptDES('F0A1F418C872DEC1', "12345678", 'H'))

print("DECRYPT  TEST5: ", test.decryptDES('catareok', "12345678", 'A'))