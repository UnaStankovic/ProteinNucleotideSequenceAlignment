#This file contains basic functions, such as: file choosers, openers, info inputs and similar. 
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

def match_mis_gap_chooser():
	global G
	global L 
	print("Do you want to manually choose values for match, mismatch and gap? \
		(If you've chosen to use BLAST or TTM matrix only gap value will be applied.)")
	m = input()
	if m not in {"yes","y","no","n"}:
		print("Invalid answer.Try again.")
		return match_mis_gap_chooser()
	elif m in {"yes","y"}:
		print("Match:")
		match = input_check()
		print("Mismatch:")
		mismatch = input_check()
		print("Gap:")
		gap = input_check()
	elif G == True:
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

def sequence_input_check():
	sequence = input()
	for i in range(len(sequence)):
		if sequence[i] not in {"A","C","G","T","a","c","g","t"}:
			print("Not a valid sequence.Try again")
			return sequence_input_check()
	return sequence	

def protein_sequence_input_check(allowed):
	sequence = input()
	for i in range(len(sequence)):
		if sequence[i] not in allowed:
			print("Invalid sequence.Try again.")
			return protein_sequence_input_check(allowed)
	return sequence 

		