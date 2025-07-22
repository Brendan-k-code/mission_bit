class Pet:
    def __init__(self, name, animal_type, hunger=0, happiness=100):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
        self.happiness = happiness

    def eat(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0 
        print(f"{self.name} has eaten. Hunger is now {self.hunger}.")

    def play(self):
        self.happiness += 10
        self.hunger += 7
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} has played. Happiness is {self.happiness}, and hunger is {self.hunger}")
    
    def status(self):
        print(f"The pet's name is {self.name} and it is a {self.animal_type}. It currently has {self.hunger} hunger and {self.happiness} happiness.")

pet1 = Pet("test", "cat")
pet1.eat()
pet1.play()
pet1.status()

numofpets = input("How many pets do you want to have?")
print(numofpets)
while numofpets.isnumeric() == False:
    print("type a number")
    numofpets = input("How many pets do you want to have?")
intnumofpets = int(numofpets)

listofpets = []
for pet in range(1,intnumofpets+1):                  
    petname = input("What is this pet's name?")
    pettype = input("What type of pet is this? (cat, dog, etc.)")
    pet = Pet(petname,pettype)
    listofpets.append(pet)

print(listofpets[0])
listofpets[0].status()

while exit == False:
    print("What would you like to do?")