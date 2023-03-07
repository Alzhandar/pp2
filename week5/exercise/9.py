import re
string='LetUsStudyPython'
words=re.findall('[A-Z][a-z]*',string)
print(' '.join(words))