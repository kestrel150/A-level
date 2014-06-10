#Aaron Parker
#100614
#Virtual Pet

class VirtualPet:
    """A representation of a pet."""
    #Constructor - run automatically
    def __init__(self,name):
        self.name = name
        self.hunger = 100
        print("{0} rises from the ashes!".format(self.name))

    #Methods
    def talk(self):
        print("Hi, im your virtual pet!")
    def hunger_status(self):
        print("Hunger is {0}.".format(self.hunger))

def main():
    name = input("Please enter your new pet's name: ")
    #Creates an instance of the class
    pet_one = VirtualPet(name)
    choice = 0
    while choice != "Q":
        choice = int(input("Please make your choice: "))
        if choice == 1:
            pet_one.talk()
        if choice == 2:
            pet_one.hunger_status()
        
    #Call talk method
    pet_one.talk()

if __name__ == "__main__":
    main()
