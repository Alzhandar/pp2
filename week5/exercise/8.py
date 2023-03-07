import re
text = "PythonTutorialAndExercises"
result = re.findall(r'[A-Z][^A-Z]*',text)
print(result)