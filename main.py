import random

user = input("Hello!, What is your Name?: ")

question = input("Hello " + user + " What would you like to know? (Yes or No Question): ")

random_number = random.randint(1, 9)

#print(random_number)

#Manual If then-else statements

if random_number == 1:
  answer = "Definetly"
elif random_number == 2:
  answer = "Maybe"
elif random_number == 3:
  answer = "Of course!"
elif random_number == 4:
  answer = "Try again please"
elif random_number == 5:
  answer = "Confusing, could you try again?"
elif random_number == 6:
  answer = "Better If I don't tell you"
elif random_number == 7:
  answer = "Very doubtfull"
elif random_number == 8:
  answer = "I don't think so"
elif random_number == 9:
  answer = "Not at all"

#Chat bot prints the answer

print("ChatBOT Answer: " + answer)


