#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
# Write a program that will print the complement of this sequence.
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 't')
print(replacement1)
replacement2 = replacement1.replace('T', 'a')
print(replacement2)
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
replacement4 = replacement3.replace('G', 'c')
print(replacement4)
print(replacement4.upper())
#     Credits to: Python for Biologist
#                 Dr. Martin Jones
                  http://www.pythonforbiologists.com/
