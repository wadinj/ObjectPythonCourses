# Class
import abc

class Animal:
    
    # Optional parameter
    def __init__(self, parent = None):
        # Création d'un attribut
        self.famille = "mammifère"
        self.parent = parent
    
    # On définit une méthode sur la classe Animal
    def cry(self):
        print('Ouaaaah')

    # On définit une autre méthode sur la classe
    def make_child(self):
        # Parent is self, named parameter
        return Animal(parent=self)

    # Static method. Pas besoin d'instance pour appeler la fonction
    @staticmethod
    def has_parent(animal):
        return animal.parent is not None

# Création d'une instance
dog = Animal()

# Appel d'une méthode
dog.cry()

baby_dog = dog.make_child()

print(Animal.has_parent(baby_dog))
print(Animal.has_parent(dog))



# Héritage
class Dog(Animal):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
    
    # On définit une méthode sur la classe Animal
    def cry(self):
        print('Wouaf Wouaf')


# volvic = Dog()
# volvic.cry()
# volvic_baby = volvic.make_child()
# volvic_baby.cry()
# print(volvic.famille)

# Permet de bloquer l'instantiation
# ! Design pattern template ! (Very useful)
# Permet de définir des méthodes abstraites
class AbstractAnimal(abc.ABC):
    
    @abc.abstractmethod
    def cry(self):
        pass


class Doggy(AbstractAnimal):
    
    def cry(self):
        print('Wouaf Wouaf Doggy')

# Not possible
# animal = AbstractAnimal()

doggy = Doggy()
doggy.cry()

# Encapsulation
# Here the “state” of the cat is the private variables mood, hungry and energy. 
# It also has a private method meow(). It can call it whenever it wants, the other classes can’t tell the cat when to meow.
# What they can do is defined in the public methods sleep(), play() and feed(). 
# Each of them modifies the internal state somehow and may invoke meow(). Thus, the binding between the private state and public methods is made.

# Abstraction
# Don't share implementation details

# Polymorphism
# Not easy to show in Python. Let's demo in Java ?