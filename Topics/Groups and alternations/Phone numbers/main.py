import re

string = input()
template = r"^\+(\d)[- ]?(\d{3})[- ]?(.*)"

result = re.match(template, string)

if result:
    country_code, area_code, number, = result.groups()
    print(f"Full number: {string}")
    print(f"Country code: {country_code}")
    print(f"Area code: {area_code}")
    print(f"Number: {number}")
else:
    print("No match")