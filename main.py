#This file is a main file for project of Protein/Nucleotide Sequence Alignment. 
#It contains interface to the four parts which make a whole, those are the following:
#1. Global and local alignment of nucleotide sequences using given matrix as a score matrix 
#2. Global and local alignments of protein sequences using PAM and BLOSUM score matrices 
#3. Alignment of protein and nucleotide sequences, depending on the type
#4. Alignment of multiple sequences using CLUSTALW algorithm 
import first, second, third, fourth, utilities
#from first import global_alignment_nucleotide, local_alignment_nucleotide
#from second import global_alignment_protein, local_alignment_protein, given_matrices_inserter
#from utilities import sequence_chooser, file_chooser, sequence_input_check, protein_sequence_input_check
import numpy as np
from screens import screen, option_chooser, alignment_chooser

SCORE_MATRIX = np.zeros((10,10))
score_matrix = np.zeros((10,10))
GIVEN = False
GIVEN2 = False
CUSTOM = False 
G = False
L = False 

def main():
	screen()
	
if __name__ == "__main__":
	main()