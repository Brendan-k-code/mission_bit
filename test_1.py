#imports a random number generator
import random
#provides a the parameters for the ranndomly generated number
variable = random.randint(1,10)

#checks if the randomly generated number is 3
if variable == 3:

    #prints this if variable is 3
    print ("THE VARIABLE IS 3, NO WAYYYYYYY")

    #if it is not 3, it moves on to the steps in the 'else'
else:
    #prints this if not 3
    print ("THE VARIABLE IS NOT 3, NNOOOOOOO")
    
    #asks the user to type a response
    input1 = input("Type the number 3.")

    #a 'while' loop that repeats the 'input' until the input is 3
    #(if the input is not 3, bool remains False, repeating the steps under 'while')
    while bool(input1 =="3") == False: 
        #prints why  
        print ("why")

        #asking for an input from user
        input1 = input("Type the number 3.")

        #once 3 has been typed in the input, the bool becomes True, and it goes to the steps in 'else'
    else:
        #turns the variable into 3
        variable = 3

        #prints this message :3
        print ("the variable is 3 now yay :3")
        

FavoriteDriverlessCar= input("What is your favorite driverless car?")

#don't mind anything I typed above this bro please please please

print ("Brendan")
CarName = "Brendan"

#hello hello hello hello hello hello hello hello 

'''
My name is Brendan, my pronouns are he/him
I don't know what I am writing this comment but I'm typing just to look busy not gonna lie

My favorite movie so far is Top Gun: Maverick :O

Things we learned today (6/24)
- input
- defining variables
- basic syntax 
- print
- expressions vs statements
- hella community builders
'''




'''




'''


list = [ 
    [1,2,3],
    [4,5,6]
]

print(list[1][1])


for x in range(1,21):
    if x % 3 == 0:
        print (x, "is divisible by 3 :3")


jungle = ["tiger", "snake", "bear", "gorilla", "exit"] 
for animal in jungle: 
   if animal == "exit": 
      print("You've reached the exit. Safe now!") 
      break 
   elif animal == "gorilla": 
      print("A gorilla appeared! Stay calm and be quiet.") 
      continue 
   print("Encountered", animal, "- Be careful!")

# def greet_customer():
#     print("Hello,   this " \
#     "is cool" \
#     "ok" \
#     "very ")

# greet_customer() 


def greet_customer(special_today, store):
   print("Welcome to" , store)
   print("Our special is", special_today)
   print("Ask if you need anything!")
print("Cleanup on aisle 6")
greet_customer("me", "mystore")
greet_customer("nothing", "notmystore")

def my_function(integer1:int, integer2: int):
    print(integer1+integer2)

my_function(2,1)

def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2



x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)

print(type(square_point(1,3)))

def guessing_game(smallest:int, biggest:int):
    import random
    secret_number = random.randint(smallest,biggest)
    small = str(smallest)
    big = str(biggest)
    guess = input("Guess a number between", small, "to", big)
    while int(guess) >biggest or int(guess) <smallest == False or guess.isnumeric == False or int(guess) != secret_number:
        print("TRY AGAIN")
        guess = input("Guess a number between", smallest, "to", biggest)
    if int(guess) == secret_number:
        print("YOU GUESSED IT WOW")

print("Lets play a guessing game!")
range1 = input("What is the smallest number that you want to guess from?")
range2 = input("What is the highest number you want to guess from?")
while range1.isnumeric == False or range2.isnumeric == False:
    range1 = int(input("What is the smallest number that you want to guess from?"))
    range2 = int(input("What is the highest number you want to guess from?"))
guessing_game(range1,range2)







