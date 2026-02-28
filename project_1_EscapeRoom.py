import random
max_lives = 3

def intro():
    print("Welcome to Escape Room")
    print("Solve the challenges using logic to escape")
#door 1
def door_1_math_puzzle():
    answer = int(input("Door 1: What is 7*6 + 8"))
    if answer == 50:
        return True
    else:
        return False
#door 2
def door_2_pattern_puzzle(attempts=2):
    secret = "mystery"
    tries = 0
    while tries < attempts:
        guess = input("Door 2: Guess the secret word:").lower()

        if guess == "":
            continue
        if guess == secret:
            return True

        tries += 1
        print("Wrong guess!")


    return False

#door 3
def door_3_code(start=1,end = 5):
    lucky =random.randint(start,end)
    for i in range(2):
        guess = int(input("Door 3: Guess the lucky number(1-5):"))
        if guess == lucky:
            return True
    return False
def reward_badges(*badges):
    """Variable length arguments"""
    return random.choice(badges)

def escape_room():
   """Main Game engine (infinite loop)"""
   lives = max_lives
   collected_badges = set()

   while True:
       print("\n Choose a door:")
       print("1. Math Door")
       print("2. Pattern Dooor")
       print("3. Lucky Door")
       print("4. Exit Game")

       choice = input("Your choice:")

       if choice == "1":
           if door_1_math_puzzle():
               collected_badges.add(reward_badges("Logic Master" , "Math Whiz"))
               print("Door unlocked!")
           else:
               lives -= 1

       elif choice == "2":
           if door_2_pattern_puzzle():
               collected_badges.add(reward_badges("Pattern Pro","Code Breaker"))
               print("Door unlocked!")
           else:
               lives -= 1

       elif choice == "3":
           if door_3_code():
               collected_badges.add(reward_badges("Lucky Star" , "Risk Taker"))
               print("Door unlocked!")
           else:
               lives -= 1
       elif choice == "4":
           break
       else:
           print("Invalid door!")

       print(f"Lives Left: {lives}")
       print(f"Badges collected: {collected_badges}")

       if lives == 0:
           print("game over")
           break

   print("escape room ended. thanks for playing!")


def main():
    intro()
    escape_room()

print(main())











