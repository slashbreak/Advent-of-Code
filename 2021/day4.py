#!/usr/bin/env python3

#AOC 2021 day 4

with open('input4') as f:
	lines = [x.strip() for x in f.read().split('\n\n')]
numbers = [x for x in lines.pop(0).split(',')]
boards = []
for i,j in enumerate(lines):
	boards.append(j)
	boards[i] = [x for x in j.replace('\n',' ').replace('  ',' ').split(' ')]

def check_bingo(index, board):
	#horizontal
	for i in range(5):
		if "".join(x for x in board[i*5:i*5+5]) == "XXXXX":
			return True

	# vertical
	if board[0]+board[5]+board[10]+board[15]+board[20] == "XXXXX":
		return True
	elif board[1]+board[6]+board[11]+board[16]+board[21] == "XXXXX":
		return True
	elif board[2]+board[7]+board[12]+board[17]+board[22] == "XXXXX":
		return True
	elif board[3]+board[8]+board[13]+board[18]+board[23] == "XXXXX":
		return True
	elif board[4]+board[9]+board[14]+board[19]+board[24] == "XXXXX":
		return True
	return False

def print_board(board):
	for i in range(5):
		print (board[i*5:i*5+5])

done = False
unsolved_boards = list(range(len(boards)))
for num in numbers:
	for i in range(len(boards)):
		if num in boards[i]:
			boards[i][boards[i].index(num)] = "X"
			if i in unsolved_boards and check_bingo(i, boards[i]):
				print("BINGO on board {}".format(i))
				unsolved_boards.remove(i)
				sum_unmarked = sum([int(x) for x in boards[i] if x.isnumeric()])
				print("Board value (sum of unmarked numbers * board_id) is: {}".format(sum_unmarked*int(num)))