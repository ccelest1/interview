def bracket_match(text: str) -> int:
    stack = []
    counter = 0
    for c in text:
        if c == "(":
            stack.append(c)
        else:
            if len(stack):
                p = stack.pop()
                if p != "(":
                    counter += 1
            else:
                counter += 1

    return counter + len(stack)
