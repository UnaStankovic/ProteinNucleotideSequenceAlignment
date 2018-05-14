#This file contains alignment of protein and nucleotide sequences. 
#Firstly, we recognize if sequence is a nucleotide or a protein.
#Secondly, from nucleotide sequences we extract potential coding subsequence (from START to STOP codon). 
#Thirdly, codons are translated into aminoacids. 
#Finally, protein sequences are aligned. 

def protein_or_nucleotide(sequence):
	p = 0
	for i in range(len(sequence)):
		if sequence[i] in {"A","C","G","T","a","c","g","t"}:
			p += 1
	if p == len(sequence):
		print("Nucleotide. It will be translated into aminoacid.")
		return sequence
	else:
		print("Protein.")
		return -1
		
#DNA to RNA
def dna_to_rna(dna):
	if dna.find(".txt") != -1:
		try:
			dna = open('dna.txt', 'r')
		except FileNotFoundError:
			print("The file does not exist.")
			exit()
		content = dna.read()
		content = content.replace('\n','')
		content = content.replace('T','U')
		rna = open(dna, 'w')
		rna.write(content)
		print("DNA to RNA transcription completed.")
	else:
		rna = dna.replace('T','U')
	return rna_to_aa(rna)

#RNK to AA
def rna_to_aa(drna):
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
		
	if rna.find('.txt') != -1:
		try:
			rna = open(drna, 'r')
			RNA = rna.read()
		except FileNotFoundError:
			print("The file does not exist.")
			exit()
	else:
		RNA = rna
		
	start = RNA.find('AUG')
	protein_sequence = ""
	while start + 2 < len(RNA):
		codon = RNA[start:start+3]
		if map[codon] == "STOP":
			break;
		protein_sequence += map[codon]
		start += 3
	print(protein_sequence)	
	return protein_sequence