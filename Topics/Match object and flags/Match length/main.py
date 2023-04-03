import re

template = r'are you ready??.?.?'
any_match = re.match(template, input())

if any_match:
    print(len(any_match.group()))
else:
    print(0)
