#!/usr/bin/python3

key = b'\x13\x37\xbe\xef'

img = bytearray(open('file.bmp', 'rb').read())

# bmp data starts at offset 0x36
pixel_array = img[0x36:]
flag = ''

for txt_i in range(200):
    c = 0
    
    for byte_i in range(8):
        byte = pixel_array[byte_i + txt_i*8]
        bit = byte & 1
        c |= (bit << byte_i)

    c ^= key[(txt_i & 3)]
    flag += chr(c)

    if chr(c) == '}':
        break

print(flag)
