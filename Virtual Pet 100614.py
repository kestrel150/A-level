#Aaron Parker
#100614
#Virtual Pet

class VirtualPet:
    """A representation of a pet."""
    #Constructor - run automatically
    def __init__(self,name):
        self.name = PetName
        print("{0} rises from the ashes!".format(self.name))

    #Methods
    def talk(self):
        print("Hi, im your virtual pet!")

def main():
    PetName = input("Please enter your new pet's name: ")
    #Creates an instance of the class
    pet_one = VirtualPet(name)
    #Call talk method
    pet_one.talk()

if __name__ == "__main__":
    main()
