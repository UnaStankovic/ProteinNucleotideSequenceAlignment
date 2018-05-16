#This file contains global and local alignments of protein sequences using PAM(global alignment) and BLOSUM(local alignment) score matrix
#PAM trace evolutionary origins of proteins refers to evolutionary distance ,
#BLOSUM score alignment between evolutionarily-divergent proteins, refers to percent identity  
#PAM High number: compares distantly related proteins 
#BLOSUM High number : compares closely related proteins 
#TODO :PAM250																						
#TODO: Add to upper everywhere 
#TODO: fix letter reading - spaces, newlines - regex

# BLOSUM45
#    A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V  B  J  Z  X  *
# A  5 -2 -1 -2 -1 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -2 -2  0 -1 -1 -1 -1 -5
# R -2  7  0 -1 -3  1  0 -2  0 -3 -2  3 -1 -2 -2 -1 -1 -2 -1 -2 -1 -3  1 -1 -5
# N -1  0  6  2 -2  0  0  0  1 -2 -3  0 -2 -2 -2  1  0 -4 -2 -3  5 -3  0 -1 -5
# D -2 -1  2  7 -3  0  2 -1  0 -4 -3  0 -3 -4 -1  0 -1 -4 -2 -3  6 -3  1 -1 -5
# C -1 -3 -2 -3 12 -3 -3 -3 -3 -3 -2 -3 -2 -2 -4 -1 -1 -5 -3 -1 -2 -2 -3 -1 -5
# Q -1  1  0  0 -3  6  2 -2  1 -2 -2  1  0 -4 -1  0 -1 -2 -1 -3  0 -2  4 -1 -5
# E -1  0  0  2 -3  2  6 -2  0 -3 -2  1 -2 -3  0  0 -1 -3 -2 -3  1 -3  5 -1 -5
# G  0 -2  0 -1 -3 -2 -2  7 -2 -4 -3 -2 -2 -3 -2  0 -2 -2 -3 -3 -1 -4 -2 -1 -5
# H -2  0  1  0 -3  1  0 -2 10 -3 -2 -1  0 -2 -2 -1 -2 -3  2 -3  0 -2  0 -1 -5
# I -1 -3 -2 -4 -3 -2 -3 -4 -3  5  2 -3  2  0 -2 -2 -1 -2  0  3 -3  4 -3 -1 -5
# L -1 -2 -3 -3 -2 -2 -2 -3 -2  2  5 -3  2  1 -3 -3 -1 -2  0  1 -3  4 -2 -1 -5
# K -1  3  0  0 -3  1  1 -2 -1 -3 -3  5 -1 -3 -1 -1 -1 -2 -1 -2  0 -3  1 -1 -5
# M -1 -1 -2 -3 -2  0 -2 -2  0  2  2 -1  6  0 -2 -2 -1 -2  0  1 -2  2 -1 -1 -5
# F -2 -2 -2 -4 -2 -4 -3 -3 -2  0  1 -3  0  8 -3 -2 -1  1  3  0 -3  1 -3 -1 -5
# P -1 -2 -2 -1 -4 -1  0 -2 -2 -2 -3 -1 -2 -3  9 -1 -1 -3 -3 -3 -2 -3 -1 -1 -5
# S  1 -1  1  0 -1  0  0  0 -1 -2 -3 -1 -2 -2 -1  4  2 -4 -2 -1  0 -2  0 -1 -5
# T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -1 -1  2  5 -3 -1  0  0 -1 -1 -1 -5
# W -2 -2 -4 -4 -5 -2 -3 -2 -3 -2 -2 -2 -2  1 -3 -4 -3 15  3 -3 -4 -2 -2 -1 -5
# Y -2 -1 -2 -2 -3 -1 -2 -3  2  0  0 -1  0  3 -3 -2 -1  3  8 -1 -2  0 -2 -1 -5
# V  0 -2 -3 -3 -1 -3 -3 -3 -3  3  1 -2  1  0 -3 -1  0 -3 -1  5 -3  2 -3 -1 -5
# B -1 -1  5  6 -2  0  1 -1  0 -3 -3  0 -2 -3 -2  0  0 -4 -2 -3  5 -3  1 -1 -5
# J -1 -3 -3 -3 -2 -2 -3 -4 -2  4  4 -3  2  1 -3 -2 -1 -2  0  2 -3  4 -2 -1 -5
# Z -1  1  0  1 -3  4  5 -2  0 -3 -2  1 -1 -3 -1  0 -1 -2 -2 -3  1 -2  5 -1 -5
# X -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -5
# * -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5 -5  1


# PAM250
# 	 G  A  V  L  I  P  S  T  D  E  N  Q  K  R  H  F  Y  W  M  C  B  Z  X       
# G  5	1 -1 -4 -3  0  1  0  1  0  0 -1 -2 -3 -2 -5 -5 -7 -3 -3  0  0 -1 -8
# A  1  2  0 -2 -1  1  1  1  0  0  0  0 -1 -2 -1 -3 -3 -6 -1 -2  0  0  0 -8
# V -1  0  4  2  4 -1 -1  0 -2 -2 -2 -2 -2 -2 -2 -1 -2 -6  2 -2 -2 -2 -1 -8 
# L -4 -2  2  6  2 -3 -3 -2 -4 -3 -3 -2 -3 -3 -2  2 -1 -2  4 -6 -3 -3 -1 -8
# I -3 -1  4  2  5 -2 -1  0 -2 -2 -2 -2 -2 -2 -2  1 -1 -5  2 -2 -2 -2 -1 -8 
# P  0  1 -1 -3 -2  6  1  0 -1 -1  0  0 -1  0  0 -5 -5 -6 -2 -3 -1  0 -1 -8
# S  1  1 -1 -3 -1  1  2  1  0  0  1 -1  0  0 -1 -3 -3 -2 -2  0  0  0  0 -8
# T  0  1  0 -2  0  0  1  3  0  0  0 -1  0 -1 -1 -3 -3 -5 -1 -2  0 -1  0 -8
# D  1  0 -2 -4 -2 -1  0  0  4  3  2  2  0 -1  1 -6 -4 -7 -3 -5  3  3 -1 -8
# E  0  0 -2 -3 -2 -1  0  0  3  4  1  2  0 -1  1 -5 -4 -7 -2 -5  3  3 -1 -8
# N  0  0 -2 -3 -2  0  1  0  2  1  2  1  1  0  2 -3 -2 -4 -2 -4  2  1  0 -8
# Q -1  0 -2 -2 -2  0 -1 -1  2  2  1  4  1  1  3 -5 -4 -5 -1 -5  1  3 -1 -8
# K -2 -1 -2 -3 -2 -1  0  0  0  0  1  1  5  3  0 -5 -4 -3  0 -5  1  0 -1 -8
# R -3 -2 -2 -3 -2  0  0 -1 -1 -1  0  1  3  6  2 -4 -4 -2  0 -4 -1  0 -1 -8
# H -2 -1 -2 -2 -2  0 -1 -1  1  1  2  3  0  2  6 -2  0 -3 -2 -3  1  2 -1 -8
# F -5 -3 -1  2  1 -5 -3 -3 -6 -5 -3 -5 -5 -4 -2  0  7  0  0 -4 -4 -5 -2 -8
# Y -5 -3 -2 -1 -1 -5 -3 -3 -4 -4 -2 -4 -4 -4  0  7 10  0 -2  0 -3 -4 -2 -8
# W -7 -6 -6 -2 -5 -6 -2 -5 -7 -7 -4 -5 -3 -2 -3  0  0 17 -4  8 -5 -6 -4 -8
# M -3 -1  2  4  2 -2 -2 -1 -3 -2 -2 -1  0  0 -2  0 -2 -4  6 -5 -2 -2 -1 -8
# C -3 -2 -2 -6 -2 -3  0 -2 -5 -5 -4 -5 -5 -4 -3 -4  0  8 -5 12 -4 -5 -3 -8
# B  0  0 -2 -3 -2 -1  0  0  3  3  2  1  1 -1  1 -4 -3 -5 -2 -4  3  2 -1 -8
# Z  0  0 -2 -3 -2  0  0 -1  3  3  1  3  0  0  2 -5 -4 -6 -2 -5  2  3 -1 -8
# X -1  0 -1 -1 -1 -1  0  0 -1 -1  0 -1 -1 -1 -1 -2 -2 -4 -1 -3 -1 -1 -1 -8
#   -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8  1 
# 	 G  A  V  L  I  P  S  T  D  E  N  Q  K  R  H  F  Y   W  M  C  B  Z   X
import numpy as np 
from matrices import given_matrices_inserter

#TODO global conf = {}

#global score_matrix 
#score_matrix = np.zeros((10,10))
#global GIVEN
#global GIVEN2 
#GIVEN2 = False

def match_score(c1, c2, m, mm, letters):
	global GIVEN, GIVEN2, score_matrix, SCORE_MATRIX
	GIVEN2 = True
	mapped_values = {}
	if GIVEN:
		mapped_values = {'A' : 0, 'a' : 0,
						'T' : 1, 't' : 1,
						'C' : 2, 'c' : 2,
						'G' : 3, 'g' : 3}
		a = mapped_values[c1]
		b = mapped_values[c2]
		return SCORE_MATRIX[a][b]
	elif GIVEN2:
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

def global_alignment_protein(first, second, letters):
	match_score("A", "G", 5, 10, letters)
	print("globalno 1")
	
def local_alignment_protein(first, second):
	print("lokalno 1")