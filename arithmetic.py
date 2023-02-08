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
    content = input()
    p = [float(x) for x in content.split()]
    content = input()
    seq = [int(x)-1 for x in content.split()]
    encoding((0,1),p,seq)