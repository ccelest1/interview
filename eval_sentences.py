"""
my current intepretation: we have pairs/parings of words
these pairs are tuples in an array and similiarity between sentences
is judged by the number of words that two sentcs share within the pairs

input: two sentences of arrays containing words as element as well as
similair Pairs wich are list pairs in an array
output: boolean (true, false) in regards to sentences sharing similairity

example 1
similarPairs -> convert to dict of value-pairs
dict_pairs ={
    'code':'program'
}

sentence1 = ["Let's", "code", "in", "Python"]
                                         i
sentence2 = ["Let's", "program", "in", "Python"]

flag = True
if sentence1[i] === sentence2[i] ||
  ( dict_pairs[sentence1[i]] === dict_pairs[sentence2[i]] || dict_pairs[sentence2[i]] === dict_pairs[sentence1[i]] )
->
whereas these are equivalent then break

idea of similairty is if they share either the same dientical words or either
similarPairs = [
    ["code", "program"],
] -> true


example 2
sentence1 = ["I", "love", "to", "play", "football"]
sentence2 = ["I", "love", "playing", "soccer"]
similarPairs = [("play", "playing"), ("football", "soccer")]
flag = True
if len(sentence1)!==len(sentence2): flag = False
output: false, different sentence lengths

sentence1 = ["Do", "you", "like", "coffee"]
                            i
sentence2 = ["Do", "you", "love", "coffee"]
flag = True
    if sentence1[i] === sentence2[i] ||
    ( dict_pairs[sentence1[i]] === dict_pairs[sentence2[i]] || dict_pairs[sentence2[i]] === dict_pairs[sentence1[i]] )
    -> continue
    else:
        flag = False
        break
return flag

similarPairs = [
    ("like", "enjoy"),
    ("coffee", "tea"),
]
flag = False
output: false, "like" is not similar to "love" based on the given pairs.

edge cases

sentence1 = ["I", "really", "love", "leetcode", "and", "apples"]
              i
sentence2 = ["I", "so", "like", "codesignal", "and", "oranges"]
similarPairs = [
    ("very", "so"),
    ("love", "adore"),
    ("really", "very"),
    ("leetcode", "codesignal"),
    ("apples", "oranges"),
    ("like", "adore"),
]
output: true, "like" is similar to "love", because both are similar to "adore".
  if (
    dict_pairs[sentence1[word]] === dict_pairs[sentence2[word]]
  )
"""

from typing import List


def areSentencesSimilar(
    sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
) -> bool:

    flag = True
    if len(sentence1) != len(sentence2):
        flag = False
        return flag

    dict_pairs = {}

    for pair in similarPairs:
        dict_pairs[pair[0]] = pair[1]

    def determination_logic(word, dict):
        dict_set = set(dict.values()) | set(dict.keys())
        if word in dict_set:
            return True

    i = 0
    while i < len(sentence1) and i < len(sentence2):

        if sentence1[i] == sentence2[i] or (
            (determination_logic(sentence1[i], dict_pairs))
            and (determination_logic(sentence2[i], dict_pairs))
            and (
                dict_pairs[sentence1[i]] == sentence2[i]
                or dict_pairs[sentence2[i]] == sentence1[i]
                or dict_pairs[sentence1[i]] == dict_pairs[sentence2[i]]
            )
        ):
            i += 1

        else:

            flag = False
            break

    return flag


# TC - O(M+N) -> no nested loop, just dict access
# SC - O(1)

# debug your code below
sentence1 = ["Let's", "code", "in", "Python"]
sentence2 = ["Let's", "program", "in", "Python"]
similarPairs = [["code", "program"]]

sentence3 = ["i", "enjoy", "coding", "very", "much"]
sentence4 = ["i", "love", "programming", "so", "much"]
similarPairs = [["enjoy", "love"], ["coding", "programming"], ["very", "so"]]

print(areSentencesSimilar(sentence3, sentence4, similarPairs))
