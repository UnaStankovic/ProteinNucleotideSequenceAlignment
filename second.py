#This file contains global and local alignments of protein sequences using PAM(global alignment) and BLOSUM(local alignment) score matrix
#PAM trace evolutionary origins of proteins refers to evolutionary distance ,
#BLOSUM score alignment between evolutionarily-divergent proteins, refers to percent identity
#PAM High number: compares distantly related proteins
#BLOSUM High number : compares closely related proteins

import numpy as np
import settings as s
from matrices import given_matrices_inserter

#global score_matrix
#score_matrix = np.zeros((10,10))
#global GIVEN
#global GIVEN2
#GIVEN2 = False

def match_score(c1, c2, m, mm, letters):
	s.GIVEN2 = True
	mapped_values = {}
	if s.GIVEN:
		mapped_values = {'A' : 0, 'a' : 0,
						'T' : 1, 't' : 1,
						'C' : 2, 'c' : 2,
						'G' : 3, 'g' : 3}
		a = mapped_values[c1]
		b = mapped_values[c2]
		return s.SCORE_MATRIX[a][b]
	elif s.GIVEN2:
		for i, v in enumerate(letters):
			print(i,v)
			mapped_values[v] = i
		print(mapped_values)
		a = mapped_values[c1]
		b = mapped_values[c2]
		return s.score_matrix[a][b]
	elif c1 == c2:
		return m
	else:
		return mm

# def global_alignment_protein(first, second, letters):
# 	match_score("A", "G", 5, 10, letters)
# 	print("globalno 1")
#
# def local_alignment_protein(first, second, letters):
# 	print("lokalno 1")
