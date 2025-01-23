# Integer to  hex

def toHex(num):
    if num == 0:
        return '0'
    if num < 0:
        num += 2**32
    hex_str = '0123456789abcdef'
    res = ''
    while num > 0:
        res = hex_str[num % 16] + res
        num //= 16
    return res

def main():
    print("Integer to hex")
    num = int(input("Enter an integer: "))
    print(num, "Coverted to Hex =",toHex(num))

if __name__ == '__main__':
    main()