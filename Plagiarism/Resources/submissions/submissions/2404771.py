def convert(number):
    if len(number) == 1:
        return int(number[0])
    else:
        return int(number[0]) * (10**(len(number) - 1)) + convert(number[1:])