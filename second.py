#This file contains global and local alignments of protein sequences using PAM(global alignment) and BLOSUM(local alignment) score matrix
#PAM trace evolutionary origins of proteins refers to evolutionary distance ,
# BLOSUM score alignment between evolutionarily-divergent proteins, refers to percent identity  
#PAM High number: compares distantly related proteins 
#BLOSUM High number : compares closely related proteins 
#TODO :PAM250																						 Blosum 45
#TODO: Custom reading: dim, letter array and values
# 	 G  A  V  L  I  P  S  T  D  E  N  Q  K  R  H  F  Y  W  M  C  B  Z  X  
# G  5
# A  1  2
# V -1  0  4 
# L -4 -2  2  6
# I -3 -1  4  2  5 
# P  0  1 -1 -3 -2  6
# S  1  1 -1 -3 -1  1  2
# T  0  1  0 -2  0  0  1  3 
# D  1  0 -2 -4 -2 -1  0  0  4
# E  0  0 -2 -3 -2 -1  0  0  3  4
# N  0  0 -2 -3 -2  0  1  0  2  1  2
# Q -1  0 -2 -2 -2  0 -1 -1  2  2  1  4
# K -2 -1 -2 -3 -2 -1  0  0  0  0  1  1  5
# R -3 -2 -2 -3 -2  0  0 -1 -1 -1  0  1  3  6
# H -2 -1 -2 -2 -2  0 -1 -1  1  1  2  3  0  2  6
# F -5 -3 -1  2  1 -5 -3 -3 -6 -5 -3 -5 -5 -4 -2  9 
# Y -5 -3 -2 -1 -1 -5 -3 -3 -4 -4 -2 -4 -4 -4  0  7  10
# W -7 -6 -6 -2 -5 -6 -2 -5 -7 -7 -4 -5 -3 -2 -3  0  0  17
# M -3 -1  2  4  2 -2 -2 -1 -3 -2 -2 -1  0  0 -2  0 -2  -4  6
# C -3 -2 -2 -6 -2 -3  0 -2 -5 -5 -4 -5 -5 -4 -3 -4  0  -8 -5  12
# B  0  0 -2 -3 -2 -1  0  0  3  3  2  1  1 -1  1 -4 -3  -5 -2  -4  3
# Z  0  0 -2 -3 -2  0  0 -1  3  3  1  3  0  0  2 -5 -4  -6 -2  -5  2  3
# X -1  0 -1 -1 -1 -1  0  0 -1 -1  0 -1 -1 -1 -1 -2 -2  -4 -1 -3  -1 -1 -1
#   -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8 -8  -8 -8 -8  -8 -8 -8  1 
# 	 G  A  V  L  I  P  S  T  D  E  N  Q  K  R  H  F  Y   W  M  C  B  Z   X
def global_alignment_protein():
	print("globalno 1")
	
def local_alignment_protein():
	print("lokalno 1")