def convert_to_uppercase(s):
    distance = ord('a') - ord('A')
    
    for x in range(len(s)):
        if s[x] >= 'a' and s[x] <= 'z':
            s = s[:x] + chr(ord(s[x])-distance) + s[x+1:]
    
    return s