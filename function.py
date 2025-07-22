def guessing_game(smallest:int, biggest:int):
    import random
    secret_number = random.randint(smallest,biggest)
    small = str(smallest)
    big = str(biggest)
    guess = input("Guess a number between"+ small+ "to"+ big)
    while int(guess) >biggest or int(guess) <smallest == False or guess.isnumeric == False or int(guess) != secret_number:
        print("TRY AGAIN")
        guess = input("Guess a number between"+ small+ "to"+ big)
    if int(guess) == secret_number:
        print("YOU GUESSED IT WOW")

print("Lets play a guessing game!")
range1 = int(input("What is the smallest number that you want to guess from? "))
range2 = int(input("What is the highest number you want to guess from? "))
while type(range1) != int or type(range2) != int:
    range1 = int(input("What is the smallest number that you want to guess from?"))
    range2 = int(input("What is the highest number you want to guess from?"))
guessing_game(range1,range2) 