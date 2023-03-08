def dlz78(seq):
    dic = [""]
    result = ""
    for index, (prev_index, last) in enumerate(seq):
        char = dic[prev_index] + last
        dic.append(char)
        result += char
        print(f"{result:>60}|{str(index + 1):>4} {('|'+str(dic[-1])+'|'):>8} {prev_index, last}")


if __name__ == '__main__':
    dlz78([
        (0, 's'),
        (0, 'i'),
        (0, 'r'),
        (0, ' '),
        (1, 'i'),
        (0, 'd'),
        (4, 'e'),
        (0, 'a'),
        (1, 't'),
        (0, 'm'),
        (8, 'n'),
        (7, 'a'),
        (5, 'l'),
        (0, 'y'),
        (4, 't'),
        (0, 'e'),
        (8, 's'),
        (16, 's'),
        (4, 's'),
        (16, 'a'),
        (19, 'i'),
        (0, 'c'),
        (0, 'k'),
        (19, 'e'),
        (8, 'l'),
    ])
