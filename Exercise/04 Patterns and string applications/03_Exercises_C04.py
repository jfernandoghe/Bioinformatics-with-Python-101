#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
# The sequence contains a recognition site for the EcoRI restriction enzyme, which
# cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk).
# Write a program which will calculate the size of the two fragments that will be
# produced when the DNA sequence is digested with EcoRI.
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))
#     Credits to: Python for Biologist
#                 Dr. Martin Jones
#                 http://www.pythonforbiologists.com/
