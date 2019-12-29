def get_most_frequent(words, k):
    setwords = set(words)
    same_words = []
    for word in setwords:
        if word in words:
            same_words.append([word, words.count(word)])
    same_words.sort(key=lambda x: x[1], reverse=True)
    return [same_words[i][0] for i in range(k)]


words = input("words = ").split(", ")
k = int(input("k = "))
print(get_most_frequent(words, k))
