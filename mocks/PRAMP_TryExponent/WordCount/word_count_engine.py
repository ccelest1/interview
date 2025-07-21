"""
implement document scanning function 'wordCountEngine'
the function receives string `document` nad returns list of unique words in it and # of occurrences sorted in descending order

if 2 or more words have same count, they should be sorted according to their placement in the original sentence -> assumptions: all letters are in english alphabet

function should be case-insensitive, so 'Perfect' and 'perfect' are the same word

engine has to strip out punctuation and use whitespaces to separate words
analyze tc, sc of solution
"""

"""
solution needs to first iterate over the string (given its non-empty) and count occurrences of each word with its being case-insensitive (using .lower)
we need to take care of punctuation (even in word middle) and whitespaces so take into account if current char is letter within a to z range
    * can either use .split("") and then ask if char in each word is between a to z range using ord to be added to initialized empty string that will contain all strings in said document input devoid of punctuation

we need to also consider if two strings occur in the same frequency
thus we need to have a dict that stores the element and its index if we do encounter that scenario so in a tie, we can return first occurring string of that frequency followed by second, ... n occurring string

then given the frequency count and occurrences dict
we need to access largest so "practice":3 has no tie, so append to result = [], for i,v in count.items(): if v == max(count.values()), result.append([i,str(v)]) -> del count[i]
"""


def word_count_engine(doc: str) -> list[list[str]]:
    result = []
    if not doc:
        return result

    def remove_punctuation(string):
        new_str = ""
        for char in string.lower():
            if ord("a") <= ord(char) <= ord("z"):
                new_str += char
        return new_str

    count = {}
    word_doc = doc.split(" ")
    for word in word_doc:
        word_doc[word_doc.index(word)] = remove_punctuation(word)
    for word in word_doc:
        count[word] = 1 + count.get(word, 0)

    # we know that word_doc indicates the order in which strings occur
    max_freq = max(count.values(), default=0)
    for word, freq in count.items():
        if freq == max_freq:
            result.append([word, str(freq)])

    return result


document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(document))
