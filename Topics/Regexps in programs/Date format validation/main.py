import re

string = input()
pattern = r"^([0-2][1-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)([1-2][0-9][0-9][0-9])$"
result = re.match(pattern, string)
if result:
    print(True)
else:
    print(False)
