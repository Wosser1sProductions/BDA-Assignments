def substring(s, frm, ln):
    lengthe = len(s)
    start = int(frm)
    aantal = int(ln)
    uitkomst =""
    for i in range(0,aantal):
        uitkomst += s[(frm+i)]
    return uitkomst

def find_pos(term, corpus):
    letter = term[0]
    lengthe = len(corpus)
    for i in range(0,lengthe):
        if letter == corpus[i]:
            return i
        

def in_string(term, corpus):
    if find_pos(term,corpus) == None:
        return False
    else:
        return True