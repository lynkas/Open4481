from decimal import *

getcontext().prec = 10
d = Decimal


def E1(crange, encoded):
    changed = False
    new_crange = crange
    if crange[0] < 0.5 and crange[1] < 0.5:
        changed = True
        new_crange = (crange[0] * 2, crange[1] * 2)
        encoded += "0"

    return changed, new_crange, encoded


def E2(crange, encoded):
    changed = False
    new_crange = crange
    if crange[0] >= 0.5 and crange[1] >= 0.5:
        changed = True
        new_crange = ((crange[0] - d(0.5)) * 2, (crange[1] - d(0.5)) * 2)
        encoded += "1"

    return changed, new_crange, encoded


def E3(crange, encoded):
    changed = False
    new_crange = crange
    if 0.25 <= crange[0] < 0.5 <= crange[1] < 0.75:
        changed = True
        new_crange = (d(0.5) - (d(0.5) - crange[0]) * 2, d(0.5) + (crange[1] - d(0.5)) * 2)

    return changed, new_crange, encoded


def encode(original, tags):
    result = ""
    crange = (d(0), d(1))
    e3 = False
    for char_index in original:
        start = tags[char_index - 1]
        end = tags[char_index]
        distance = crange[1] - crange[0]
        crange = (crange[0] + distance * start, crange[0] + distance * end)
        print(f"{char_index} -> [{crange[0]},{crange[1]})")
        while True:
            for i, f in enumerate([E1, E2]):
                changed, new_crange, new_result = f(crange, result)
                if changed:
                    crange = new_crange
                    result = new_result
                    print(f"E{i+1} -> 0.{result} -> [{crange[0]},{crange[1]})")

                    break
            else:
                break
    result += "1"
    print(f"0.{result}")
    print("=========")


if __name__ == '__main__':
    content = input("p ")
    p = [d(x) for x in content.split()]
    tags = [0]
    for i in p:
        tags.append(tags[-1] + i)
    content = input("char ")
    seq = [int(x) for x in content.split()]
    encode(seq, tags)
