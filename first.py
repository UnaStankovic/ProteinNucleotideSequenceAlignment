#This file contains global and local alignments of nucleotide or protein sequences using given matrix as a score matrix
#This file contains, also, global and local alignments of protein sequences using PAM(global alignment) and BLOSUM(local alignment) score matrix
#PAM trace evolutionary origins of proteins refers to evolutionary distance ,
#BLOSUM score alignment between evolutionarily-divergent proteins, refers to percent identity
#PAM High number: compares distantly related proteins
#BLOSUM High number : compares closely related proteins

import numpy as np
from utilities import input_check, match_mis_gap_chooser
from matrices import custom_matrix, premade_score, matrix_chooser

def match_score(c1, c2, m, mm, letters, score_matrix):
	mapped_values = {}
	for i, v in enumerate(letters):
		#print(i,v)
		mapped_values[v] = i
	#print(mapped_values)
	a = mapped_values[c1]
	b = mapped_values[c2]
	return score_matrix[a][b]

def global_alignment(first, second, letters, matrix, protein):
	match, mismatch, gap, ind = match_mis_gap_chooser("g")
	if ind == 0 and protein == 0:
		letters, matrix = matrix_chooser(letters, match, mismatch)
	n = len(first)
	m = len(second)
	backtrack = [[(-1,1) for j in range(m+1)] for i in range(n+1)]
	s = [[0 for j in range(m+1)] for i in range(n+1)]

	for i in range(1, n+1):
		s[i][0] = s[i-1][0] + gap
		backtrack[i][0] = (i-1, 0)
	for j in range(1, m+1):
		s[0][j] = s[0][j-1] + gap
		backtrack[0][j] = (0, j-1)

	for i in range(1, n+1):
		for j in range(1, m+1):
			s[i][j] = max(s[i-1][j] + gap, s[i][j-1] + gap, s[i-1][j-1] + match_score(first[i-1], second[j-1], match, mismatch, letters, matrix))
			if s[i][j] == s[i-1][j] + gap:
				backtrack[i][j] = (i-1, j)
			elif s[i][j] == s[i][j-1] + gap:
				backtrack[i][j] = (i, j-1)
			else:
				backtrack[i][j] =  (i-1, j-1)

	first_p = ""
	second_p = ""
	i = n
	j = m
	while (i,j) != (0,0):
		if backtrack[i][j] == (i-1, j-1):
			first_p = first[i-1] + first_p
			second_p = second[j-1] + second_p
		elif backtrack[i][j] == (i-1, j):
			first_p = first[i-1] + first_p
			second_p = '-' + second_p
		else:
			first_p = '-' + first_p
			second_p = second[j-1] + second_p
		(i, j) = backtrack[i][j]

	print(first_p)
	print(second_p)
	return s[n][m]

def local_alignment(first, second, letters, matrix, protein):
	match, mismatch, gap, ind = match_mis_gap_chooser("l")
	if ind == 0 and protein == 0:
		letters, matrix = matrix_chooser(letters, match, mismatch)
	#print(match, mismatch, gap)
	local_alignment = [[0 for j in range(len(second) + 1)] for i in range(len(first) + 1)]

	for i in range(len(first) + 1):
		local_alignment[i][0] = 0
	for i in range(len(second) + 1):
		local_alignment[0][i] = 0

	for i in range(1, len(first) + 1):
		for j in range(1, len(second) + 1):
			matcher = match_score(first[i-1], second[j-1], match, mismatch, letters, matrix)
			if matcher < 0:
				matcher = 0
			local_alignment[i][j] = max(0, local_alignment[i-1][j] + gap, local_alignment[i][j-1] + gap, \
										local_alignment[i-1][j-1] + matcher)
										#local_alignment[i-1][j-1] + int(first == second))

	maximum = 0
	for i in range(len(local_alignment)):
		for j in range(len(local_alignment[i])):
			if local_alignment[i][j] > maximum:
				maximum = local_alignment[i][j]

	print("Local alignment:")
	for i in range(len(local_alignment)):
		print(local_alignment[i])

	return maximum
