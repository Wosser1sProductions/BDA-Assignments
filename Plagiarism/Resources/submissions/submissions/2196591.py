def count_words(sentence):
    sentencewithoutpunc = ""
    for char in sentence:
        if char in """0123456789!\#$%&'()"*+,-./:;<=>?@[\]^_`{|}~':""":
            sentencewithoutpunc += " "
        else:
            sentencewithoutpunc += char

    splitsentence = sentencewithoutpunc.split()
    print(int(len(splitsentence)))



count_words("ik heb honger,hallo1slaap 51")

