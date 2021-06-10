'''
NAME
	[at_arguments].py
VERSION
	[0.1]
AUTHOR
	Diana H. Oaxaca <hoaxacadiana@gmail.com>
DATE
	[8/06/2021]
DESCRIPTION
	[Program that calcule AT content of dna sequence, use arguments and error manipulations, if there are 'Ns' in the sequence, display an error]
CATEGORY
	[Class of program: dna seq analysis]
USAGE
	[at_arguments.py][ -i -o]
ARGUMENTS
	[-i] [input file with DNA sequences]
	[-o] [output file with AT content percentage]
	
EXAMPLE
	[at_arguments.py -i data/4_dna_sequences.txt -o results/at_percentage.txt]
DEPENDENCES
    library argparse
GITHUB LINK
	
'''

#Charge to libraries
import argparse
#Create parser and add arguments
parser = argparse.ArgumentParser(description= "This program calcule AT content of dna sequence, if there are 'Ns' in the sequence display an error ")
parser.add_argument("-i", "--input", metavar="path to input file with dna sequences", type=str, help="File with dna sequence", required=True)
parser.add_argument("-o", "--output", metavar="path to output file with AT content", type=str, help="File with ATcontent", required=False)
#Execute parse method
arguments = parser.parse_args()
#Define at content function without N
def get_at_content(sequence, digits=2):
    if sequence.count("N") > 0:
        raise ValueError("The sequence contain Ns")
    length = len(sequence)
    a_count = sequence.upper.count('A')
    t_count = sequence.upper.count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, digits)
#check errors
try:
    file = open(arguments.input)
except IOError:
    print("File not found, try again")
    correct_path = input("insert correct input file: ")
    data = open(correct_path)
file = data.readlines()
data.close()
#Create output file
output_file = open("results/atcontent_args.tct", "w")
for seq in file:
    file_split = seq.split(" = ")
    output_file.write('>SEQUENCE_'+file_split[0] + 'has an ' + get_at_content(file_split) + 'of AT content\n')
output_file.close()
