def word_count(input_string: str) -> list[str]:
    # remove punctuation helper
    def helper(word: str):
        word_strip = ""
        for char in word:
            if char.isalpha():
                word_strip += char.lower()
        return word_strip

    # split string based on spaces, tracker for word occurrence, list_str for understanding order of relative frequency (most frequent word is in last bucket), maxCounter to initialize list_str
    res_split = input_string.split(" ")
    tracker = {}
    maxCounter = 0

    # remove punctuation of each word, append each stripped word to new list, create hashmap storing counts of each word, update maxCounter to always know which word is most frequent
    for char in res_split:
        string_word = helper(char)
        tracker[string_word] = 1 + tracker.get(string_word, 0)
        if tracker[string_word] > maxCounter:
            maxCounter = tracker[string_word]

    # create array containing n # of subarrays, n = maxCounter + 1
    list_str2 = [[] for _ in range(maxCounter + 1)]

    # store in subarrays word, count in each subarray
    for word, count in tracker.items():
        list_str2[count].append(word)
        list_str2[count].append(str(count))

    # descending order, deal with words that occur the same amount of times
    res = []
    for i in range(len(list_str2) - 1, 0, -1):
        if list_str2[i]:
            input_str = list_str2[i]
            if len(input_str) == 2:
                res.append(input_str)
            else:
                for i in range(0, len(input_str), 2):
                    arr = [input_str[i], input_str[i + 1]]
                    res.append(arr)
    return res


document1 = (
    "Practice makes perfect. you'll only get Perfect by practice. just practice!"
)
print(word_count(document1))
