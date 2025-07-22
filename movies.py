movies = [
    ["Thunderbolts", "7.5", "Action"],
    ["The Dark Knight", "9.0", "Action"],
    ["Loki", "8.2", "Sci-Fi"],
    ["Captain America: Brave New World", "5.6", "Action"],
    ["The Emoji Movie", "3.4", "Animation"],
]


addmovie = input("Do you want to add a movie to this list? Type Y or N:")
while addmovie == "Y":
    newtitle = input("What is the movie title?")
    newrating = input("What is the rating of the movie?")
    while newrating.isnumeric() == False or float(newrating) > 10:
        print("type an actual number bro")
        newrating = input("What is the rating of the movie?")
    newgenre = input("What is the genre of the movie?")
    movies.append([newtitle, newrating, newgenre])
    print(movies)
    addmovie = input("Do you want to add another movie? Type Y or N")

# score analysis
sumofscores = 0
highscore = 0
for movie in movies:
    sumofscores += float(movie[1])
    if float(movie[1]) >= highscore:
        highscore = float(movie[1])
        highmovie = movie[0]
    if float(movie[1]) >= 8:
        print(movie[0], "is a good movie, with a rating of", movie[1])
    elif float(movie[1]) >= 5 and float(movie[1]) < 8:
        print(movie[0], "is an ok movie, with a rating of", movie[1])
    else:
        print(movie[0], "is a bad movie :(, with a rating of", movie[1])
print("")
print("The total score added for all of these movies is", sumofscores)
print(
    "The highest rated movie was", highmovie, "which was rated", highscore, "out of 10"
)
print("")  # lol


# genre sorting
def filter_by_genre(fulllist):
    # makes an empty list to put stuff in
    genrelist = []

    # for every term in the list given in the parameter, it appends the genre to the empty list
    for movie in fulllist:
        genrelist.append(movie[2])

    unique_list = list(set(genrelist))
    listsoflists = []
    for list1 in unique_list:
        listsoflists.append([list1])
    for list2 in listsoflists:
        for movie in fulllist:
            if list2[0] == movie[2]:
                list2.append(movie[0])
    for x in listsoflists:
        del x[0]
    return listsoflists


# find average ratings
def calculate_average_rating(ratings: list):
    ratinglist = []
    totalrating = 0
    for movie in ratings:
        ratinglist.append(movie[1])
    for number in ratinglist:
        totalrating += float(number)

    average = totalrating / len(ratinglist)
    formataverage = "The average rating is " + str(average)
    return formataverage


def find_highest_rated(ratings: list):
    ratinglist = []
    bestrating = 0
    for movie in ratings:
        ratinglist.append(movie[1])
    for rating in ratinglist:
        if float(rating) >= float(bestrating):
            bestrating = rating
    formatbestrating = "The best movie has the rating of " + str(bestrating)
    return formatbestrating


print(filter_by_genre(movies))
print(calculate_average_rating(movies))
print(find_highest_rated(movies))


def modify_movieslist(filename: str):
    import csv

    with open(filename + ".csv", "r") as source:
        reader = csv.reader(source)

        with open("output.csv", "w") as result:
            writer = csv.writer(result)
            for r in reader:
                if r[6] != "" or r[6].isnumeric == True:
                    writer.writerow((r[1], r[6], r[5]))


def readmovieslist():
    import csv

    actuallist = []
    with open("output.csv", "r") as source:
        reader = csv.reader(source)

        for r in reader:
            actuallist.append(r)
    return actuallist


modify_movieslist("animation")
biglist = readmovieslist()
print(biglist)

print(filter_by_genre(biglist))
print(calculate_average_rating(biglist))
print(find_highest_rated(biglist))


def save_analysis(data: list):
    a = filter_by_genre(data)
    b = calculate_average_rating(data)
    c = find_highest_rated(data)
    import csv

    with open("analysis.csv", "w") as result:
        writer = csv.writer(result)
        writer.writerow(a)
        writer.writerow(str(b))
        writer.writerow(str(c))


save_analysis(biglist)
