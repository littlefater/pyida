"""
Map the APIs from dynamic debugging into IDB file.

Example of input file (api.txt):
005CB130  7C8316B7  kernel32.GetComputerNameW
005CB134  7C812DE6  kernel32.GetSystemInfo
005CB138  7C8612D7  kernel32.GetLogicalDriveStringsW
005CB13C  7C80FA75  kernel32.GetVolumeInformationW
005CB140  7C80B360  kernel32.GetDriveTypeW
005CB144  7C831DD3  kernel32.GetSystemDirectoryW
005CB148  7C82134B  kernel32.GetWindowsDirectoryA
005CB14C  7C80AE0B  kernel32.GetWindowsDirectoryW
005CB150  7C830779  kernel32.GetTempPathW
005CB154  7C80EF71  kernel32.FindFirstFileW
005CB158  7C80EFCA  kernel32.FindNextFileW
...
"""

import re
from idaapi import *


apifile = 'api.txt'
api_dict = dict()

for line in open(apifile, 'rb'):
    m = re.search('([0-9a-zA-Z]+).*\.(\w+)', line)
    if m is not None:
        api_addr = int(m.group(1), 16)
        api_name = m.group(2)
        api_dict[api_addr] = api_name

for addr, name in api_dict.items():
    print hex(addr), name
    i = 0
    while False == MakeName(addr, name):
        name = name + '_' + str(i)
        i += 1
        if i == 3:
            print 'Failed to rename address:', hex(addr) 
            break

