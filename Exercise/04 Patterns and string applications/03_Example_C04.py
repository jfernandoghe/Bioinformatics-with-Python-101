def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))
    return name, seq

i = 0
ti = {}
sq = {}
#with open('HOMO.fa') as fp:  # Name of the file, *.fa
#    for name, seq in read_fasta(fp):
#        ti[i] = name
#        sq[i] = seq
        # print(name, seq)
#        i = i + 1
read_fasta('HOMO.fa')
print(len(ti[0]))
