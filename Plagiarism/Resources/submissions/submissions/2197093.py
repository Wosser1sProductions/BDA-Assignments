punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789 "

def remove_punctuation(sentence):

    s_sans_punct = ""
    for letter in sentence:
        if letter not in punctuation:
            s_sans_punct += letter
        else:
            s_sans_punct += " "
    return s_sans_punct


def is_palindrome_sentence(sentence):
    n = len(sentence)
    x = 1
    if sentence[0] == sentence[n - 1]:
        if sentence[0 + x] == sentence[n - 1 - x]:
            print("True")
    else:
        print("False")