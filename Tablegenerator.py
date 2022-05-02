from openpyxl import Workbook
import json
import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

workbook = Workbook()
sheet = workbook.active

gender = ["male", "female"]

names = json.loads(open('names.json').read())

lastnames = json.loads(open('lastnames.json').read())

i = 1

sheet["A1"] = "ID"
sheet["B1"] = "Name"
sheet["C1"] = "Nickname"
sheet["D1"] = "E-Mail"
sheet["E1"] = "Password"
sheet["F1"] = "Birthday"
sheet["G1"] = "Gender"

for name in names:
    i += 1
    lastname = random.choice(lastnames)

    sheet["A" + str(i)] = str(i)
    sheet["B" + str(i)] = name + " " + lastname
    sheet["C" + str(i)] = name + "." + lastname + str(i) + str(random.randint(1, 999))
    sheet["D" + str(i)] = name + lastname + str(i) + str(random.randint(1, 999)) + "@protonmail.com"
    sheet["E" + str(i)] = str(random.randint(999, 9999999999)) + random_string_generator(size=8)
    sheet["F" + str(i)] = str(random.randint(1, 30)) + "." + str(random.randint(1, 12)) + "." + str(random.randint(1980, 2003))
    sheet["G" + str(i)] = random.choice(gender)

workbook.save(filename="accounts.xlsx")
