def count_unique_codes(words):
    morse_base = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."]
        
    alph = [chr(l) for l in range(ord("a"), ord("z")+1)]
    dict = {}
    for i, j in zip(alph, morse_base):
        dict[i] = j
    same_words = set()
    for word in words:
        str = ""
        for i in range(len(word)):
            str = str + dict[word[i]]
        same_words.add(str)
    return same_words


words = input("Введите слова: ").split()
print(count_unique_codes(words))
