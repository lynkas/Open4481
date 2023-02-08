def recursive(code, sample, tmp=None, original=False):
    if tmp is None:
        tmp = []
    if sample in tmp:
        return True, None
    tmp.append(sample)

    for single in code:
        if single == sample:
            if original: continue
            return False, sample
        elif single.startswith(sample):
            result = recursive(code, single[len(sample):], tmp)
        elif sample.startswith(single):
            result = recursive(code, sample[len(single):], tmp)
        else:
            continue
        if not result[0]:
            if original:
                return False, sample[0:len(single)] + result[1]
            return False, sample + result[1]
    return True, None


if __name__ == '__main__':
    while True:
        code = input()
        if not code:
            break
        code = code.split()
        results = set()
        instantaneous = True
        for i in code:
            tmp = []
            result = recursive(code, sample=i, tmp=tmp, original=True)
            if not result[0]:
                results.add(result)
            instantaneous &= len(tmp) == 1

        results = [r[1] for r in results if not r[0]]
        if not results:
            if instantaneous:
                print("instantaneous")
            else:
                print("not instantaneous")
            print("ok")
        else:
            for i in results:
                print(i)
        print("=" * 20)
