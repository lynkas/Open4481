def lzw(content):
    i = 0
    dic = []
    while i < len(content):
        length = 1
        code = 0
        while True:
            char = content[i:i + length]
            if length == 1:
                code = ord(char)
            elif char in dic:
                code = 256 + dic.index(char) + 1
            else:
                dic.append(char)
                i += length - 1
                if i < len(content):
                    # print(f"{code}")
                    print(f"{len(dic) + 256}\t{('|' + char + '|'):>8}\t{code}")
                else:
                    # print(f"{code}")
                    print(f"   \t{'':>8}\t{code}")
                break
            length += 1


if __name__ == '__main__':
    lzw("ABABABAB")
