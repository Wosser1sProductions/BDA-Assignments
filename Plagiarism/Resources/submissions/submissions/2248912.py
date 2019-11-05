import string

def encode(a_str, rotation):
    encoded_string = ""
    for char in a_str:
        if char in string.ascii_lowercase:
            encoded_string += chr((ord(char) + rotation - ord("a")) % 26 + ord("a"))
        else: 
            encoded_string += char
    return encoded_string


def decode(a_str, rotation):
    decoded_string = ""
    for char in a_str:
        if char in string.ascii_lowercase:
            decoded_string += chr((ord(char) - rotation - ord("a")) % 26 + ord("a"))
        else: 
            decoded_string += char
    return decoded_string