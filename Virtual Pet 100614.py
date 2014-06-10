#Aaron Parker
#100614
#Virtual Pet

class VirtualPet:
    """A representation of a pet."""
    #Constructor - run automatically
    def __init__(self,name):
        self.name = name
        self.hunger = 100
        self.food = 5
        print("{0} rises from the ashes!".format(self.name))

    #Methods
    def talk(self):
        if self.hunger >= 5:
            print("Hi, im your virtual pet!")
            self.hunger = self.hunger - 5
        else:
            print("{0} cannot speak, it is too hungry. (hunger = {1})".format(self.name,self.hunger))
        
    def hunger_status(self):
        print("Hunger is {0}.".format(self.hunger))
        feed = input("Would you like to feed {0}[Y/N]? (amount of food = {1}) ".format(self.name,self.food))
        if feed = "Y":
            self.hunger = 100
            self.food = self.food - 1
        else:
            print("You chose not to feed your pet")

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
