def sentence_without_punctuation(string):
    sent_without_punct = ""
    punctuation = """!?,.; :"'"""
    for letter in string:
        if letter not in punctuation:
            sent_without_punct += letter
            continue
        if sent_without_punct == "":
            return ""
    return sent_without_punct

def sentence_without_heading(string3):
    string3 = sentence_without_punctuation(string3)
    return string3.lower()
def is_palindrome_sentence(string2):
    string2 = sentence_without_heading(string2)
    x = 0
    if string2 == "":
        return True
    while x < len(string2) - 1:
        if string2[0+x] == string2[len(string2)-1-x]:
            x += 1
        else:
            return False
        return True