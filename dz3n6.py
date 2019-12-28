def text_generator(filename):
    while True:
        with open(filename, "r") as f:
            for line in f:
                yield line.replace("\n", "")


gen = text_generator("somefile.txt")
text_filter = filter(lambda x: "NOD19" in x, gen)
for i, line in enumerate(text_filter):
    print(line)
    if i > 100:
        break
