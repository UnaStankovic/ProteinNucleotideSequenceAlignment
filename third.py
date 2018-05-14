#This file contains alignment of protein and nucleotide sequences. 
#Firstly, we recognize if sequence is a nucleotide or a protein.
#Secondly, from nucleotide sequences we extract potential coding subsequence (from START to STOP codon). 
#Thirdly, codons are translated into aminoacids. 
#Finally, protein sequences are aligned. 


#DNA to RNA
def dna_to_rna():
	dna = open('dna.txt', 'r')
	content = dna.read()
	content = content.replace('\n','')
	content = content.replace('T','U')
	rna = open('rna.txt', 'w')
	rna.write(sadrzaj)
	print("DNA to RNA transcription completed.")

#RNK to AA
def rna_to_aa():
	map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
	    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
	    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
	    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
	    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
	    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
	    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
	    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
	    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
	    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
	    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
	    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
	    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
	    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
	    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
	    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
	
	rna = open('rna.txt', 'r')
	RNA = rna.read()
	start = RNA.find('AUG')
	protein_sequence = ""

	while start + 2 < len(RNA):
	    codon = RNA[start:start+3]
	    if map[codon] == "STOP":
	        break;
	    protein_sequence += map[codon]
	    start += 3
	print(protein_sequence)
