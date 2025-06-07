import random
num = random.randint(1,100)
print('WELCOME TO GUESS ME GAME!')
print("I'm thinking of a number betweeen 1 and 100.")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD!")
print("If your guess is within 10 of my number, I'll tell you you're WARM!")
print("If your guess is farther away than your most recent guess, I'll say You're getting colder!")
print("If your guess is closer than your most recent guess, I'll say You're gettting warmer!")
print("Let's Play!")
guesses = [0]
while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n What is your guess? "))
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS! Please try again: ")
        continue
    if guess == num:
        print(f'CONGRATULATIONS! YOOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break 
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    #when testing our first guess, guesses [-2]==0, which evaluated to False
    # and brings us down to the second section 
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("WARMER! ")
        else:
            print("COLDER! ")
    else:
        if abs(num-guess) <= 10:
            print("WARM! ")
        else:
            print("COLD! ")