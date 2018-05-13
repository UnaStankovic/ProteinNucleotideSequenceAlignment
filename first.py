#This file contains global and local alignments of nucleotide sequences using given matrix as a score matrix 
#BLAST AND TTM MATRIX ARE GIVEN AS 
#  A  T  C  G      A  T  C  G
#A 5 -4 -4 -4    A 1 -5 -5 -1
#T -4 5 -4 -4    T -5 1 -1 -5
#C -4 -4 5 -4    C -5 -1 1 -5
#G -4 -4 -4 5    G -1 -5 -5 1
#  BLAST		   TTM MATRIX 
import numpy as np

def input_check():
	val = input()
	if val.isdigit():
		#print(val)
		return int(val)
	else:
		print("Not a number. Try again.")
		return input_check()
		
def custom_matrix():
#	# take input from user in one row
#	nn_matrix = input().split()
#	total_cells =  len(nn_matrix)
#	row_cells = int(total_cells**0.5)
#	matrix = [nn_matrix[i:i+row_cells] for i in xrange(0, total_cells, row_cells)]
	print("Insert dimensions:")
	n = input_check()
	m = input_check()
	print("Insert matrix:")
	matrix = np.zeros((n,m))
	for i in range(0,n):
		print(matrix)
		for j in range(0,m):
			matrix[i][j] = input_check()
	print(matrix)		
	return matrix
	
def fill_matrix(n, m, t, param1, param2, param3):
	matrix = np.zeros((n,m))
	for i in range(n):
		for j in range(m):
			if i == j:
				matrix[i][j] = param1
			elif t.lower() == "ttm" and i + j == 3:
				matrix[i][j] = param3
			else: 
				matrix[i][j] = param2
	print(matrix)
	return matrix 
	
def premade_score():
	print("Do you want to use BLAST(B) or Transition-Transvertion Matrix(TTM)?")
	m = input()
	if m not in {"B","b", "TTM","ttm"}:
		print("Not a valid option. Try again.")
		return premade_score()
	if m in {"B","b"}:
		return fill_matrix(4, 4, m, 5, -4, 0)
	else:
		return fill_matrix(4, 4, m, 1, -5, -1)
	
def matrix_chooser():
	print("Do you want to use custom score matrix? yes/no")
	a = input()
	if a not in ['yes','no']:
		print("Not a valid option. Try again.")
		return matrix_chooser()
	elif a == 'yes':
		return custom_matrix()
	else:
		return premade_score()	

def match_mis_gap_chooser():
	print("Do you want to manually choose values for match, mismatch and gap?")
	m = input()
	if m not in {"yes","y","no","n"}
		print("Invalid answer.Try again.")
		return match_mis_gap_chooser()
	elif m in {"yes","y"}:
		match = input_check()
		mismatch = input_check()
		gap = input_check()
	else:
		match = 5
		mismatch = -1
		gap = -2
	return match, mismatch, gap
	
def global_alignment_nucleotide(first, second):
	score_matrix = matrix_chooser()
	match, mismatch, gap = match_mis_gap_chooser()
	
	
def local_alignment_nucleotide(first, second):
	score_matrix = matrix_chooser()
	local_alignment = [[0 for j in range(len(second) + 1)] for i in range(len(first) + 1)]
	
	for i in range(len(first) + 1):
		local_alignment[i][0] = 0
	for i in range(len(second) + 1):
		local_alignment[0][i] = 0
		
	for i in range(1, len(first) +1):
		for j in range(1, len(second) + 1):
			local_alignment[i][j] = max(0, local_alignment[i-1][j] - 2, local_alignment[i][j-1] - 2, \
										local_alignment[i-1][j-1] + int(first == second))
	
	maximum = 0
	for i in range(len(local_alignment)):
		for j in range(len(local_alignment[i])):
			if local_alignment[i][j] > maximum:
				maximum = local_alignment[i][j]
	
	for i in range(len(local_alignment)):
		print(local_alignment[i])
	
	return maximum