def bwt(content):
    for i in range(len(content)):
        print(f"{i}\t{content[-i:] + content[:-i]}")
    pair = list(zip([content[-i:] + content[:-i] for i in range(len(content))], range(len(content))))
    pair = sorted(pair, key=lambda item: item[0])
    print(f"\nsorted")
    for i in pair:
        print(f"{i[1]}\t{i[0]}")
    for i,c in enumerate(pair):
        if c[1]==0:
            print(f"original is line {i}")
    print("\n=====\n")
    return [x[0][-1] for x in pair]

def m2f(content):
    m2f = []
    print(f"char set")
    for i in content:
        char = i
        if char not in m2f:
            m2f.append(char)
    m2f = sorted(m2f)
    [print(f"|{x}\t",end="") for x in range(len(m2f))]
    print()
    [print(f"|{x}\t",end="") for x in m2f]
    print()
    print()

    encoded = []
    L = [x[0][-1] for x in content]
    for i in L:
        index = m2f.index(i)
        encoded.append(index)
        m2f=[m2f[index]]+m2f[0:index]+m2f[index+1:]
        print()
        [print(f"|{x}\t",end="") for x in range(len(m2f))]
        print()
        [print(f"|{x}\t",end="") for x in m2f]
        print()
        print(encoded)


if __name__ == '__main__':
    m2f(bwt(input()))