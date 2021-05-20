'''
NAME
        Droshophyla_genes.py
VERSION
        [0.1]
AUTHOR
        Diana H. Oaxaca <hoaxacadiana@gmail.com>
        GitHub:
        
DESCRIPTION
        Programa que proporciona informacion de los genes que contiene un archivo con secuencias proteicas
CATEGORY
        Secuencia proteica
USAGE
        python3 src/Droshophyla_genes.py
OPTIONS
        NA
INPUT
       6.data.csv 
       
OUTPUT
            Melanogaster y  genes:
            Genes con longitud entre 90 y 100 aminoacidos:
            Genes con AT=50% y altos niveles de expresion:
            Genes que comienzan con K y h pero no son D. melanogaster:
'''

# calcular el contenido de AT
def at_cont(sequence):
    a_content = (sequence.upper()).count("A")
    t_content = (sequence.upper()).count("T")
    at_content = (a_content + t_content) / len(sequence)
    return at_content


# Function that prints the names of the genes that belong to Drosophila melanogaster and Drosophila simulans
def print_by_specie(all_lines):
    for line in all_lines:
        divided_lines = line.split(',')
        if divided_lines[0] == "Drosophila melanogaster" or divided_lines[0] == "Drosophila simulans":
            print(divided_lines[2])

    print("")


# Function that prints the names of genes between 90 and 110 bases in length.
def print_by_length(all_lines):
    for line in all_lines:
        divided_lines = line.split(',')
        if len(divided_lines[1]) >= 90 and len(divided_lines[1]) <= 110:
            print(divided_lines[2])
    print("")


# Function that prints the names of genes whose AT content is less than 0.5 and whose expression level
# is greater than 200.
def print_by_expression(all_lines):
    for line in all_lines:
        divided_lines = line.split(',')
        if at_rich(divided_lines[1]) < 0.5 and int(divided_lines[3]) > 200:
            print(divided_lines[2])
    print("")


# Function that prints the names of genes whose names begin with "k" or "h", except those belonging
# to Drosophila melanogaster.
def print_by_letter(all_lines):
    for line in all_lines:
        divided_lines = line.split(',')
        if (divided_lines[2].startswith("k") or divided_lines[2].startswith("h")) and divided_lines[0] != "Drosophila melanogaster":
            print(divided_lines[2])
    print("")


# Function prints the name of the gene and says if its AT content is high (greater than 0.65),
# low (less than 0.45) or medium (between 0.45 and 0.65).
def print_by_AT_content(all_lines):
    for line in all_lines:
        divided_lines = line.split(',')
        if at_rich(divided_lines[1]) > 0.65:
            print("Gene with high AT content: " + divided_lines[2])
        elif at_rich(divided_lines[1]) < 0.45:
            print("Gene with low AT content: " + divided_lines[2])
        else:
            print("Gene with medium AT content " + divided_lines[2])


# The file opens
input_file = open("data/6-data.csv", "r")

# Here all the lines of the file are stored in the variable all_lines
all_lines = input_file.readlines()

# The file is closed
input_file.close()

# The messages corresponding to each function are printed and the functions are also called
print("Melanogaster and simulans genes: ")
print_by_specie(all_lines)
print("Genes of length between 90 and 110: ")
print_by_length(all_lines)
print("Genes with 50% AT and high levels of expression: ")
print_by_expression(all_lines)
print("Genes that start with 'k' and 'h' but are not from Drosophila melanogaster: ")
print_by_letter(all_lines)
print_by_AT_content(all_lines)
