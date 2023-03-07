import re

def text_match(text):
    regex_pattern = r'[A-Z]+[a-z]+$'
    if re.search(regex_pattern, text):
        return 'Found'
    else:
        return 'Not Found'

print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))
print(text_match('AAaaa'))