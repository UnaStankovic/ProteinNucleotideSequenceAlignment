import numpy as np 
from utilities import input_check

def given_matrices_inserter(filename):
	try:	
		data = open(filename, 'r')
		dimensions = data.readline()
		n = int(dimensions)
		letters = data.readline()
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
		given = 1
		return given, letters_arr, score_matrix
	except FileNotFoundError:
		print("There is no matrix file.")
		exit()		

def fill_matrix(letters, match, mismatch):
	n = len(letters)
	score_matrix = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if i == j:
				score_matrix[i][j] = match 
			else:
				score_matrix[i][j] = mismatch
	given = 0
	return given, letters, score_matrix
	
def input_matrix():
	print("Insert the size of the matrix and the sequence " \
	 "of letters in which order you choose to fill the matrix:\ne.g. 4 A T C G")
	input_arr = input().split()
	n = int(input_arr[0])
	letters = input_arr[1:]
	score_matrix = np.zeros((n, n)) # which matrix should be filled here?
	for i in range(n):
		score_matrix[i] = input().split()
	given = 1
	return given, letters, score_matrix

def custom_matrix(letters):
	for i in range(len(letters)):
		if letters[i] not in ["A", "C", "G", "T"]:
			return input_matrix()
		else:
			print("Insert matrix data in following order: " + str(letters))
			n = len(letters)
			print("Insert matrix:")
			score_matrix = np.zeros((n,n))
			for i in range(0,n):
				print(score_matrix)
				for j in range(0,n):
					score_matrix[i][j] = input_check()
			print("Custom matrix:")
			print(score_matrix)
			given = 1
			return given, letters,score_matrix
	
def premade_score(letters, match, mismatch):
	blosum = {"blosum", "BLOSUM", "blosum45", "BLOSUM45"}
	pam = {"pam","PAM", "pam250", "PAM250"}
	for i in range(len(letters)):
		if letters[i] not in ["A", "C", "G", "T"]:
			print("Do you want to use PAM250, BLOSUM45 or none?")
			m = input()
			if m not in {pam, blosum,  "no", "n"}:
				print("Not a valid option. Try again.")
				return premade_score(letters, match, mismatch)
			elif m in {"no", "n"}:
				return fill_matrix(letters, match, mismatch)
			elif m in blosum:
				return given_matrices_inserter("blosum45.txt")
			else: 
				return given_matrices_inserter("pam250.txt")
		else:
			print("Do you want to use BLAST(B), Transition-Transvertion Matrix(TTM) or none?")
			m = input()
			if m not in {"B","b", "TTM","ttm", "no", "n"}:
				print("Not a valid option. Try again.")
				return premade_score(letters, match, mismatch)
			elif m in {"no", "n"}:
				return fill_matrix(letters, match, mismatch)
			elif m in {"B","b"}:
				return given_matrices_inserter("blast.txt")
			else:
				return given_matrices_inserter("ttm.txt")
	
def matrix_chooser(letters, match, mismatch):
	print("Do you want to use custom score matrix? yes/no")
	a = input()
	if a not in ['yes','no']:
		print("Not a valid option. Try again.")
		return matrix_chooser(letters)
	elif a == 'yes':
		return custom_matrix(letters)
	else:
		return premade_score(letters, match, mismatch)