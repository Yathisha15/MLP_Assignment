import random

def user_choice () :
  user_choice = input("Enter your choice (Rock/Paper/Scissors): ")
  return user_choice

def computer_choice():
  choices = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(choices)
  print(f"The computer choice is {computer_choice}")
  return computer_choice

def winner(user,computer) :
  if user == computer:
        return "It's a tie!"
  elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        return "You win!"
  else:
        return "Computer wins!"


print("Welcome to Rock, Paper, Scissors Game!")
user = user_choice()
computer = computer_choice()

game_winner = winner(user,computer)
print(game_winner)
