import math


def entropy(data):
    result = 0
    for x in data:
        result -= x * math.log2(x)
    return result


def fraction(original):
    data = [float(x) for x in original.split("/")]
    return data[0] / data[1]


if __name__ == '__main__':
    content = input()
    p = [(float(x) if "/" not in x else fraction(x)) for x in content.split()]
    print(entropy(p))
