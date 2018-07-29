
from os import system, name

test_board = [' '] * 9
playing = True

def clear():
 
    if name == 'nt':
        _ = system('cls')

def playing_board(board):
	'''Print the playing board.
	0 | 1 | 2
	---------
	3 | 4 | 5 
	---------
	6 | 7 | 8'''
	
	clear()
	print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
	print("-----------")
	print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
	print("-----------")
	print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

playing_board(test_board)	

def player_assign():
	'''Assign 'X' or 'O' to players.'''
	player1 = ''
	while player1 != 'X' and player1 != 'O':
		player1 = input("Player1 choose 'X' or 'O' : ")

	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	return player1,player2

player1,player2 = player_assign()

def win_check(board):
	'''Dtermine if there is a winner or is it a tie.
	   Check all rows, columns and diagonals.'''
	i = 0
	while i <= 6:
		if board[i] != ' ':
			if board[i] == board[i + 1] and board[i] == board[i + 2]:
				return 0
		i += 3
	i = 0
	while i <= 2:
		if board[i] != ' ':
			if board[i] == board[i + 3] and board[i] == board[i + 6]:
				return 0
		i += 1
	i = 0
	if board[i] != ' ':
		if board[i] == board[i + 4] and board[i] == board[i + 8]:
			return 0
	i = 2
	if board[i] != ' ':
		if board[i] == board[i + 2] and board[i] == board[i + 4]:
			return 0
	if ' ' not in board:
		return 1				 

def play_game(board):
	'''Input the players move and call win function.'''
	pl = 3
	global playing
	while True:
		player1_pos = int(input('Player1 Choose your position 0-8 : '))
		if player1_pos in range(0,9):
			if board[player1_pos] == ' ':
				break
	board[player1_pos] = player1
	if win_check(board) == 0:
		playing = False
		pl = 1
	elif win_check(board) == 1:
		pl = 0
		playing = False	
	if playing:		
		while True:
			player2_pos = int(input('Player2 Choose your position 0-8 : '))
			if player2_pos in range(0,9):
				if board[player2_pos] == ' ':
					break
		board[player2_pos] = player2
		if win_check(board) == 0:
			playing = False
			pl = 2
		elif win_check(board) == 1:
			pl = 0
			playing = False	
	return pl			
			
while playing:
	player = play_game(test_board)
	playing_board(test_board)
	if player == 0:
		print("\nToo bad!! It's a tie.")
	elif player == 1:
		print("\nCongratulations!! Player1 Wins.")
	elif player == 2:
		print("\nCongratulations!! Player2 Wins.")
		


		