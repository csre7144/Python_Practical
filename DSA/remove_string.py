def remove_invalid_closing(s):
    s = list(s)
    i = 0
    j = 0
    count = 0
    n = len(s)

    while j < n:
        if s[j] == '(':
            s[i] = s[j]
            i += 1
            count += 1
        elif s[j] != ')':  # character is not a parenthesis
            s[i] = s[j]
            i += 1
        else:  # s[j] == ')'
            if count == 0:
                j += 1
                continue
            s[i] = s[j]
            i += 1
            count -= 1
        j += 1

    return ''.join(s[:i])

# ✅ Example usage
input_string = "a)b(c)d)"
result = remove_invalid_closing(input_string)
print("Result after removing invalid ')':", result)
