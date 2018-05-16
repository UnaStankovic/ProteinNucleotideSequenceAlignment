#This file contains option choosers and other screen settings
from utilities import sequence_chooser, file_chooser, sequence_input_check, protein_sequence_input_check
from first import global_alignment_nucleotide, local_alignment_nucleotide
from second import global_alignment_protein, local_alignment_protein, given_matrices_inserter
from third import protein_nucleotide_alignment

def alignment_chooser(opt):
	print("For global alignment type G, for local L:")
	a = input()
	if a not in ["L","G", "l", "g"]:
		print("Not a valid option. Try again.")
		return alignment_chooser(opt)
	if opt == '1':
		print("Insert sequences for alignment:")
		first = sequence_input_check()
		second = sequence_input_check()
		if a in ["G", "g"]:
			print(global_alignment_nucleotide(first, second))
		else:
			print(local_alignment_nucleotide(first, second))
	elif opt == '2':
		letters = given_matrices_inserter(file_chooser())
		print("Insert sequences for alignment:")
		first = protein_sequence_input_check(letters)
		second = protein_sequence_input_check(letters)
		if a in ["G", "g"]:
			print(global_alignment_protein(first, second, letters))
		else:
			print(local_alignment_protein(first, second))  


def option_chooser(opt):
	valid = set(['1','2','3','4','5'])
	if opt not in valid:
		print("Not a valid option. Try again.")
		return screen()
	elif opt in ["1","2"]:
		return alignment_chooser(opt)
	elif opt == '3':
		print("Option 3")
		first = sequence_chooser()
		second = sequence_chooser()
		return protein_nucleotide_alignment(first, second)
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
