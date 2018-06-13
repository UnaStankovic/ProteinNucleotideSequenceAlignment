#This file contains alignment of multiple sequences using CLUSTALW algorithm.
# By default we are using Neighbour Joining algorithm for clustering.
import sys
import getopt
import numpy as np
import collections
from utilities import sequence_input_check, input_check
from first import global_alignment
from matrices import custom_matrix, premade_score, matrix_chooser
from first import match_score


It = collections.Iterable
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
node_dict = dict()
letter_dict = dict()
order_of_alignment = list()

def global_alignment_clustalw(first, second, letters, matrix, match, mismatch, gap):
	print('We are aligning: ', first, ' and ', second)
	if matrix.all() == 0:
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

	# print(first_p)
	# print(second_p)
	return second_p

def match_mis_gap_chooser():
	print("Do you want to manually choose values for match, mismatch and gap?")
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
	else:
		match = 5
		mismatch = -1
		gap = -2
	return match, mismatch, gap

def map_letters_to_seq(input_seqs):
    num_of_seqs = len(input_seqs)
    for i in range(num_of_seqs):
        letter_dict[letters[i]] = input_seqs[i]

def calculate_distance_matrix(input_seqs):
    length = len(input_seqs)
    distance_matrix = np.zeros((length, length))
    for first in range(length):
        for second in range(first + 1, length):
            score = 0
            for i in range(len(input_seqs[first])):
                score +=  0 if input_seqs[first][i] ==  input_seqs[second][i] else 1
            distance_matrix[first][second] = score
            distance_matrix[second][first] = score
    return distance_matrix

def groups(L,N=3):
    R = range(0,len(L),N)
    return [L[i:i+N] for i in R]

def one_round(A,otus,count):
    div = np.sum(A,axis=1) #"divergence" matrix
    n = A.shape[0] #get number of rows

	# two nodes only:  we're done
    if n == 2:
        dist = A[1][0]
        nD = node_dict[otus[0]]
        nD['up'] = otus[1]
        nD['d_up'] = dist
        return None,otus

	#Find the i,j to work on using divergence:
	#based on a distance matrix relating the r taxa, calculate Q-matrix and
	#find the pair of taxa for which Q(i,j) has its lowest value.
    i,j = 0,0
    low_value = A[i][j]
    for r,row in enumerate(A):
        if r == 0:  continue
        for c,col in enumerate(row):
            if c >= r:  continue
            dist = A[r][c]
            first = div[c]
            second = div[r]
            correction = (first + second)/(n-2)
            value = dist - correction
            if value < low_value:
                i,j,low_value = r,c,value

	#Merge i and j entries
	#Calculate distance of new node from tips
    new_name = digits[count]

	#Dist from node[i]
    dist =  A[i][j]
    diff = div[i] - div[j]
    dist_i = dist/2.0 + diff/(2*(n-2))
    dist_j = dist - dist_i
    node = { 'L':otus[i], 'dL':dist_i, #"L"&"R" state for "Left" and "Ridht"
             'R':otus[j], 'dR':dist_j } #"dL" & "dR" are left/right distances from divergence point to the left/right node.
    node_dict[new_name] = node

	#Calculate distances to new node,
	# i,j assigned above
    tL = list()
    ij_dist = A[i][j]
    for k in range(len(A[0])):
        if k == i or k == j:  continue
        dist = (A[i][k] + A[j][k] - ij_dist)/2
        tL.append(dist)

	#Remove columns and rows involving i or j
    if i < j:  i,j = j,i
    assert j < i
    sel = list(range(n))
    for k in [j,i]:	#Larger first
        sel.remove(k)
        A1 = A[sel,:]
        A2 = A1[:,sel]
    A = A2
	#Correct the otu names:
    otus = [new_name] + otus[:j] + otus[j+1:i] + otus[i+1:]

	#Add col at left and row at top for new node
    new_col = np.array(tL)
    new_col.shape = (n-2,1)
    A = np.hstack([new_col,A])

    new_row = np.array([0] + tL)
    new_row.shape = (1,n-1)
    A = np.vstack([new_row,A])
    return A,otus

def build_tree(distance_matrix):

    N = len(distance_matrix)
    otus = list(letters[:N])
    A = distance_matrix
    count = 0

    while True:
        A,otus = one_round(A,otus,count)
        if A is None:  break
        count += 1

    node_t = -1
    kL = ['L','dL','R','dR','up','d_up']
    for node in sorted(node_dict.keys()):
        for k in kL:
            nD = node_dict[node]
            if not k in nD:
                continue
            v = nD[k]
            if (str(v).isalpha()):
                order_of_alignment.append(str(v))
    print('The order of alignment is: ', order_of_alignment)
    print(multiple_alignment())

def multiple_alignment():
    letters_actg = ['A','C','T','G', '-']
    seq_len = len(order_of_alignment)
    first = letter_dict[order_of_alignment[0]]
    second = letter_dict[order_of_alignment[1]]
    matrix_tmp = np.zeros((len(letters_actg), len(letters_actg)))
    match, mismatch, gap = match_mis_gap_chooser()
    tmp_result = global_alignment_clustalw(first, second, letters_actg, matrix_tmp, match, mismatch, gap)
    for i in range(2, seq_len):
        second = letter_dict[order_of_alignment[i]]
        tmp_result = global_alignment_clustalw(tmp_result, second, letters_actg, matrix_tmp, match, mismatch, gap)
    return tmp_result

def clustalw(filename):
    input_seqs = list()
    with open(filename) as openfileobject:
        for line in openfileobject:
            line = line.replace('\n', '')
            input_seqs.append(line)
    print('The sequences are: ', input_seqs)
    map_letters_to_seq(input_seqs)
    build_tree(calculate_distance_matrix(input_seqs))
