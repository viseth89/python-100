import codecs

hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

b64=codecs.encode(codecs.decode(hex,"hex"), 'base64').decode()

print(b64)
print('hello')


###
#Understanding difference between implementtation

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
decoded = hex_str.decode("hex")
# I'm killing your brain like a poisonous mushroom
base64_str = decoded.encode("base64")
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n
print(base64_str)
print(decoded)

#Create a variable, use method of codecs to convert hex to base 64



#!/usr/bin/python

# Convert hex to base64
# 
# The string:
#
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#
# Should produce:
#
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

def HexToRaw(s):
    """Return raw bytes from a hexadecimal string."""
    r = s.decode("hex")
    return r

def RawToBase64(s):
    """Return a base64 strong from raw bytes."""
    b = s.encode("base64")
    return b

if __name__ == "__main__":
    h = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    try:
        assert(RawToBase64(HexToRaw(h)).strip() == b)
        print("Success")
    except AssertionError:
        print("Failure")