import re
text='Python,Java,C++.'
print(re.sub('[ ,.]',':',text))