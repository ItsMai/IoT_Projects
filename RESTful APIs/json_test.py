# Mailani Gelles / Emily Kuo 
# github.com/usc-ee250-fall2019/lab05-emily-mailani
import json

# json library: https://docs.python.org/3.5/library/json.html

person = {
    'name': 'Tommy Trojan',
    'email': 'tommy@usc.edu',
    'phone': '213-740-2311',
    'nicknames': [
        'Tommy T',
        'Spirit of Troy',
    ],
}

print(type(person))
print(person)

person_json = json.dumps(person)
print(person_json)

# TODO: What type is person_json?
print(type(person_json))
# TODO: Pretty printing
person_json = json.dumps(person, sort_keys=False, indent=4)
print(person_json)