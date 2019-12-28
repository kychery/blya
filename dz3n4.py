def text_generator(filename):
    while True:
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()


def len_string_generator(path):
    for line in text_generator(path):
        yield sum(map(len, line))


if __name__ == '__main__':
    gen = len_string_generator("somefile.txt")
    for i, line in enumerate(gen):
        print(line)
        if i > 50:
            break
