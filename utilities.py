#This file contains basic functions, such as: file choosers, openers, info inputs and similar.
import numpy as np
import settings as s

#CHOOSERS
def sequence_chooser():
	print("Enter 1 for a file name or 2 for DNA/protein sequence:")
	a = input()
	if a not in {"1","2"}:
		print("Not a valid option.Try again.")
		return sequence_chooser()
	elif a == "1":
		print("Enter file name:")
		data = input()
		if(data.find('.txt') == -1):
			print("Not a valid option. Try again.")
			return sequence_chooser()
		else:
			return data
	else:
		print("Insert sequence:")
		sequence = input()
		return sequence

def file_chooser():
	print("Insert filename ex. blast.txt")
	name = input()
	if(name.find('.txt') == -1):
		print("Not a valid option. Try again.")
		return file_chooser()
	else:
		return name

def match_mis_gap_chooser(opt):
	print("Do you want to manually choose values for match, mismatch and gap? \
		(If you've chosen to use BLAST or TTM matrix only gap value will be applied.)")
	m = input()
	if m not in {"yes","y","no","n"}:
		print("Invalid answer.Try again.")
		return match_mis_gap_chooser(opt)
	elif m in {"yes","y"}:
		print("Match:")
		match = input_check()
		print("Mismatch:")
		mismatch = input_check()
		print("Gap:")
		gap = input_check()
	elif opt == "g":
		match = 5
		mismatch = -1
		gap = -2
	else:
		match = 1
		mismatch = -1
		gap = -1
	return match, mismatch, gap

#INPUT CHECKS
def input_check():
	val = input()
	v = val
	if v.lstrip('-').isdigit():
		return int(val)
	else:
		print("Not a number. Try again.")
		return input_check()

def sequence_input_check(allowed):
	sequence = input()
	sequence = sequence.upper()
	print(sequence)
	print(allowed)
	for i in range(len(sequence)):
		if sequence[i] not in allowed:
			print("Invalid sequence.Try again.")
			return sequence_input_check(allowed)
	return sequence

#FILE OPENERS - WRITERS
def file_opener(filename):
	try:
		dna = open(filename, 'r')
		content = dna.read()
		content = content.replace('\n','')
		return content
	except FileNotFoundError:
		print("The file does not exist.")
		exit()

def rna_file_writer(content):
	print("Do you want to have RNA info written in a file?")
	answer = input()
	if answer not in ["Yes","y", "yes", "No", "n", "no"]:
		print("Not a valid answer. Try again.")
		return rna_file_writer(content)
	elif answer in ["Yes","y", "yes"]: 
		print("Insert file name:")
		filename = input()
		filename.append(".txt")
		print(filename)
		rna = open(filename, 'w')
		rna.write(content)
		print("Writing in " + filename + "successfully finished.")
		return
	else:
		return

def input_matrix():
	print("Insert the size of the matrix and the sequence " \
	 "of letters in which order you choose to fill the matrix:\ne.g. 4 A T C G")
	input_arr = input().split()
	n = int(input_arr[0])
	letters = input_arr[1:]
	s.score_matrix = np.zeros((n, n)) # which matrix should be filled here?
	for i in range(n):
		s.score_matrix[i] = input().split()
	return letters
