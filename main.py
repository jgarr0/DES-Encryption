import des

sample_message          = "0123456789ABCDEF"
sample_key              = "133457799BBCDFF1"

encryptme = des.DES(sample_message, sample_key)
print(encryptme.encryptDES())
print(encryptme.key_array)