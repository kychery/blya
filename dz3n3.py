def text_generator(filename):
    while True:
        with open(filename, "r") as f:
            for line in f:
                yield line.replace("\n", "")


gen = text_generator("somefile.txt")
for i, line in enumerate(gen):
    print(line)
    if i > 100:
        break
        
