#Hey guys!!!
#Vaibhav This side 
#The code given below is of a Simple Tac Toe Game
#My motive to write this code was to apply whatever i have learnt yet

#Definiton of the used functions in this game

from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker=''
    while marker!= 'X' and marker!= 'O':
         marker=input('Player1, choose X or O: ').upper()
    player1=marker
    
    if player1 =='X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)
def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    #all rows
    return ((board[1] ==mark and board[2]==mark and board[3]==mark) or #rows
           (board[4] ==mark and board[5]==mark and board[6]==mark) or #rows
           (board[7] ==mark and board[8]==mark and board[9]==mark)or #rows
           (board[1] ==mark and board[4]==mark and board[7]==mark)or #columns
           (board[2] ==mark and board[5]==mark and board[8]==mark)or #columns
           (board[3] ==mark and board[6]==mark and board[9]==mark)or #columns
           (board[1] ==mark and board[5]==mark and board[9]==mark)or #diagonals
           (board[3] ==mark and board[5]==mark and board[7]==mark))
import random
def choose_first():
    return random.choice(['Player1', 'Player2'])

def space_check(board,position):
    return board[position]== ' '

def full_board_check(board):
    for it in board:
         if it==' ':
            return False
         else:
             pass
    return True  
              
def player_choice(board):
    position=0
    while position not in range(1,10) or not  space_check(board,position):
          position =int(input('Choose a position: (1-9)'))
    return position

def replay():
    choice=input("Play again? Enter Yes or No")
    return choice=='Yes'     

# WHILE LOOP TO KEEP RUNNING THE GAME
print ('Welcome to Tic Tac Toe')
while True:
     #play the game
      #set everything up (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
      board=[' ']*10
      player1_marker,player2_marker= player_input()
      turn= choose_first()
      print(turn+' wil go first')
      play_game=input('Ready To Play? ..y or n').lower()
      if play_game=='y':
         game_on=True
      else:    
          game_on=False
##gameplay
      while game_on:
             ##player one turn 
            if turn =='Player1':
              #show board
               display_board(board)
               #choose a position
               position= player_choice(board)
               #place the marker on the position
               place_marker(board,player1_marker,position)
                #check if they won
               if win_check(board,player1_marker):
                  display_board(board)
                  print('PLAYER 1 HAS WON!!!!')
                  game_on=False
               else:   #check if there is a tie
                     if full_board_check(board):
                         display_board(board)
                         print("TIE GAME!")
                         game_on=False
                     else:   
                         turn='Player2'
#no tie and no win? then next player's turn   
            else: #player two turn
                  display_board(board)
               #choose a position
                  position= player_choice(board)
               #place the marker on the position
                  place_marker(board,player2_marker,position)
                  if win_check(board,player2_marker):
                     display_board(board)
                     print('PLAYER 2 HAS WON!!!!')
                     game_on=False
                  else:
                       if full_board_check(board):
                           display_board(board)
                           print("TIE GAME!")
                           game_on=False
                       else:    #no tie and no win? then next player's turn    
                           turn='Player1'
           
          #break out of the while loop on replay()
      if not replay():
            print('THANKS FOR PLAYING!!!!')
            break
        