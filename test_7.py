class Smartphone:
    def __init__(self, brand="mephone", model="mine", storage=0):  # Class constructor
        self.brand = brand  # Initializes brand
        self.model = model  # Initializes model
        self.storage = storage  # Initializes storage

    def display_info(self):  # Method to display smartphone info
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB")


# Creating two objects
my_phone = Smartphone("Apple", "iPhone 13", 128)
your_phone = Smartphone("Samsung", "Galaxy S22", 256)
the_other_phone = Smartphone()
# Using a method to display info about the phones
my_phone.display_info()  # Outputs -> Smartphone: Apple iPhone 13, Storage: 128GB
your_phone.display_info()  # Outputs -> Smartphone: Samsung Galaxy S22, Storage: 256GB
the_other_phone.display_info()
#:333


class Book:
    def __init__(self, title="mybook", author="me", year=2):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"The book is {self.title} by {self.author} published in {self.year}")

    def is_classic(self):
        if self.year <= 1970:
            print(f"True, this book is a classic, published in {self.year}")

    def __str__(self):
        return str(self.__dict__)
        # return repr(self)


book1 = Book("1984", "George Orwell", 1949)
book1.describe()
book1.is_classic()

book2 = Book()
book2.describe()
print(book1.__dict__)
print(book1)

# meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow m
