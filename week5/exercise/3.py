import re

def text_match(text):
    regex_pattern = r'^[a-z]+_[a-z]+'
    if re.search(regex_pattern, text):
        return 'Found'
    else:
        return 'Not found'

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))