'''
NAME
        ATCG_content.py
VERSION
        [0.1]
AUTHOR
        Diana H. Oaxaca <hoaxacadiana@gmail.com>
DESCRIPTION
        Program that asks the user for a DNA sequence and returns the contents of each nucleotide.
CATEGORY
        DNA sequence
USAGE
        python3 src/ATCG_content.py
OPTIONS
        NA
INPUT
        dna [DNA sequence]
OUTPUT
        [ATCG content in the DNA sequence and RNA sequence]
EXAMPLE
        [input] AACGTTCAGT
        [output] A:3 C:2 G:2 T:3
'''
print("Escribe una secuencia de DNA:\n")#Ask the user to enter a DNA sequence
dna= input()#Allows keyboard sequence entry and maps to a variable
print(f"Esta es la secuencia de DNA a evaluar: {dna}")#Return DNA sequence
#The content of each nucleotide is assigned to a separate variable
A_count = dna.count('A')
C_count = dna.count('C')
G_count = dna.count('G')
T_count = dna.count('T')
#Returns content of each nucleotide from the DNA sequence
print(f"El contenido de cada nucleotido es:\n A:{A_count}\n C:{C_count}\n G:{G_count}\n T:{T_count}")
