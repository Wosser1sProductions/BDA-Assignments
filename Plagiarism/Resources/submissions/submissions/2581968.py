def cleanup_spaces(s):
    while s[0] == " ":
        s = s[1:]
    while "  " in s:
        for i in range(len(s)-2):
            if s[i] == " " and s[i+1] == " ":
                s = s[0:i] + s[i+1:]
    return s