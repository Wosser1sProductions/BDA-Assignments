def substring(s, frm ,ln):
    new_string = ""
    for i in range(ln):
        new_string += s[frm]
        frm += 1
    return new_string


def find_pos(term, corpus):
    for i in range(len(corpus)-len(term)):
        sub = substring(corpus, i, len(term))
        if sub == term:
            return i

def in_string(term, corpus):
    pass