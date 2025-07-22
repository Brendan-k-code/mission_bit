 # Creating a dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# Printing the dictionary


print(country_capitals["United States"])
print(country_capitals.get("United States")) #.get will try to get something w/o sending an error
#left

country_capitals["Italy"] = "Naples"
country_capitals["China"] = "Beijing"
del country_capitals["United States"]
print(country_capitals) 

print(country_capitals.keys())


country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)


student = {
    "name": "Angel",
    "age": "15",
    "height": "about like 6'7"
}
student["age"] = "19"
student["grade"]= "A"
print(student)

