#This file contains global and local alignments of nucleotide sequences using given matrix as a score matrix 
import numpy as np

def input_check():
	val = input()
	if val.isdigit():
		print(val)
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
	print(matrix)

def premade_score():
	print("Do you want to use BLAST(B) or Transition-Transvertion Matrix(TTM)?")
	m = input()
	if m not in {"B","b", "TTM","ttm"}:
		print("Not a valid option. Try again.")
		return premade_score()
	matrix = np.zeros((4,4))
	print(matrix)
	if m in {"B","b"}:
		for i in range(4):
			for j in range(4):
				if i == j:
					matrix[i][j] = 5
				else:
					matrix[i][j] = -4
	else:
		for i in range(4):
			for j in range(4):
				if i == j:
					matrix[i][j] = 1
				elif i + j == 3:
					matrix[i][j] = -1
				else:
					matrix[i][j] = -5
	print(matrix)
	return matrix 
	
def matrix_chooser():
	print("Do you want to use custom score matrix? yes/no")
	a = input()
	if a not in ['yes','no']:
		print("Not a valid option. Try again.")
		return matrix_chooser()
	elif a == 'yes':
		custom_matrix()
	else:
		premade_score()	

			
def global_alignment_nucleotide(first, second):
	matrix_chooser()
	match = 1
	mismatch = -1
	indel = -1
	
	
def local_alignment_nucleotide(first, second):
	matrix_chooser()
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