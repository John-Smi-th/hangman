import random

def hangman():
    list1 = ["cat","dog","bard","mice"]
    randomnumber = random.randint(0,3)
    word = list1[randomnumber]
    wrong = 0
    stages = ["","______      ", "|           ", "|      |    ","|      0    ","|    / | \  ","|    /   \  ","|           "]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to hangman!")
    while wrong < len(stages)-1:
	      print("\n")
	      msg = "Guess a word:"
	      char = input(msg)
	      if char in rletters:
	          cind = rletters.index(char)
	          board[cind] = char
	          rletters[cind] = '$'
	      else:
	          wrong +=1
	          
	      print("".join(board))
	      e=wrong+1
	      print("\n".join(stages[0:e]))
	      if "_" not in board:
	          print("You win!")
	          print(" ".join(board))
	          win = True
	          break
    if not win:
	          print("\n".join(stages[0:wrong+1]))
	          print("You lose! Answer is {}".format(word))
