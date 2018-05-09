#This file is a main file for project of Protein/Nucleotide Sequence Alignment. 
#It contains interface to the four parts which make a whole, those are the following:
#1. Global and local alignment of nucleotide sequences using given matrix as a score matrix 
#2. Global and local alignments of protein sequences using PAM and BLOOSUM score matrices 
#3. Alignment of protein or nucleotide sequences, depending on the type
#4. Alignment of multiple sequences using CLUSTALW algorithm 
import nekifajl

def alignment_chooser():
	print("For global alignment type G, for local L:")
	a = input()
	return a

def option_chooser(opt):
	valid = set(['1','2','3','4','5'])
	if opt not in valid:
		print("Not a valid option. Try again.")
		screen()
	elif opt == '1':
		print("Option 1")
	elif opt == '2':
		print("Option 2")
	elif opt == '3':
		print("Option 3")
	elif opt == '4':
		print("Option 4")
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
	option_chooser(option)

def main():
	nekifajl.say_hi()
	screen()
	
if __name__ == "__main__":
	main()