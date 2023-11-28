def byte_xor(byte1, byte2):
    # 使用bytearray数据类型，可以改变字节串的值
    bytearray1 = bytearray(byte1)
    bytearray2 = bytearray(byte2)

    # 补到等长
    length = max(len(bytearray1), len(bytearray2))
    bytearray1.extend([0x00]*(length - len(bytearray1)))
    bytearray2.extend([0x00]*(length - len(bytearray2)))
    # 逐字节异或
    result = bytearray(a ^ b for a, b in zip(bytearray1, bytearray2))
    return bytes(result)
if __name__ == '__main__':
    byte1 = bytes.fromhex('37')
    byte2 = bytes.fromhex('58')
    byte3 = byte_xor(byte1, byte2)
    print(byte3)
