def encode(s, n):
    string = ""
    for i in s:
        if 'a' <= i <= chr(ord('z') - n) or 'A' <= i <= chr(ord('A') - n):
            string = string + chr(ord(i) + n)
        elif chr(ord('a') - n + 1) <= i <= 'z' or chr(ord('A') - n + 1) <= i <= 'Z':
            string = string + chr(ord(i) - (26 - n))
        else:
            string = string + i
    return string

def decode(s, n):
    encode(s,(-1)*n)