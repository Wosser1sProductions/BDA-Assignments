def is_palindrome_sentence(sentence):
    sentence_filter = ""
    palindroom = True
    for i in range(len(sentence)):
        if sentence in alfabet:
            sentence_filter[i] += sentence[i]
    for i in range(len(sentence_filter) // 2):
        if sentence_filter[i] != sentence_filter[len(sentence_filter)-i-1]:
            return False
        return palindroom
alfabet = "abcdefghijklmnopqrstuvwxyz"
