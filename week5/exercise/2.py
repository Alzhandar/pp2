import re

def text_match(text):
    regex_pattern = r'ab{2,3}'
    if re.search(regex_pattern, text):
        return 'Found'
    else:
        return 'Not found'

print(text_match('ab'))
print(text_match('aabbbbbc'))
print(text_match('abb'))