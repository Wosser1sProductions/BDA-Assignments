def cleanup_spaces(string):
    cleaned = ""
    place = -1
    for letter in string:
        place = place + 1
        part = string[place:]
        if part in " ":
            break
        if letter == " ":
            if string[place + 1] == " ":
                continue
            else:
                cleaned = cleaned + " "
        else:
                cleaned = cleaned + letter
    if cleaned[0] == " ":
        cleaned = cleaned[1:]
    return cleaned