def substring(s, frm, ln):
    for i in range(len(s)):
        if i == frm:
            return s[i:i+ln]

def find_pos(term, corpus):
    ln = len(term)
    for frm in len(corpus)-ln:
        if substring(s, frm, ln) == term:
            return frm
    
def in_string(term, corpus):
    if find_pos(term, corpus) != None:
        return True
    return False