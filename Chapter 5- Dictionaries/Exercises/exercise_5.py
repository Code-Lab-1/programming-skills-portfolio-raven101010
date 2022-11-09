#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet


pets = []


pet = {
    'animal type': 'dog',
    'owner name': 'Raven',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'owner name': 'Adhenz',
}
pets.append(pet)

pet = {
    'animal type': 'parrot',
    'owner name': 'Patrick',
}
pets.append(pet)


for pet in pets:
    print(f"\nAbout " + pet['animal type'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))