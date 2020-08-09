from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self, species, shape, character):
        self.species = species
        self.shape = shape
        self.character = character

    @property
    def is_raptor(self):
        if self.species == 'eat-meat' and self.character == 'ferocious' and (self.shape == 'M' or self.shape == 'L'):
            return True
        return False


class Cat(Animal):

    sound = 'miaomiao'
    
    def __init__(self, name, species, shape, character):
        self.name = name
        super().__init__(species, shape, character)

    @property
    def is_pet(self):
        if self.character == 'mild' and self.shape == 'S':
            return True
        else:
            return False


class Zoo:

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal):

        animal_id = id(animal)
        animal_class_name = animal.__class__.__name__

        if animal_id in self.animals:
            print (f'Animal with id {animal_id} already added')
            return
        else:
            self.animals[animal_id] = animal
           

if __name__ == '__main__':

    z = Zoo('time-zoo')
    cat1 = Cat('big-cat', 'eat-meat', 'M', 'mild')
    z.animals('cat1')

