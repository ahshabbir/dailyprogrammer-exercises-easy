# Ahad H. Shabbir
# r/dailyprogrammer Challange #3
# Caeser Cipher Program

# Encrypt with a Caesear Cipher rotation of rotn.
def caeserCipher(msg: str, rotn: int) -> str:
    return ''.join([chr(ord(m)+ rotn - 1) for m in msg])

# Decrypt with a Caesear Cipher rotation of rotn.
def decryptCC(msg: str, rotn: int) ->  str:
    return ''.join([chr(ord(m) - rotn + 1) for m in msg])

