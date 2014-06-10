#Aaron Parker
#100614
#Virtual Pet

class VirtualPet:
    """A representation of a pet."""

    #Methods
    def talk(self):
        print("Hi, im your virtual pet!")

def main():
    #Creates an instance of the class
    pet_one = VirtualPet()
    #Call talk method
    pet_one.talk()

if __name__ == "__main__":
    main()
