"""
Map the binary data from dynamic debugging into IDB file.
"""

from idaapi import *

binfile = '0050E000.bin'
begin_addr = 0x005C4FDC

data = open(binfile, 'rb').read()
end_addr = begin_addr + len(data)

print 'Map binary data to: ' + hex(begin_addr) + ' ~ ' + hex(end_addr)

i = 0
addr = begin_addr
while addr < end_addr:
    PatchByte(addr, ord(data[i]))
    addr += 1
    i += 1

print 'Map binary done.'