def count_words(string):
    niet = ',.?;:/![]^*<>&"()'
    getal = "0123456789"
    lijst = string.split()
    teller = 0
    for i in lijst:
        if i in getal:
            teller = 0
            continue
        for j in i:
            if j in niet or j in getal:
                teller += 1
        teller += 1
    return teller