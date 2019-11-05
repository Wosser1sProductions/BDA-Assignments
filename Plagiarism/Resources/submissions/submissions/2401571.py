def encode(s, n):
    new = ""
    for i in range(len(s)):
        if s[i] != ' ':
            new += chr(((ord(s[i]) - ord('a') + n) % 26) + ord('a'))
        else:
            new += s[i]
    return new


def decode(s, n):
    new = ""
    for i in range(len(s)):
        if s[i] != ' ':
            new += chr(((ord(s[i]) - ord('a') - n) % 26) + ord('a'))
        else:
            new += s[i]
    return new
