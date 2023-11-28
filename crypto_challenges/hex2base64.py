import base64


def hex_to_base64(hex_string):
    # 将16进制字符串转换为字节串
    byte_string = bytes.fromhex(hex_string)

    # 使用base64模块进行编码
    base64_encoded = base64.b64encode(byte_string)

    return base64_encoded



if __name__ == '__main__':
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base64_bytes = hex_to_base64(hex_string)
    print(base64_bytes)