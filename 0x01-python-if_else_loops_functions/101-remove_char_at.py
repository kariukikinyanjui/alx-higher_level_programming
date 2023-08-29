#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s

    result = ""
    for a in range(len(s)):
        if a != n:
            result += s[a]
    return result
