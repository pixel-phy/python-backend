class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("Whoof, whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

owner1 = Owner("Danny", "122 Springfield Drive", "888-999")
dog1 = Dog("Bruce", "Scottish Terrier", owner1)
print(dog1.owner.name)
dog1.bark()
print(dog1.name)
print(dog1.breed)

owner2 = Owner("Sally", "122 Springfield Drive", "777-666")
dog2 = Dog("Freya", "Greyhound", owner2)
print(dog2.owner.name)
dog2.bark()
print(dog2.name)
print(dog2.breed)
