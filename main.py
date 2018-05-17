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
# 3. Add custom matrix input format for nucleotide and protein - this might be useless since the num of letters and matrix for proteins is too big
# 4. fix letter reading - spaces, newlines - regex from file
# 5. possibly reduce more functions
# renamed functions 6. option and alignment chooser to be reduced or rewritten a lot of repetetive code in there right now
# 7. in match_score function to reduce 2 GIVEN options to one by sending letters for nucleotides
# DONE - 8. to leave just one global alignment function and local_alignment function which is to be invoked by both proteins and nucleotides
# 9. to make revision of all the imports and remove unneccessary ones


import first, second, third, fourth, utilities, settings
from screens import screen

def main():
        settings.init()
        screen()

if __name__ == "__main__":
        main()
