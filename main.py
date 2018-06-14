#This file is a main file for project of Protein/Nucleotide Sequence Alignment.
#It contains interface to the four parts which make a whole, those are the following:
#1. Global and local alignment of nucleotide sequences using given matrix as a score matrix
#2. Global and local alignments of protein sequences using PAM and BLOSUM score matrices
#3. Alignment of protein and nucleotide sequences, depending on the type
#4. Alignment of multiple sequences using CLUSTALW algorithm

#List of files:
# 1. utilities - contains choosers, file openers, writers and other utilities
# 2. screens - contains alignment and option choosers for the "main screen"
# 3. first - contains alignments, global and local
# 4. second - match_score function, third file content to be moved here and match_score function moved to first
# 5. third - contains protein or nucleotide check, nucleotide to aminoacid and protein nucleotide alignment, to be moved to second
# 6. fourth - contains multiple sequences alignment, to be moved to third and removed

#TODO:
# DONE - removed global vars 0. PRIORITY : to fix global variables issues by doing 1 and 2 :D
# DONE - removed global vars 1. to reduce global variables to just one score matrix and one given
# DONE - added to settings file 2. to move global variables to one global conf = {}
# DONE - added input matrix function 3. Add custom matrix input format for nucleotide and protein - this might be useless since the num of letters and matrix for proteins is too big
# DONE - written script.py 4. fix letter reading - spaces, newlines - regex from file
# DONE - all should be reduced to minumum by now 5. possibly reduce more functions
# DONE - made minimal, renamed functions 6. option and alignment chooser to be reduced or rewritten a lot of repetetive code in there right now
# DONE - match_score function rewritten 7. in match_score function to reduce 2 GIVEN options to one by sending letters for nucleotides
# DONE - 8. to leave just one global alignment function and local_alignment function which is to be invoked by both proteins and nucleotides
# DONE - 9. to make revision of all the imports and remove unneccessary ones
# DONE - 10. Fix thrid file function calls (now second file), there should be some type of check if given sequence is correct. If not, the program crashes when
# 	there is no sequence letter in table for match_score
# DONE - 11. DO CLUSTALW
# DONE/FIXED - 12. ASAP!!!!!FIX PAM250.txt and BLOSUM45.txt so they can be used - REMOVE EXTRA SPACES(DONE), CONVERSION PROBLEM SPOTTED 
# DONE - 13. add more examples for testing 
# NOT GOING TO BE DONE - 14. add in local alignment visual representation of alignment - backtrack
# DONE - 15. Add/ remove unneccessary printfs 
# DONE - 16. Fix options 2 and 3 to disallow user to use custom matrix 
# 17. Check if local alignment really works some bugs noticed
# 18. Make easy matrix choice. 
import first, second, third, utilities
from screens import screen

def main():
        screen()

if __name__ == "__main__":
        main()
