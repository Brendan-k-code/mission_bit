user_input = "Python"
if user_input.lower() == "python":
    print("Match!")
else:
    print("No match.")

fruits = ["apple", "banana", "cherry", "date"]
check = 0
user_input = input("Enter a fruit name: ")
for fruit in fruits:
    new = user_input.lower()
    if new == fruit:
        print("fruit is found :3")
        check +=1
if check != 1:
    print("fruit not found :(")


data = "apple,banana,cherry"
newdata = data.split(",")
print(newdata)



data = "Apple, Banana, Cherry"
fruits = data.split(",")
print(fruits) # split() without strip()

clean_fruits = [] 

for fruit in fruits:
    clean_fruits.append(fruit.strip())  

print(clean_fruits) # split() with strip()












books = [
    ["The Hobbit", "J.R.R. Tolkien", "Fantasy"],
    ["1984", "George Orwell", "Dystopian, Science Fiction"],
    ["To Kill a Mockingbird", "Harper Lee", "Fiction, Drama"],
    ["The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy, Adventure"],
    ["Brave New World", "Aldous Huxley", "Dystopian, Science Fiction"],
    ["Pride and Prejudice", "Jane Austen", "Romance, Classic Literature"],
]

# Define a function to filter books by genre
def filter_books_by_genre(target_genre):
    matching_books = []  # Create an empty list to store results

    # Loop through each book in the list
    for book in books:
        genre_string = book[2]  # The genre field (may contain multiple genres)
        newlist = genre_string.split(",")
        for genre in newlist:
            newgenre = genre.strip()
            if str(newgenre.lower()) == str(target_genre.lower()):
                matching_books.append(book[0])
        # TODO: Split genre_string by comma into a list of genres
        # TODO: Loop through each genre in the list
            # TODO: Strip spaces and compare it (lowercase) with target_genre (also lowercase)
            # TODO: If there's a match, add the book to matching_books and break

    return matching_books


# Example usage
results = filter_books_by_genre("Science Fiction")
print(results)
# Print the matching books
# for book in results:
#     print(f"{book[0]} by {book[1]} — {book[2]}")