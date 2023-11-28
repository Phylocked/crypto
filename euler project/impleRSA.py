from crypto_challenges.oujilide import extended_gcd
from dataclasses import dataclass
from typing import Optional
import random
import sympy
import time
import secrets




def str2num(txt: str) -> int:
    bytes_hex = txt.encode()
    return int(bytes_hex.hex(), 16)


def num2str(num: int, errors='replace') -> str:
    hex_rep = hex(num)[2:]
    hex_rep = '0' * (len(hex_rep) % 2) + hex_rep
    b_str = bytes.fromhex(hex_rep)
    str_rep = b_str.decode(encoding='utf-8', errors=errors)
    return str_rep


def generate_prime(bits) -> int:
    while True:
        candidate = int(secrets.randbits(bits))
        # 使用Miller-Rabin算法进行素数检测
        if sympy.isprime(candidate):
            return candidate


def generate_two_random_primes(bits) -> tuple:
    prime1 = generate_prime(bits)
    prime2 = generate_prime(bits)

    while prime1 == prime2:
        # 确保两个素数不相等
        prime2 = generate_prime(bits)

    return prime1, prime2


def fast_modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # 可以提高性能，确保 base 在 modulus 范围内

    while exponent > 0:
        # 如果指数是奇数，乘以当前的 base
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # 将指数减半，同时将 base 平方
        exponent //= 2
        base = (base * base) % modulus

    return result


@dataclass(order=True)
class Rsa:
    public_key: Optional[list] = None
    private_key: Optional[list] = None

    @classmethod
    def gen_rsa_key(cls, p: int, q: int, e: int,):
        phi = (p-1) * (q-1)
        n = p * q
        d = extended_gcd(e, phi)[1]
        if d < 0:
            d = d + phi
        return cls([e, n], [d, n])

    def encrypto_rsa(self, plain_text: int) -> int:
        return fast_modular_exponentiation(plain_text, self.public_key[0], self.public_key[1])

    def decrypto_rsa(self, cipher_text: int) -> int:
        return fast_modular_exponentiation(cipher_text, self.private_key[0], self.private_key[1])


if __name__ == '__main__':
    plain = 'hello'
    int_plain = str2num(plain)
    print(int_plain)
    mp, mq = generate_two_random_primes(512)
    myRsa = Rsa.gen_rsa_key(mp, mq, 3)
    int_cipher = myRsa.encrypto_rsa(int_plain)
    print(int_cipher)
    decrypto = myRsa.decrypto_rsa(int_cipher)
    print(decrypto)
    str_plain = num2str(decrypto)
    print(str_plain)
