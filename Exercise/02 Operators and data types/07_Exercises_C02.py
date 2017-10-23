#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string tt corresponding to a coding strand, its transcribed RNA string uu is formed by replacing all occurrences of 'T' in tt with 'U' in uu.
#   Given: A DNA string tt having length at most 1000 nt.
#   Return: The transcribed RNA string of tt.
my_dna = input()
my_rna = my_dna.replace("T","U")
print(my_rna)
#     Credits to: Rosalind Website
#                 http://rosalind.info/problems/rna/
