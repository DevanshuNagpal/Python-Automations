#!/usr/bin/python3

from pwn import *

# io = process(["nmap","127.0.0.1"])
# output = io.recvall()
# print(output.decode())

# io = process(["msfconsole","-q"],stdin = PTY)
# io.recvuntil(b">")
# io.sendline(b"use exploit/multi/handler") 

# io.sendline(b"set payload windows/x64/meterpreter/reverse_tcp")

# io.sendline(b"set lport 4444")
# io.sendline(b"set lhost eth0")

# io.interactive()

 

s1 = ssh(host = "127.0.0.1",user="kali",password="kali")
t1  = s1.shell("zsh")
t1.interactive()