#Parant class
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("sound")
            
 #child class
class dog(Animal):
    def __init__(self, breed):
        self.breed = breed
        super().__init__("species")

    def speak(self):
        print("barks")

#create object
myDog =dog("lordbarn")
myDog.speak()


