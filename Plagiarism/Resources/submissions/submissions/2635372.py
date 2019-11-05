lower_cases = [chr(i + ord('a')) for i in range(26)]
def encode(s, n):
    new_str = ""
    for i in s:
        if 'a' <= i <= 'z':
            code = (lower_cases.index(i) + (n)) % 26
            new_str += lower_cases[code]
        else:
            new_str += i
    return new_str


def decode(s, n):
    new_str = ""
    for i in s:
        if 'a' <= i <= 'z':
            code = (lower_cases.index(i) - (n)) % 26
            new_str += lower_cases[code]
        else:
            new_str += i
    return new_str