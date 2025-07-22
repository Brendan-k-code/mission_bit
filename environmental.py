#a list of prompts to ask the user
prompts = ["How many showers do you take every week?","How long is your average shower in minutes?","How many meals do you eat per day?","How many of these meals include meat?", "How many miles do you usually drive every day?"]

#empty list to store the prompts
responses = []

#a for loop that repeats all the steps below for every item in the list 'prompts'
for x in prompts:

    #takes the item in the list, and uses it to ask an input, which is then stored in the 'tempresponse' variable
    tempresponse = input(x)

    #a 'while' loop that repeats the steps under 'while' until it is no longer 'False'
    #This was made to check if the user typed a non-negative number in the response
    while tempresponse.isnumeric() == False:

        #prints a message and asks the prompt again
        print("Type a number omg")
        tempresponse = input(x)

    #when the 'tempresponse' is a number, the 'while' loop becomes true, and it goes to the steps under here
    #adds the users input into the 'responses' list
    responses.append(tempresponse)
    print (responses)
    #then the whole thing repeats until all items are done

#converts everything to floats since all the items in 'responses' are strings in the list
#calculates
truescore = float(responses[0]) * 2 * float(responses[1]) + float(responses[2]) * 21 + float(responses[3]) * 5 + float(responses[4]) * 14

#prints stuff
print("Your environmental impact is", truescore)

#conditionals for tips
if float(responses[1]) >= 30:
    print("One tip for lowering your score is taking shorter showers")
if float(responses[4]) >=40:
    print("One tip for lowering your score is driving less")
if float(responses[4]) >=150:
    print("WHERE ARE YOU GOING?!??!????")

#why
if truescore >= 10000000:
    print("stop lying 💔💔💔💔💔")





#                           yay            




















#theres nothing below this plz












#absolutely nothing



















#please vro 💔










'''
showers = input("How many showers do you take every week?")
average_shower_time = input("How long is your average shower?")
meals = input("How many meals do you eat per day?")
meat_in_meals = input("How many of these meals include meat?")
'''
#checks if the user input is a number, and not words (if it is a word, it does the steps below 'while')
#the while loop keeps asking the questions to the user until they input all numbers, which then goes to the steps under 'else'


'''
while (showers.isnumeric() == True and average_shower_time.isnumeric() == True and meals.isnumeric() == True and meat_in_meals.isnumeric() == True) == False:
    print("type a number omg") 
    showers = input("How many showers do you take every week?")
    average_shower_time = input("How long is your average shower?")
    meals = input("How many meals do you eat per day?")
    meat_in_meals = input("How many of these meals include meat?")

#then, it uses the variables to calculate the score, defined in the variable 'score'
else:
    score = int(showers) * 2 * int(average_shower_time) + int(meals) * 10 + int(meat_in_meals) * 2
    #prints the score
    print("your water usage score is ", score)
    #please take showers 💔💔💔💔💔💔💔
    if int(showers) == 0:
        print("brooooooooooooooo ur lying,..... right?!?!?!?!?") 

x = "5"
y= 3

result = x+ str(y)
print(result)
#yay it works :3

    
a=12
b=4

sum = a+b
difference = a-b
product = a* b 
quotient = a / b 
remainder = a % b
exponent = a ** b

print(sum , difference, product, quotient, remainder, exponent)
#ez

x=10
x += 5
print(x)
x-=3
print(x)
x*= 2
print(x)
x/=4
print(x)


fruits = ["apple", "watermelon", "banana", "grapes", "kiwi"]
print(fruits[-4])





'''


#what the heck bro
'''
what the hell
what the helly
what the helly
what the hellyon
what the hellyberry
what the hellyburton
what the hellybronjames
what the hellycyrus
'''