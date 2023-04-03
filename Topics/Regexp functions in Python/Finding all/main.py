import re

template = r"(s\w*)"
result = re.findall(template, input())
print(result)
