'''
NAME
        find_transcribe_sequence.py
VERSION
        [0.1]
AUTHOR
        Diana H. Oaxaca <hoaxacadiana@gmail.com>
DESCRIPTION
        Program that given a DNA sequence, find the start and end codon, and the sequence that will be transcribed.
CATEGORY
        DNA sequence
USAGE
        python3 src/find_transcribe_sequence.py
OPTIONS
        NA
INPUT
        dna_sequence [DNA sequence]
OUTPUT
        [Start and stop codon, sequence that will be transcribed and RNA sequence]
EXAMPLE
        [Program that find the start and stop codons of a  given DNA sequence, return positions, sequence to be transcribed and RNA sequence]
'''
dna_sequence = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'#input DNA sequence
start_codon = "TAC" #Define start codon
stop_codon = "TAA" #Define stop codon
sequence_transcribed = dna_sequence[4:24] #Obtain the sequence that will be transcribed
print("The TAC start codon, starting in position:", dna_sequence.find(start_codon),
      "and the TAA stop codon starting in position:", dna_sequence.find(stop_codon)) #Define output1 with start and stop codons positions
print("The sequence that will be transcribed is:", sequence_transcribed) #Define output2 with sequence to will transcribed
RNA_sequence = sequence_transcribed.replace('T', 'U') #test to RNA sequence, replace Thymine to Uracil
print("The RNA sequence is:", RNA_sequence) #Define output3 with RNA sequence