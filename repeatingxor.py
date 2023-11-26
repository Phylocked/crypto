from xor import byte_xor


def repeat_xor(key: bytes, text: bytes) -> bytes:
    r_key = b''
    while len(r_key) < len(text):
        r_key += key
    r_key = r_key[0:len(text)]
    return byte_xor(r_key, text)


if __name__ == '__main__':
    with open('5.txt', 'r') as file:
        plain_text = file.read().strip()
    my_key = 'ICE'
    b_key = my_key.encode()
    b_plain_text = plain_text.encode()
    result = repeat_xor(b_key, b_plain_text)
    print(result)
    