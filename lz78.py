def lz78(content):
    result = {"": ()}
    index = 0
    while index < len(content):
        length = 0
        key = 0
        char = ""
        while char in result:
            key = list(result.keys()).index(char)
            length += 1
            char = content[index:index + length]
        result[char] = (key, char[-1])
        index += length
    for i, key in enumerate(result):
        print(f"{i}\t{('|'+key+'|'):>8}\t{result[key]}")


if __name__ == '__main__':
    lz78("sir sid eastman easily teases sea sick seal")