import re;
result=re.findall(r'\b(\w+ов)\b', 'строка, состоящая из пробелов, слов, знаков препинания')
print(result)