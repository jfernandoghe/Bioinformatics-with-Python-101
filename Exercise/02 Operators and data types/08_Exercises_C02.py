#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string ss is the string scsc formed by reversing the symbols of ss, then taking the complement of each
# symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string ss of length at most 1000 bp.
# Return: The reverse complement scsc of ss.
# The reverse complement of a DNA string is formed by reversing the string and taking the complement of each symbol.
# We must reverse the string in addition to taking complements because of the directionality of DNA: DNA replication and transcription
# occurs from the 3' end to the 5' end, and the 3' end of one strand is opposite from the 5' end of the complementary strand. Thus, if we
# were to simply take complements, then we would be reading the second strand in the wrong direction.
my_dna = input()
my_dna2 = ""
for i in range(0, len(my_dna)):
    if my_dna[i] == "A":
        my_dna2 = my_dna2 + 'T'
    elif my_dna[i] == "C":
        my_dna2 = my_dna2 + 'G'
    elif my_dna[i] == "T":
        my_dna2 = my_dna2 + 'A'
    elif my_dna[i] == "G":
        my_dna2 = my_dna2 + 'C'
myst = my_dna2[::-1]
print(myst) 
#     Credits to: Rosalind Website
#                 http://rosalind.info/problems/rna/
