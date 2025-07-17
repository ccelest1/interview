"""
//problem
given two strings of uppercase letters 'source', 'target', list a sequence of edits to convert source to target using the lest edits i.e return min(edits)

Example: source = 'ABCDEF', target = 'ABDFFGH' - > edits = ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]- for tokens that are similar to target and source append token, for token not present in target but in source -token, for token present in target but not in source +token

if there are multiple answers, use answer that favors removing from source first

// original attempt
source = str1
target = str2

idea:
  pointer i, j
  if(not source or not target): return
  longer string: len(str1) v len(str2)
    handle edge case of tie
  as we iterate, upper bound of iteration is the longer string
  min_transactions = 0
  transactions = []
  n in range(longer(str1)):
    compare each character
      encounter character thats found in source, thats not in target
        trans.append(f`-{char}`) // source[n]
      encounter char, found in target thats not in source
         trans.append(f`+{char}`) // target[n]
      encounter char in both
        trans.append(char) // source[n]

min = iterate number of transaction possibilities, min length(transactions(array))
min_transactions = min(min_transactions, len(transactions))
"""


def diffBetweenTwoStrings(source, target):
    """
    @param source: str
    @param target: str
    @return: str[]
    """
    i, j = 0, 0
    transactions = []

    if len(source) < len(target):
        longer_str = target
    else:
        longer_str = source
    while i < len(source) and j < len(target):
        print(i, j)
        if source[i] == target[j]:
            transactions.append(source[i])
            i += 1
            j += 1
        elif source[i] != target[j] and source[i] not in target:
            transactions.append(f"-{source[i]}")
            transactions.append(target[j])
            i += 1
        elif target[j] != source[i] and target[j] not in source:
            transactions.append(f"+{target[j]}")
            j += 1
            # if(len(source)!=len(target)):
            # (target[j] and not source[j]):
            #   transactions.append(f'+{target[j]}')
        """
        if longer_str == target:
            while i < len(source) or j < len(target):
                if source[i]:
                    if source[i] == target[j]:
                        transactions.append(target[j])
                    elif source[i] != target[j] and source[i] not in target:
                        transactions.append(f"-{source[i]}")
                        transactions.append(target[j])
                    i += 1
                    j += 1
        # rest of implementation is if the lengths are of differing length, but have to revise completely as this is too verbose
        """

    return transactions


input1 = {"source": "ABCDEFG", "target": "ABDFFGH"}

print(diffBetweenTwoStrings(input1["source"], input1["target"]))
