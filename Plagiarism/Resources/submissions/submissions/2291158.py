def is_ordered(l):
    vorige = l[0]
    for getal in l:
        if getal >= vorige:
        vorige = getal    
        continue
        elif vorige = '':
            return
        else:
            return False
    return True
