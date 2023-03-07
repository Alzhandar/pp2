import re

def text_match(text):
    regex_pattern = r'a.*b$'
    if re.search(regex_pattern, text):
        return 'True'
    else:
        return 'False'

print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))