b_list = []
size = 3
ded_t = [b'abc', b'def', b'ghi', b'jfe', b'wad',]
for i in range(size):
    b_machine = b''
    for block in ded_t:
        if i < len(block):
            b_machine += bytes([block[i]])
    b_list.append(b_machine)
print(b_list)