def decodeVariations(S: str) -> int:
    if not S:
        return 0
    # letters 0 -> 27 (non inclusive)

    """
    pre - aids in calculating 2 digit codes
        * (any digit * 10 + 27) >= 27
    curr - # ways for S[i:]
    """
    pre, cur = 27, 0

    # represent dp[i+1], dp[i+2] [first and second chars as we can only have between 0 and 26 representing A-Z]

    """
    Base case for DP
    first = # of ways to decode suffix S[i+1:]
    second = # of ways to decode S[i+2:]
    """
    first, second = 1, 1

    # iterate right to left
    for i in range(len(S) - 1, -1, -1):
        # store current character
        d = int(S[i])

        if d == 0:
            cur = 0
        else:
            cur = first

            """
            if current and next digit combine to <=26 add decodings from S[i+2:]
            """
            eval_2_digit = d * 10 + pre

            if eval_2_digit < 27:
                cur += second

        """
        pre now holds current digit for use by previous iteration
        slide dp window
        """
        pre = d
        first, second = cur, first

    return cur
