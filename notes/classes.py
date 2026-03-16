#EHCP2 classes

#example 1
class Dog:
    def __init__(self, names, breeds, age):
        self.names = names.capitalize()
        self.breeds = breeds.title()
        self.age = age

    def __str__(self):
        return f"Name: {self.names}\nBreed: {self.breeds}\nAge: {self.age}"
    
    def speak(self, words):
        return f"{self.names}: {words} "

doug = Dog("Doug", "Golden Retreiver", 3)
pongo = Dog("Pongo", "Dalmation", 8)

print(doug)
print(pongo)
while True:
    print(doug.speak("huh?"))
    print(pongo.speak("what?"))