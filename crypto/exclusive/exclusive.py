#!/usr/bin/python3

b = bytearray(open('encrypted.png', 'rb').read())

for i in range(len(b)):
    b[i] ^= 0xd7

open('decrypted.png', 'wb').write(b)