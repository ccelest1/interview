"""

110 - 100 = 10

10 + 26 = 36 + 26 = 62 + 26 = 88 + 26 = 114

111 - 110 = 1 + 26*4 = 105

input: string, output: string
goal of function: decrypt encrypted message
to encrypt a message:
(1) convert every char in decrypted message to ascii value, ord(chr) ->
(2) 100 is between range,

results = []
results2 = []
decrypted -> encrypted
ord(char) ->

difference = 1 (base)

for every ord in string:
   ord(char)+=difference
   results.append(ord(char))
   difference = ord(char)

iterate through results
  if(ord('a')<= ord(char) <= ord('z')):
    results2.append(char)
   else:
      while(ord(char)>ord('z'))):
         ord(char)-=26
      results2.append(ord(char))

 # convert char to string
   iteart through results, convert ord to str, join in result string
iterate through results2
   result_str = ''
   for ord_char in results 2:
      result_str = chr(ord_char)
"""


def decrypt(word: str):
    results = []
    for i in range(len(word)):
        if i == 0:
            results.append(ord(word[i]) - 1)
        else:
            difference = ord(word[i]) - ord(word[i - 1])
            results.append(difference)
    for j in range(len(results)):
        if j > 0:
            new_result = results[j]
            while new_result < ord("a"):
                new_result += 26
            results[j] = new_result
    return "".join([chr(num) for num in results])


def encrypt(word):
    results = []
    results2 = []

    if not word:
        return results2

    difference = 1

    for str_char in word:
        new_char = ord(str_char) + difference
        results.append(new_char)
        difference = new_char

    for result1 in results:
        if ord("a") <= result1 <= ord("z"):
            results2.append(result1)
        else:
            while result1 > ord("z"):
                result1 -= 26
            results2.append(result1)

    result_str = ""
    for ord_char in results2:
        result_str += chr(ord_char)

    return result_str


# print(decrypt("crime"))
# print(decrypt("encyclopedia"))

print(decrypt("dnotq"))
print(decrypt("flgxswdliefy"))
