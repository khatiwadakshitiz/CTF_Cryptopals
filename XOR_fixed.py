def fixed_xor(buffer1,buffer2):
    if len(buffer1)!=len(buffer2):
        raise ValueError("Buffers must be of equal length")
    result = bytes([b1^b2 for b1,b2 in zip(buffer1,buffer2)]) 

    return result
hex_string1 = '1c0111001f010100061a024b53535009181c'
hex_string2 = '686974207468652062756c6c277320657965'
bytes_1 = bytes.fromhex(hex_string1)
bytes_2 = bytes.fromhex(hex_string2)
output = bytes.hex(fixed_xor(bytes_1,bytes_2))
print(output)