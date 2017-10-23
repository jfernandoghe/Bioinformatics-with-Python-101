#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
# Here's a short section of genomic DNA:
# ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
# It comprises two exons and an intron. The first exon runs from the start of the
# sequence to the sixty-third character, and the second exon runs from the ninetyfirst
# character to the end of the sequence. Write a program that will print just the
# coding regions of the DNA sequence.
my_dna ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATC
GATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[0:62]
exon2 = my_dna[90:10000]
print(exon1 + exon2)
#     Credits to: Python for Biologist
#                 Dr. Martin Jones
#                 http://www.pythonforbiologists.com/
