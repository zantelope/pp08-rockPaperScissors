https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html


import sys

def choice(num):
  choice = input("Player " + str(num) + ": rock, paper, or scissors?")
  choice = choice.lower()
  if choice != "rock" and choice != "paper" and choice != "scissors":
    print ("Invalid entry")
  else:
    return choice

def compare(p1c, p2c):
  print()
  print("Player 1 chooses " + p1c + ".")
  print("Player 2 chooses " + p2c + ".")

  if p1c == p2c:
    print ("Tie.\n")

    compare(p1_choice, p2_choice)
  else:
    if p1c == "rock":
      if p2c == "scissors":
        return("Player 1 wins.")
      else:
        return("Player 2 wins.")
    if p1c == "paper":
      if p2c == "rock":
        return("Player 1 wins.")
      else:
        return("Player 2 wins.")
    if p1c == "scissors":
      if p2c == "paper":
        return("Player 1 wins.")
      else:
        return("Player 2 wins.")
  
  answer_valid = False
  while answer_valid == False:
    answer = input("Play again? (y/n")
    if answer.lower != "y" and answer.lower != "n":
      print ("Invalid answer")
    elif answer.lower() == "y":
      answer_valid = True
      play()
    elif answer.lower() == "n":
      sys.exit


def play():

  p1_choice = choice(1)

  p2_choice = choice(2)

  print(compare(p1_choice, p2_choice))





play()
