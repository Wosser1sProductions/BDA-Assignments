import string

numbers = "123456789"
whitespace = " "
def remove(zin):
    new_string = ""
    for i in zin:
        if i in string.punctuation:
            new_string += ""
        elif i in numbers:
            new_string += ""
        elif i == whitespace:
            new_string += ""
        else:
            new_string += i
    return new_string

def is_palindrome_sentence(sentence):
    new_sentence = remove(sentence)
    reversed_sentence = ""
    for i in range(len(new_sentence)-1):
        reversed_sentence += new_sentence[len(new_sentence)-i]
    if new_sentence.lower == reversed_sentence.lower:
        return True
    else:
        return False