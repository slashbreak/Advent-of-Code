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
	for i in range(5):
		if board[0+i]+board[5+i]+board[10+i]+board[15+i]+board[20+i] == "XXXXX":
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
			boards[i][boards[i].index(num)] = "X" # Replace number with an X
			if i in unsolved_boards and check_bingo(i, boards[i]):
				print("BINGO on board {}".format(i))
				unsolved_boards.remove(i)
				sum_unmarked = sum([int(x) for x in boards[i] if x.isnumeric()])
				print("Board value is: {}".format(sum_unmarked*int(num)))