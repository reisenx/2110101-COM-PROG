# Input character details until the input = 'q'
# Each line contains [Character], [Animal]
# Contains data in a dictionary 'animals_dict' and list 'unique_animals'
# animals = {Animal:[Character01 ,Character02, ...], ...}
# unique_animals = [Animal01, Animal02, ...]
unique_animals = []
animals_dict = {}
while(True):
    # Input data
    data = input().strip()
    # Check if data is 'q'. If true, then break the loop
    if(data == 'q'):
        break
    else:
        # Split an input data 
        character, animal = data.split(", ")
        # Input data to 'unique_animals'
        if(animal not in unique_animals):
            unique_animals.append(animal)
        # Input data to 'animals_dict'
        if(animal not in animals_dict):
            animals_dict[animal] = [character]
        else:
            animals_dict[animal].append(character)

# Output
for animal in unique_animals:
    line = animal + ": "
    line += ", ".join(animals_dict[animal])
    print(line)