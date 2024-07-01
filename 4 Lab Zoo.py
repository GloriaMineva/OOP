class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fishes':
            self.fishes.append(name)
        elif species == 'birds':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif species == 'fishes':
            result += f'Fishes in {self.name}: {", ".join(self.fishes)}\n'
        elif species == 'birds':
            result += f'Birds in {self.name}: {", ".join(self.birds)}\n'

        result += f'Total animals: {Zoo.__animals}'
        return result


user_zoo_name = input()
instance_zoo = Zoo(user_zoo_name)
animals_count = int(input())
for i in range(animals_count):
    species, animal = input().split(' ')
    instance_zoo.add_animal(species, animal)

user_species = input()
print(instance_zoo.get_info(user_species))