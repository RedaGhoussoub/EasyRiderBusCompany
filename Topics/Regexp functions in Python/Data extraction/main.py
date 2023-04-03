import re

string = input()

result = re.split(r"(<START>|<END>)", string)
print(result[2])
