import numpy as np 
from utilities import input_check

def given_matrices_inserter(filename):
	try:	
		data = open(filename, 'r')
		dimensions = data.readline()
		try:
			n = int(dimensions)
		except ValueError:
			print("Wrong file")
			exit()
		letters = data.readline()
		letters = letters.replace('\n', '')
		letters_arr = letters.split(' ')
		#print(letters_arr)
		score_matrix = np.zeros((n,n))
		for i in range(0,n):
			arr = data.readline().split(" ")
			for j in range(0,n):
				#print(arr[j])
				score_matrix[i][j] = float(arr[j])
		#print("Chosen matrix:")
		#print(score_matrix)
		return letters_arr, score_matrix
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
	return letters, score_matrix
	
def input_matrix():
	print("Insert the size of the matrix and the sequence " \
	 "of letters in which order you choose to fill the matrix:\ne.g. 4 A T C G")
	input_arr = input().split()
	n = int(input_arr[0])
	letters = input_arr[1:]
	score_matrix = np.zeros((n, n))
	for i in range(n):
		score_matrix[i] = input().split()
	return letters, score_matrix

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
				#print(score_matrix)
				for j in range(0,n):
					score_matrix[i][j] = input_check()
			print("Custom matrix:")
			print(score_matrix)
			return letters,score_matrix
	
def premade_score(letters, match, mismatch):
	blosum = {"blosum", "BLOSUM", "blosum45", "BLOSUM45"}
	indicator = 0 #0 is for nucleotide 1 is for protein
	for i in range(len(letters)):
		if letters[i] not in ["A", "C", "G", "T", "-"]:
			indicator = 1
	
	if indicator == 1:
		print("Do you want to use PAM250, BLOSUM45 or none?")
		m = input()
		if m not in {"pam","PAM", "pam250", "PAM250", "blosum", "BLOSUM", "blosum45", "BLOSUM45", "no", "n"}:
			print("Not a valid option. Try again.")
			return premade_score(letters, match, mismatch)
		elif m in {"no", "n"}:
			return fill_matrix(letters, match, mismatch)
		elif m in blosum:
			return given_matrices_inserter("matrices/blosum45.txt")
		else: 
			return given_matrices_inserter("matrices/pam250.txt")
	else:
		print("Do you want to use BLAST(B), Transition-Transvertion Matrix(TTM) or none?")
		m = input()
		if m not in {"B","b", "TTM","ttm", "no", "n"}:
			print("Not a valid option. Try again.")
			return premade_score(letters, match, mismatch)
		elif m in {"no", "n"}:
			return fill_matrix(letters, match, mismatch)
		elif m in {"B","b"}:
			return given_matrices_inserter("matrices/blast.txt")
		else:
			return given_matrices_inserter("matrices/ttm.txt")
	
def matrix_chooser(letters, match, mismatch):
	print("Do you want to use custom score matrix? yes/no")
	a = input()
	if a not in ['yes','no']:
		print("Not a valid option. Try again.")
		return matrix_chooser(letters, match, mismatch)
	elif a == 'yes':
		return custom_matrix(letters)
	else:
		return premade_score(letters, match, mismatch)