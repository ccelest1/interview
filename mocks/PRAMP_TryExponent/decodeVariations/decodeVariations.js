/*
letter can be encoded from its character to a number value where A:1,...,Z:26
String of uppercase letters, encoded first using scheme of 'AZB' -> '1262"
Given string of digits S with each integer in range of 0-0, return number of ways to decode particular given S

input: S = '1262' -> output: 3
ex: there are 3 messages that encode to '1262' being 'AZB', 'ABFB', 'LFB'
"""

"""
Dynamic Programming Problem
dp[i] = answer from string S[i:] -> can calc dp(i) in terms of dp(i+1)and dp(i+2)

if s[i]==0, dp(i)=0, no encoded letters start with 0

if s[i]==1, dp(i) = dp(i+1) + dp(i+2) as we can only (1) write A + any way to write S[i+1] or (2) letter encoded between 10 and 19 then decoding S[i+2:] i.e next character

if s[i]==2, dp(i) = dp(i+1) + s[i+1]<=6?dp(i+2)(meaning its in range 0 to 6, translate that to char):0(none?)) -> either write B + write S[i+1:] or write letter between 20 and followed by next decoded char

if s[i]>2, then dp(i) = dp(i+1)-> can only be one char as no 2-integer combo can be greater than 26
*/

/**
 * @param {string} S
 * @return {number}
 */
//bottom up
var numDecoding = function (S) {
    const N = S.length
    let cache = {}
    cache[N] = 1
    for (let i = N - 1; i > -1; i--) {
        if (S[i] === '0') {
            cache[i] = 0
        } else {
            cache[i] = cache[i + 1]
        }

        if (
            i + 1 < N && (
                S[i] === "1" || S[i] == "2" && Number(S[i + 1]) <= 6
            )
        ) {
            cache[i] += cache[i + 2]
        }
    }
    return cache[0]
}


console.log(numDecoding("1262"))
