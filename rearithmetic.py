precision = 10

def decoding(endpoint, p, n, level):
    if level == 0:
        return
    gap = round(endpoint[1] - endpoint[0], precision)
    local_position = n
    if endpoint[0] != 0:
        local_position = round(n - endpoint[0], precision)
    enlarged = round(local_position / gap, precision)
    remain = enlarged
    index = 0
    while round(remain - p[index],precision) >= 0:
        remain -= p[index]
        remain = round(remain, precision)
        index += 1
    print(index + 1, end="")
    start_at = round(sum(p[:index]), precision)
    end_at = round(start_at + p[index], precision)
    real_start = round(gap * start_at + endpoint[0],precision)
    real_end = round(gap * end_at + endpoint[0],precision)
    return decoding((real_start, real_end), p, n, level - 1)


def encoding(endpoint, p, data, current=0):
    print(f"{current}\t[{endpoint[0]:g},{endpoint[1]:g})")
    if current == len(data):
        print("=" * 20)
        return
    char = data[current]
    start_at = sum(p[:char])
    end_at = start_at + p[char]
    real_start = (endpoint[1] - endpoint[0]) * start_at + endpoint[0]
    real_end = (endpoint[1] - endpoint[0]) * end_at + endpoint[0]
    return encoding((real_start, real_end), p, data, current + 1)


if __name__ == '__main__':
    content = input("p")
    p = [float(x) for x in content.split()]
    number = input("number")
    number = float(number)
    level = input("level")
    level = int(level)
    decoding((0, 1), p,number, level)

