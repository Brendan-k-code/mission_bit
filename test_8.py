fruits = ["apple", "banana", "cherry", "date"]
person = {
    "name": "Bob", 
    "age": 25, 
    "city": "Chicago"
}
print(fruits[2])
print(person["age"])

dict = {"name": "Alice"}
# print(dict["age"]) 
print(dict.get("age")) 

word = "hello"
print(word.upper())

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!")

#name of class is Dog

#__init__ initializes the class with all of its parameters
#bark is a defined function inside the class

#self means that it is refering to its own class

dog1 = Dog("Bingo")
dog1.bark()

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name + " says meow!")



#self not defined
#not indented correctly
#cat not capital 

cat1 = Cat("whiskers")
cat1.meow()

#A class is a blueprint that lets you create new objects using the same format
#an object in python is a specific instance of a class when innputted
#__init__ initializes the required parameters and defines what they are
#the main goal of OOP is to organize and structure code

#A

#c
#c

#b
#d

#

class Note:
    def __init__(self, content):
        self.content = content

    def show(self):
        print(f"Note: {self.content}")

class Notebook:
    def __init__(self):
        self.notes = []  # list to hold Note objects

    def add_note(self, note):
        self.notes.append(note)

# Example usage:
note1 = Note("Buy milk")
note2 = Note("Finish homework")

notebook = Notebook()
notebook.add_note(note1)
notebook.add_note(note2)
print(notebook)

# a python library is a collection of external functions that you can import and use, such as random, pillow and more

class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Cat named {self.name}"

class Owner:
    def __init__(self, cat):
        self.cat = cat
    def __str__(self):
        return f"Owner of the {self.cat}"

cat1 = Cat("Whiskers")     
owner = Owner(cat1)            
print(owner.cat.name)    
print(cat1)
print(owner)
