def substring(s, frm, ln):
    woord = ""
    for k in range(ln):
        woord += (s[frm+k])
    print("'", woord, "'", sep="")
def find_pos(term, corpus):
    juist = False
    for l in range(len(term)):
        for m in range(len(corpus)):
            if term[l] == corpus[m]:
                if term == corpus[m: m+len(term)]:
                    juist = True
                    start=m
                    break
    if juist == True:
        return start
    else:
        return None
def in_string(term, corpus):
    juist = False
    for l in range(len(term)):
        for m in range(len(corpus)):
            if term[l] == corpus[m]:
                if term == corpus[m: m + len(term)]:
                    juist = True
                    start = m
                    break
    if juist == True:
        return True
    else:
        return False
