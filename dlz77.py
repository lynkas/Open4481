def dlz77(encoded):
    decoded = ""
    for each in encoded:
        for i in range(each[1]):
            decoded += decoded[len(decoded) - each[0]]
        decoded += each[2]
        print(f"{each}\t\t{decoded}|")


if __name__ == '__main__':
    dlz77(
        [
            (0, 0, "s"),
            (0, 0, "i"),
            (0, 0, "r"),
            (0, 0, " "),
            (4, 2, "d"),
            (4, 1, "e"),
            (0, 0, "a"),
            (6, 1, "t"),
            (0, 0, "m"),
            (4, 1, "n"),
            (8, 4, "i"),
            (0, 0, "l"),
            (0, 0, "y"),
            (7, 1, "t"),
            (8, 3, "e"),
            (2, 1, " "),
            (4, 2, "a"),
            (30, 3, "c"),
            (0, 0, "k"),
            (5, 5, ""),
        ]
    )
