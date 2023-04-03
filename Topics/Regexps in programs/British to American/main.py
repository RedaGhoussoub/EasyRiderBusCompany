import re

string = input()
string = re.sub(r'ou(?=\w+)', 'o', string)
print(string)
