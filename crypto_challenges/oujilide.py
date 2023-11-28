def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

if __name__ == "__main__":
    a = int(input("请输入a的值: "))
    b = int(input("请输入b的值: "))

    gcd, x, y = extended_gcd(a, b)

    print(f"{a}和{b}的最大公约数是: {gcd}")
    print(f"x = {x}, y = {y}")
    print(f"{a}*{x} + {b}*{y} = {gcd}")
