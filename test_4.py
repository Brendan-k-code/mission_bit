restaurants = [
    "Burger Palace",
    "Sushi World",
    "Pasta Heaven",
    "Taco Town",
    "Curry Express",
    "Vegan Delight",
    "idk, try again :P"
]

def random_restaurant(thelist:list):
    import random
    random_int = random.randint(1,len(thelist))
    print(random_int)
    tonights_pick = thelist[random_int-1]
    return tonights_pick

print("Tonight's pick is:", random_restaurant(restaurants))
#what do I do here ngl 
# i did absolutely nothing yesterday I WAS STRESSING FOR MY AP SCORE (i got a 5 :3)


students = [
    ["Alice", 95],
    ["Bob", 82],
    ["Charlie", 77],
    ["Diana", 88],
    ["Eli", 91],
    ["Fiona", 67],
    ["George", 58],
    ["Hannah", 73],
    ["Ian", 60],
    ["Jane", 85]
]

def sort_grade(thelist:list):
    A=[]
    B=[]
    C=[]
    D=[]
    F=[]
    for student in thelist:
        if student[1] >= 90:
            A.append(student[0])
        elif student[1] >=80:
            B.append(student[0])
        elif student[1] >= 70:
            C.append(student[0])
        elif student[1] >= 60:
            D.append(student[0])
        else:
            F.append(student[0])
    stara = "*" * len(A)
    print("A students:", stara)
    starb = "*"* len(B)
    print("B students:", starb)
    starc = "*"*len(C)
    print("C students:", starc)
    stard = "*"*len(D)
    print("D students:", stard)
    starf= "*"* len(F)
    print("F students:", starf)

sort_grade(students)

try:
    value = int(input("Enter a number: "))
    print("You entered:", value)
except ValueError:
    print("that wansn't a number bro")

inputs = ["10", "20", "", "abc", "30", "40", "xyz"]

listofnumbers = []
for x in inputs:
    try:
        test= float(x)
        listofnumbers.append(test)
    except ValueError:
        continue
average = sum(listofnumbers) / len(listofnumbers)
print(average)
