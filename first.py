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

def global_alignment_nucleotide():
	matrix_chooser()
	print("globalno 1")
	
def local_alignment_nucleotide():
	matrix_chooser()
	print("lokalno 1")