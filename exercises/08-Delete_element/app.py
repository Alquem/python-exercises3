people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    people_without_person_name = []
    for person in people:
        if person_name != person:
            people_without_person_name.append(person)
    return people_without_person_name
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))