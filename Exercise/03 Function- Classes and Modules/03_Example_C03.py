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

def compDNA (DNA1, DNA2):


class Human:
    humanCo = 0
    def __init__(self, name, DNA, DNAti):
         self.name = name
         self.DNA = DNA
         self.DNAti = DNAti
         Human.humanCo += 1
    def showAt(self):
        print('Lenght of DNA: ', len(self.DNA))
        print('Title for DNA of', self.name, ' is ', self.DNAti)

i = 0
ti = {}
sq = {}
with open('HOMO.fa') as fp:  #Name of the file, *.fa
    for name, seq in read_fasta(fp):
        ti[i] = name
        sq[i] = seq
        #print(name, seq)
        i = i + 1
sophia = Human("Sophia", sq[0], ti[0])
sophia.showAt()
