import numpy as np 
from utilities import input_check

def given_matrices_inserter(filename):
	try:	
		data = open(filename, 'r')
		dimensions = data.readline()
		n = int(dimensions)
		letters = data.readline()
		global score_matrix
		score_matrix = np.zeros((n,n))
		for i in range(0,n):
			arr = data.readline().split(" ")
			for j in range(0,n):
				score_matrix[i][j] = arr[j]
		print("filename matrix:")
		print(score_matrix)
		letters = letters.replace('\n', '')
		letters_arr = letters.split(' ')
		print(letters_arr)
		return letters_arr 
	except FileNotFoundError:
		print("There is no matrix file.")
		exit()
		

def custom_matrix():
	global SCORE_MATRIX
	global CUSTOM
	CUSTOM = True
	print("Insert dimensions:")
	n = input_check()
	m = input_check()
	print("Insert matrix:")
	SCORE_MATRIX = np.zeros((n,m))
	for i in range(0,n):
		print(SCORE_MATRIX)
		for j in range(0,m):
			SCORE_MATRIX[i][j] = input_check()
	print("Custom matrix:")
	print(SCORE_MATRIX)
	return SCORE_MATRIX
	
def fill_matrix(n, m, t, param1, param2, param3):
	global GIVEN
	global SCORE_MATRIX
	SCORE_MATRIX = np.zeros((n,m))
	GIVEN = True
	for i in range(n):
		for j in range(m):
			if i == j:
				SCORE_MATRIX[i][j] = param1
			elif t.lower() == "ttm" and i + j == 3:
				SCORE_MATRIX[i][j] = param3
			else: 
				SCORE_MATRIX[i][j] = param2
	print("Score matrix (" + t +"):")
	print(SCORE_MATRIX)
	return SCORE_MATRIX
	
def premade_score():
	print("Do you want to use BLAST(B), Transition-Transvertion Matrix(TTM) or none?")
	m = input()
	if m not in {"B","b", "TTM","ttm", "no", "n"}:
		print("Not a valid option. Try again.")
		return premade_score()
	elif m in {"no", "n"}:
		return 
	elif m in {"B","b"}:
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