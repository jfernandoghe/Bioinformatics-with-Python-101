#     Bioinformatics with Python 101
#     José Fernando González Herrera
#     jfernandoghe@gmail.com
def read_fasta(fp):
j = 0
name, seq = None, []
for line in fp:
line = line.rstrip()
if line.startswith(">"):
if name: yield (name, ''.join(seq))
name, seq = line, []
else:
seq.append(line)
if name: yield (name, ''.join(seq))
j = j + 1
i = 0
ti = {}
sq = {}
with open('input.fa') as fp: #Name of the file, *.fa
for name, seq in read_fasta(fp):
ti[i]=name
sq[i]=seq
print(name, seq)
i = i + 1
