from decimal import *

getcontext().prec = 10
d = Decimal


def E1(crange,binary):
    changed = False
    new_crange = crange
    if crange[0] < 0.5 and crange[1] < 0.5:
        changed = True
        new_crange = (crange[0] * 2, crange[1] * 2)
        print(f"E1 -> [{new_crange[0]},{new_crange[1]})", end=" ")
        if len(binary) == 0:
            binary = "0"
        binary = binary[1:]
    return changed, new_crange,binary


def E2(crange,binary):
    changed = False
    new_crange = crange
    if crange[0] >= 0.5 and crange[1] >= 0.5:
        changed = True
        new_crange = ((crange[0] - d(0.5)) * 2, (crange[1] - d(0.5)) * 2)
        print(f"E2 -> [{new_crange[0]},{new_crange[1]})", end=" ")
        if len(binary) == 0:
            binary = "0"
        binary = binary[1:]
    return changed, new_crange,binary


def E3(crange,binary):
    changed = False
    new_crange = crange
    if 0.25 <= crange[0] < 0.5 <= crange[1] < 0.75:
        changed = True
        new_crange = (d(0.5) - (d(0.5)-crange[0]) * 2, d(0.5) + (crange[1] - d(0.5)) * 2)
        print(f"E3 -> [{new_crange[0]},{new_crange[1]})", end=" ")
        binary = "1"+binary[2:]
    return changed, new_crange,binary


def decode(binary, tags, level):
    crange = (d(0), d(1))
    value = b2f(binary)

    while level > 0:
        while True:
            for f in [E1, E2, E3]:
                changed, new_crange,binary = f(crange,binary)
                if changed:
                    crange = new_crange
                    value = b2f(binary)
                    print(f"0.{binary}, i.e., {value}")
                    value = (value - crange[0]) / (crange[1] - crange[0])
                    break
            else:
                break

        for i, tag in enumerate(tags):
            if tag > value:
                level -= 1
                start = tags[i - 1]
                end = tags[i]
                crange = (crange[0] + (crange[1] - crange[0]) * start, crange[0] + (crange[1] - crange[0]) * end)
                print(f"{value} -> {i} -> [{crange[0]},{crange[1]})")
                value = (value - crange[0]) / (crange[1] - crange[0])
                break

    print("=========")


def b2f(binary):
    value = 1
    result = 0
    for char in binary:
        value /= d(2)
        if char == "1":
            result += value
    return result


if __name__ == '__main__':
    content = input("p ")
    # content = "0.8 0.02 0.18"
    p = [d(x) for x in content.split()]
    tags = [d(0)]
    for i in p:
        tags.append(tags[-1] + i)
    # number = "1100011000001"
    number = input("number ")
    # level = 4
    level = int(input("level "))
    decode(number, tags, level)
