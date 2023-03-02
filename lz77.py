def lz77(string):
    buffer_position = 0
    while buffer_position < len(string):
        last_ok = buffer_position+1
        encoding_length = 1
        while True:
            start = -1
            char_seq = string[buffer_position:buffer_position + encoding_length]
            for i in range(buffer_position, 0, -1):
                if string[i - 1:i - 1 + encoding_length] == char_seq:
                    start = max(start, i)
                    last_ok = start
                    encoding_length += 1
                    break
            else:
                encoding_length -= 1
                current_char = string[buffer_position + encoding_length] if buffer_position + encoding_length<len(string) else ""
                buffer_position += encoding_length+1
                break
        print(f"{string[:buffer_position]}|{string[buffer_position:]}\t",end="")
        print(f'{buffer_position - last_ok - encoding_length, encoding_length, current_char},')
if __name__ == '__main__':
    lz77(input())