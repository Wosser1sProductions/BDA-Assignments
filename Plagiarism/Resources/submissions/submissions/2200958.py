def encode(s, n):
    niet = ''',?;.:/"<>[]^!'“”’ '''
    nieuw = ""
    for i in s:
        if i in niet:
            nieuw += i
        else:
            getal = ord(s) + n
            nieuw += chr(getal)
    return nieuw


def decode(s, n):
    pass