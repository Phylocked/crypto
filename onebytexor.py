from xor import byte_xor
from dataclasses import dataclass
from typing import Optional


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


def calculate_score(t_p: bytes) -> float:
    length = len(t_p)
    score = 0.0
    for letter, value in letter_frequencies.items():
        frequency = t_p.count(ord(letter))/length
        err = abs(frequency - value)
        score += err
    return score


@dataclass(order=True)
class Score:
    score: float = float('inf')
    key: Optional[bytes] = None
    cipher_text: Optional[bytes] = None
    plain_text: Optional[bytes] = None

    @classmethod
    def best_score(cls, b_ct: bytes, int_key: int,):
        b_k = bytes([int_key]) * len(b_ct)
        b_p = byte_xor(b_k, b_ct)
        score = calculate_score(b_p)
        return cls(score, bytes([int_key]), b_ct, b_p)


def find_best(c_t: bytes) -> Score:
    best_s = Score()
    for i in range(256):
        test_score = Score.best_score(c_t, i)
        best_s = min(best_s, test_score)
    if best_s.plain_text is None:
        exit('No such key')
    return best_s


if __name__ == '__main__':
    ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ciphertext = bytes.fromhex(ciphertext)
    best = find_best(ciphertext)
    print(best)
