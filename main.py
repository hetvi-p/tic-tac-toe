import randomx

def winner(board):
  """This function accepts the Tic-Tac-Toe board as a parameter.  
  If there is no winner, the function will return the empty string "".  
  If the user has won, it will return 'X', and if the computer has
  won it will return 'O'."""

  # Check rows for winner
  for row in range(3):
    if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] !=
                                                              " "):
      return board[row][0]

  # Check columns for winner
  for col in range(3):
    if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] !=
                                                              " "):
      return board[0][col]

  # Check diagonal (top-left to bottom-right) for winner
  if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != " "):
    return board[0][0]

  # Check diagonal (bottom-left to top-right) for winner
  if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != " "):
    return board[0][2]

  # No winner: return the empty string
  return ""


def display_board(board):
  """This function accepts the Tic-Tac-Toe board as a parameter.  
  It will print the Tic-Tac-Toe board grid (using ASCII characters)
  and show the positions of any X's and O's.  It also displays
  the column and row numbers on top and beside the board to help
  the user figure out the coordinates of their next move.  
  This function does not return anything."""

  print("   1   2   3")
  print("1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
  print("  ---+---+---")
  print("2: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
  print("  ---+---+---")
  print("3: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
  print()


def make_user_move(board):
  """This function accepts the Tic-Tac-Toe board as a parameter.  
  It will ask the user for a row and column.  If the row and
  column are each within the range of 1 and 3, and that square
  is not already occupied, then it will place an 'X' in that square."""

  #The try statement ensures that no exception occurs if user enters a string
  valid_move = False
  while not valid_move:
    try:
      row = int(input("What row would you like to move to (1-3):"))
      col = int(input("What col would you like to move to (1-3):"))
      if (1 <= row <= 3) and (1 <= col <= 3) and (board[row - 1][col - 1]
                                                  == " "):
        board[row - 1][col - 1] = 'X'
        valid_move = True
      else:
        print("Sorry, invalid square. Please try again!\n")
    except:
      print("Sorry, invalid input. Please try again with an integer!\n")


def make_computer_move(board, cells):
  """This function accepts the Tic-Tac-Toe board and the number of cells 
  left as the parameters. The computer will try to create a line with 3 O's.
  If the user is about to win, the computer will place an 'O' there. """

  #This variable shows if the computer has made a move
  valid_move = False
  """On the first move, the computer will place an 'O'  in the middle of the board.
  If that's already taken, then it will place an 'O' on the top right of the board instead."""
  if cells == 8:
    if board[1][1] == " ":
      board[1][1] = 'O'
      valid_move = True
    else:
      board[0][0] = 'O'
      valid_move = True
  """The computer will check if there's any two 'O's in a row; 
  If so, it will place an 'O' to create three in a row and win"""
  # Check columns for 'O's
  for column in range(3):
    if valid_move == False:
      if board[0][column] == board[1][column] and board[2][
          column] == " " and board[0][column] == 'O':
        board[2][column] = 'O'
        valid_move = True
      elif board[0][column] == board[2][column] and board[1][
          column] == " " and board[0][column] == 'O':
        board[1][column] = 'O'
        valid_move = True
      elif board[1][column] == board[2][column] and board[0][
          column] == " " and board[1][column] == 'O':
        board[0][column] = 'O'
        valid_move = True

  # Check rows for 'O's
  for row in range(3):
    if valid_move == False:
      if board[row][0] == board[row][1] and board[row][2] == " " and board[
          row][0] == 'O':
        board[row][2] = 'O'
        valid_move = True
      elif board[row][0] == board[row][2] and board[row][1] == " " and board[
          row][0] == 'O':
        board[row][1] = 'O'
        valid_move = True
      elif board[row][1] == board[row][2] and board[row][0] == " " and board[
          row][1] == 'O':
        board[row][0] = 'O'
        valid_move = True

  # Check diagonal (top-left to bottom-right) for 'O's
  if valid_move == False:
    if board[0][0] == board[1][1] and board[2][2] == " " and board[0][0] == 'O':
      board[2][2] = 'O'
      valid_move = True
    elif board[0][0] == board[2][2] and board[1][1] == " " and board[0][
        0] == 'O':
      board[1][1] = 'O'
      valid_move = True
    elif board[1][1] == board[2][2] and board[0][0] == " " and board[1][
        1] == 'O':
      board[0][0] = 'O'
      valid_move = True


# Check diagonal (bottom-left to top-right) for 'O's
    elif board[2][0] == board[1][1] and board[0][2] == " " and board[2][
        0] == 'O':
      board[0][2] = 'O'
      valid_move = True
    elif board[2][0] == board[0][2] and board[1][1] == " " and board[2][
        0] == 'O':
      board[1][1] = 'O'
      valid_move = True
    elif board[0][2] == board[1][1] and board[2][0] == " " and board[0][
        2] == 'O':
      board[2][0] = 'O'
      valid_move = True
  """The computer will check if there's any two 'X's in a row; 
  If so, it will place an 'O' to block the user from winning"""
  # Check columns for 'X's
  for column in range(3):
    if valid_move == False:
      if board[0][column] == board[1][column] and board[2][
          column] == " " and board[0][column] == 'X':
        board[2][column] = 'O'
        valid_move = True
      elif board[0][column] == board[2][column] and board[1][
          column] == " " and board[0][column] == 'X':
        board[1][column] = 'O'
        valid_move = True
      elif board[1][column] == board[2][column] and board[0][
          column] == " " and board[1][column] == 'X':
        board[0][column] = 'O'
        valid_move = True

  # Check rows for 'X's
  for row in range(3):
    if valid_move == False:
      if board[row][0] == board[row][1] and board[row][2] == " " and board[
          row][0] == 'X':
        board[row][2] = 'O'
        valid_move = True
      elif board[row][0] == board[row][2] and board[row][1] == " " and board[
          row][0] == 'X':
        board[row][1] = 'O'
        valid_move = True
      elif board[row][1] == board[row][2] and board[row][0] == " " and board[
          row][1] == 'X':
        board[row][0] = 'O'
        valid_move = True

  # Check diagonal (top-left to bottom-right) for 'X's
  if valid_move == False:
    if board[0][0] == board[1][1] and board[2][2] == " " and board[0][0] == 'X':
      board[2][2] = 'O'
    elif board[0][0] == board[2][2] and board[1][1] == " " and board[0][
        0] == 'X':
      board[1][1] = 'O'
    elif board[1][1] == board[2][2] and board[0][0] == " " and board[1][
        1] == 'X':
      board[0][0] = 'O'
  # Check diagonal (bottom-left to top-right) for 'X's
    elif board[2][0] == board[1][1] and board[0][2] == " " and board[2][
        0] == 'X':
      board[0][2] = 'O'
    elif board[2][0] == board[0][2] and board[1][1] == " " and board[2][
        0] == 'X':
      board[1][1] = 'O'
    elif board[0][2] == board[1][1] and board[2][0] == " " and board[0][
        0] == 'X':
      board[2][0] = 'O'
  #If none of the conditions apply, the computer can pick a random square to place an 'O'
    else:
      while not valid_move:
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 2)
        if board[randomRow][randomColumn] == " ":
          board[randomRow][randomColumn] = 'O'
          valid_move = True


def main():
  """Our Main Game Loop:"""
  free_cells = 9
  users_turn = True
  ttt_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
  while winner(ttt_board) == "" and (free_cells > 0):
    display_board(ttt_board)
    if users_turn:
      make_user_move(ttt_board)
      users_turn = not users_turn
    else:
      make_computer_move(ttt_board, free_cells)
      users_turn = not users_turn
    free_cells -= 1

  display_board(ttt_board)
  if (winner(ttt_board) == 'X'):
    print("Y O U   W O N !")
  elif (winner(ttt_board) == 'O'):
    print("I   W O N !")
  else:
    print("S T A L E M A T E !")
  print("\n*** GAME OVER ***\n")


# Start the game!
main()
