def substring(s, frm, len):
    result = ""
    for i in range(frm, frm + len):
        result = result + string[i]

def find_pos(term, corpus):
    end = len(corpus) - len(term) + 1
    for i in range(0, end):
        sub = substring(corpus, i, len(term))
        if term == sub:
            return i

def in_string(term, corpus):
    return find_pos(term, corpus) != None