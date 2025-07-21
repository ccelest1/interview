def word_count_engine(document):
    if document == "":
        return []
    document = document.lower()
    words = [" "]
    for c in document:
        if ord("a") <= ord(c) and ord(c) <= ord("z"):
            words[-1] += c
        elif c == " ":
            if words[-1] != "":
                words.append("")
        else:
            continue

    if words[-1] == "":
        words.pop(-1)

    first_occurences = dict()
    freq = dict()

    for i, v in enumerate(words):
        if v not in first_occurences:
            first_occurences[v] = i
        if v not in freq:
            freq[v] = 0
        freq[v] += 1
    res = sorted(
        freq.items(), key=lambda l: (l[1], first_occurences[l[0]]), reverse=True
    )
    res = [[str(i[0]), str[i[1]]] for i in res]
    return res


document1 = (
    "Practice makes perfect. you'll only get Perfect by practice. just practice!"
)
print(word_count_engine(document1))
