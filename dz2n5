def is_valid(braces_string):
    count_braces = 0
    if (braces_string[0] == ")") or (braces_string[-1] == "("):
        return False
    else:
        for i in range(len(braces_string)):
            if braces_string[i] == "(":
                count_braces += 1
            else:
                count_braces -= 1
        return count_braces == 0


braces_string = input("braces_string = ")
print(is_valid(braces_string))
