from typing import TypedDict
class person(TypedDict):
    name:str
    age:int

new_person: person = {'name':'Raman','age':27}
print(new_person)