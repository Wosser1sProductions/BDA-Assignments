def cleanup_spaces(string):
    current = ""
    space = False
    for i in string:
        if i != " ":
            current += i
            space = False
        elif i == " " and not(space) and len(current) != 0:
            current += i
            space = True
        elif i == " " and space:
            continue
    return current

print(cleanup_spaces(s))