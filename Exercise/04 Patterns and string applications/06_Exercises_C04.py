#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
# Using the data from part one, write a program that will print out the original
# genomic DNA sequence with coding bases in uppercase and non-coding bases in
# lowercase.
my_dna ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATC
GATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
print(exon1 + intron.lower() + exon2)
#     Credits to: Python for Biologist
#                 Dr. Martin Jones
#                 http://www.pythonforbiologists.com/
