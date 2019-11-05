def relativechar(string, i):
    length_string = len(string)
    
    if i >= len(string):
        while i >= len(string):
            i = i - len(string)
        
    return(string[i])


def create_sequence(string, index, length):
    word = ""
    if index < 0:
        index = -index - 2
    
    for i in range(index, index+length):
        word = word + relativechar(string, i)

    return word