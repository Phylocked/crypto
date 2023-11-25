from xor import byte_xor
if __name__ == '__main__':
    with open('5.txt','r') as file:
        plain_text = file.read().strip()
    key = 'ICE'
    repeated_key = ''
    while len(repeated_key) < len(plain_text):
        repeated_key += key
    repeated_key = repeated_key[0:len(plain_text)]
    bytes_repeated_key = repeated_key.encode()
    bytes_plain_text = plain_text.encode()
    bytes_cipher_text = byte_xor(bytes_repeated_key,bytes_plain_text)
    print(bytes_cipher_text)