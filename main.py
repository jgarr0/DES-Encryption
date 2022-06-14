import des

sample_message          = "0123456789ABCDEF"
sample_key              = "133457799BBCDFF1"

encryptme = des.DES(sample_message, sample_key)
encryptedMessage = encryptme.encryptDES()
print("Encrypted Message: ", encryptedMessage, "\n")

decryptedMessage = encryptme.decryptDES()
print("Decrypted Message: ", decryptedMessage, "\n")
#encryptme.decryptDES("133457799BBCDFF1", encryptme.encrypted_message)

decryptme = des.DES()
print(decryptme.decryptDES(encryptedMessage, '133457799BBCDFF4'))