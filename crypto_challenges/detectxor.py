from onebytexor import byte_frequency
from xor import byte_xor
from dataclasses import dataclass
def is_bytes_printable(b:bytes) -> bool:
    # 最后一位有可能是换行符，因此不考虑最后一位的可打印情况
    return all(32 <= byte <= 126 for byte in b[0:len(b)-1])


def test_plain(line:bytes) -> None:
    for i in range(256):
        # print(len(line))
        test_key = bytes([i])*len(line)
        test_plain = byte_xor(test_key, line)
        if is_bytes_printable(test_plain):
            print(test_plain.decode())
# 打开文件并读取十六进制数字符串


if __name__ == '__main__':
    file_path = '4.txt'
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            byte_line = bytes.fromhex(line)
            test_plain(byte_line)
