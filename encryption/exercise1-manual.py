import codecs

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

decodedString = hexString.decode('hex')
print(decodedString)

base64String = decodedString.encode('base64')
print(base64String)

# Import Codecs
# Taking original Hexstring
# Decoding Message
# Encoding it to base64