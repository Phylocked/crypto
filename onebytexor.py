from xor import byte_xor
from dataclasses import dataclass


def byte_frequency(b):
    # 字节转bytearray
    byte_array = bytearray(b)
    # 使用字典统计字符频数
    byte_count = {}
    # 统计
    for byte in byte_array:
        if byte in byte_count:
            byte_count[byte] += 1
        else:
            byte_count[byte] = 1
    most_frequent = max(byte_count, key=byte_count.get)
    return most_frequent


letter_frequencies = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074,
}


@dataclass(order=True)
class Score:
    score: float = 'inf'
    key: bytes = None
    cipher_text: bytes = None
    plain_text: bytes = None

    @classmethod
    def best_score(cls, c_t):
        pass


if __name__ == '__main__':
    ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    byte_ciphertext = bytes.fromhex(ciphertext)
    byte_frequency_cipher = byte_frequency(byte_ciphertext)
    frequency_cipher = chr(byte_frequency_cipher)
    byte_frequency_cipher = frequency_cipher.encode()
    # 改变这里的值来测试test_plain
    test_plain = ' '
    byte_test_plain = test_plain.encode()
    byte_test_key = byte_xor(byte_frequency_cipher, byte_test_plain)
    byte_array_test_key = bytearray(bytes([ord(byte_test_key.decode())]*len(byte_ciphertext)))
    test_key = bytes(byte_array_test_key)
    byte_test_plain = byte_xor(test_key, bytes.fromhex(ciphertext))
    print('the key is', byte_test_key)
    print(byte_test_plain)
