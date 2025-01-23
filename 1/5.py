import random
import os
import time

os.system("clear")

total_count = 0
win_count = 0
ai_score = 0

print("Welcome to Rock, Paper, Scissors!")
print("You need to win 3 out of 5 rounds to win the game.")
print("You can exit the game at any time by typing 'exit'.")
print("Let's begin!\n")

time.sleep(2)

os.system("clear")

while True:
  ai_choice = random.choice(["Rock", "Paper", "Scissors"])
  user_choice = input("Enter your choice (Rock, Paper, Scissors, or Exit): ")

  if user_choice.lower() == "exit":
    break

  if user_choice not in ["Rock", "Paper", "Scissors"]:
    print("Invalid choice. Please try again.")
    continue

  total_count += 1

  if user_choice == ai_choice:
    print(f"AI chose {ai_choice}.")
    print("It's a tie!")
  elif (user_choice == "Rock" and ai_choice == "Scissors") or \
       (user_choice == "Paper" and ai_choice == "Rock") or \
       (user_choice == "Scissors" and ai_choice == "Paper"):
    print(f"AI chose {ai_choice}.")
    print("You win!")
    win_count += 1
  else:
    print(f"AI chose {ai_choice}.")
    print("You lose!")
    ai_score += 1



    score_print = f"\nScore -> You: {win_count} - AI: {ai_score}"

  if win_count == 3:
    print("\nYou won the whole game!")
    print(score_print)
    print("\nThank you for playing!")
    break
  elif ai_score == 3:
    print("\nYou lost the whole game!")
    print(score_print)
    print("\nThank you for playing!")

    break
  elif total_count == 5 and win_count == ai_score:    
    print("\nGame is a draw!")
    print(score_print)
    print("\nThank you for playing!")
    break