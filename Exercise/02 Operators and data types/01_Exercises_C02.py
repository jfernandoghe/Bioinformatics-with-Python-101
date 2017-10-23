#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
# Write a program that will print out the AT content of this DNA sequence. Hint: you
# can use normal mathematical symbols like add (+), subtract (-), multiply (*), divide
# (/) and parentheses to carry out calculations on numbers in Python.
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))
#     Credits to: Python for Biologist
#                 Dr. Martin Jones
#                 http://www.pythonforbiologists.com/
