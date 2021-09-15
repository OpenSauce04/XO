from os import system # Used to clear the screen; WHY ISN'T THIS A BASE FUNCTION IN PYTHON?!
from easy_getch import getch # Used to detect keystrokes
from random import randint # Used to pick moves for bot opponent

from wincons import wincons # Win condition arrays

while True: # Main loop
  system("cls")
  board = ["", ' ',' ',' ',' ',' ',' ',' ',' ',' ',] #Skips value 0
  winner = ''
  def drawBoard():
    print(" " + board[7] + ' ║ ' + board[8] + ' ║ ' + board[9]) #There is definitely a better way of doing this
    print("═══╬═══╬═══")
    print(" " + board[4] + ' ║ ' + board[5] + ' ║ ' + board[6])
    print("═══╬═══╬═══")
    print(" " + board[1] + ' ║ ' + board[2] + ' ║ ' + board[3])

  while True:
    drawBoard()

    # Player Turn
    print("Press your selected space on the number pad")
    while True:
      try:
        userinput = int(str(getch())[2]) # Get entered character

        if board[userinput] == ' ':
          board[userinput] = "X" # Player is ALWAYS X
          break
        else:
          system("cls")
          drawBoard()
          print("Press your selected space on the number pad")
          print("Space is taken")

      except:
        system("cls")
        drawBoard()
        print("Press your selected space on the number pad")
        print("Invalid input")
        continue

    # Bot turn
    botinput = randint(1,9)
    botattempts = 0
    while board[botinput] != ' ':
      botinput = randint(1,9)
      botattempts+=1
      if botattempts>100:
        break
    if not botattempts>100:
      board[botinput] = 'O' # Bot is ALWAYS O


    # Checking for a win condition
    for p in ['X','O']: # Player
      for w in range(0,len(wincons)-1): # Win condition index
        matches = 0
        for x in range(1,9): # Board position
          if (board[x]==p) and (wincons[w][x-1]==1):
            matches += 1
        if matches == 3:
          break
      if matches == 3:
        break
    if matches == 3:
      winner = p
      break
    if not ' ' in board:
      break
    system("cls")

  # The match has ended
  system("cls")
  drawBoard()
  if winner == '':
    print("Nobody won!")  
  else:
    print(winner + " won!")

  print("\nPress any key to try again")
  getch()