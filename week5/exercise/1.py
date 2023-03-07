import re

def text_match(text):
    regex_pattern = r'^a(b*)$'
    if re.search(regex_pattern, text):
        return 'Found a match'
    else:
        return 'No match found'

print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))