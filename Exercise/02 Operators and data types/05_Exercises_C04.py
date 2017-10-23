#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
# Using the data from part one, write a program that will calculate what percentage
# of the DNA sequence is coding.
my_dna ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATC
GATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[0:62]
exon2 = my_dna[90:10000]
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print(100 * coding_length / total_length)
#     Credits to: Python for Biologist
#                 Dr. Martin Jones
#                 http://www.pythonforbiologists.com/
