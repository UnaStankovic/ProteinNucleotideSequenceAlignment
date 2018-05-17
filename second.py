#This file contains global and local alignments of protein sequences using PAM(global alignment) and BLOSUM(local alignment) score matrix
#PAM trace evolutionary origins of proteins refers to evolutionary distance ,
#BLOSUM score alignment between evolutionarily-divergent proteins, refers to percent identity
#PAM High number: compares distantly related proteins
#BLOSUM High number : compares closely related proteins

import numpy as np
import settings as s
from matrices import given_matrices_inserter

def match_score(c1, c2, m, mm, letters, score_matrix):
	s.GIVEN = True
	mapped_values = {}
	if s.GIVEN:
		for i, v in enumerate(letters):
			print(i,v)
			mapped_values[v] = i
		print(mapped_values)
		a = mapped_values[c1]
		b = mapped_values[c2]
		return score_matrix[a][b]
	elif c1 == c2:
		return m
	else:
		return mm
