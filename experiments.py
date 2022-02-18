import io
from arepl_dump import dump
import re
from pathlib import PurePosixPath

path_string = '/mnt/PVE/SharePoint/ptnrMemblaze/Shared__Files/MemblazeFirmware/Weekly'

ss = PurePosixPath(path_string)

stringy = str(ss)

aaa = ss.parts
for i in aaa:
    print(i)

bbb = aaa.index('MemblazeFirmware')

foo = str(aaa[bbb+1]).lower()

def derive_firmware_type(path_string: str, firmware_dir: str):
    posix_path = PurePosixPath(path_string)
    parts = posix_path.parts
    firmware_dir_index = parts.index(firmware_dir)
    return(str(parts[firmware_dir_index + 1]).lower())

derived = derive_firmware_type(path_string, 'MemblazeFirmware')

print(derived)

firmware_rev_contents = '''
FIRMWARE_REV = 1234567
OTHER_THING = HELLO
STUFF = MoreStuff.23.55.abc
'''

f = io.StringIO(firmware_rev_contents)


def parse_firmware_rev(file_io):
    results = dict()
    for line in file_io:
        match
        print(line.strip())

parse_firmware_rev(f)


regex = r"^([a-zA-Z0-9_]+)\s*=\s*([a-zA-Z0-9_\.]+)$"
# test_str = "aaa = bbb.00.GG"
test_str = firmware_rev_contents
matches = re.finditer(regex, test_str, re.MULTILINE)

