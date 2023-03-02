def dbwt(content, start):
    ordered = sorted(content)
    times = len(content)
    while times > 0:
        first = ordered[start]
        print(f"{start}\t{first}")
        number = nth(ordered, start)
        start = find_nth(content, number, first)
        times -= 1


def nth(content, index):
    char = content[index]
    count = 0
    for i, c in enumerate(content):
        if i == index:
            return count
        if c == char:
            count += 1


def find_nth(content, n, char):
    for i, c in enumerate(content):
        if c == char:
            n -= 1
            if n < 0:
                return i


def dm2f(numbers, charset_original):
    charset=[]
    for i in charset_original:
        if i not in charset:
            charset.append(i)
    charset = sorted(charset)
    decoded = []
    for i in numbers:
        char = charset[i]
        decoded.append(char)
        charset=[char]+charset[0:i]+charset[i+1:]
        print()
        [print(f"|{x}\t",end="") for x in range(len(charset))]
        print()
        [print(f"|{x}\t",end="") for x in charset]
        print()
        print(decoded)

if __name__ == '__main__':
    dbwt("sshtth ii e", 10)
    dm2f([4,0 ,3 ,5, 0, 1, 3, 5, 0, 1, 5]," ehist")
