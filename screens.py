#This file contains option choosers and other screen settings
import numpy as np 
from utilities import sequence_chooser, file_chooser, sequence_input_check
from first import global_alignment, local_alignment
from matrices import given_matrices_inserter
from second import protein_nucleotide_alignment

def alignment_chooser(opt):
	print("For global alignment type G, for local L:")
	a = input()
	if a not in ["L","G", "l", "g"]:
		print("Not a valid option. Try again.")
		return alignment_chooser(opt)
	if opt == '1':
		print("Insert sequences for alignment:")
		letters = ['A','C','T','G']
		first = sequence_input_check(letters)
		second = sequence_input_check(letters)
		matrix = np.zeros((len(letters), len(letters)))
		if a in ["G", "g"]:
			print(global_alignment(first, second, letters, matrix))
		else:
			print(local_alignment(first, second, letters, matrix))
	elif opt == '2':
		letters, matrix = given_matrices_inserter(file_chooser())
		print("Insert sequences for alignment:")
		first = sequence_input_check(letters)
		second = sequence_input_check(letters)
		if a in ["G", "g"]:
			print(global_alignment(first, second, letters, matrix))
		else:
			print(local_alignment(first, second, letters, matrix))
	elif opt == '3':
		first = sequence_chooser()
		second = sequence_chooser()
		matrix = np.zeros((2,2))
		first, second, letters, matrix = protein_nucleotide_alignment(first, second)
		if a in ["G", "g"]:
			return global_alignment(first, second, letters, matrix)
		else:
			return local_alignment(first, second, letters, matrix)

def option_chooser(opt):
	valid = set(['1','2','3','4','5'])
	if opt not in valid:
		print("Not a valid option. Try again.")
		return screen()
	elif opt in ["1","2", "3"]:
		return alignment_chooser(opt)
	elif opt == '4':
		print("Option 4")
		given_matrices_inserter(file_chooser())
	else:
		exit()

def screen():
	print("Choose one option of the following:\n \
		1. Global and local alignment of nucleotide sequences using given matrix as a score matrix\n \
		2. Global and local alignments of protein sequences using PAM and BLOOSUM score matrices\n \
		3. Alignment of protein or nucleotide sequences, depending on the type\n\
		4. Alignment of multiple sequences using CLUSTALW algorithm \n \
		5. Exit program")
	option = input()
	return option_chooser(option)
