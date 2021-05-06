'''
NAME
        4_add_multi_headers.py
VERSION
        [0.1]
AUTHOR
        Diana H. Oaxaca <hoaxacadiana@gmail.com>
        https://github.com/DianaOaxaca/Python_2021/blob/master/src/4_add_multi_headers.py
DATE
        29-04-21
DESCRIPTION
        Programa que agrega un identificador de secuencia y su secuencia para convertir la información a formato fasta
CATEGORY
        DNA sequence
USAGE
        python3 src/4_add_multi_headers.py
OPTIONS
        NA
INPUT
        dna [DNA sequence]
OUTPUT
        [Secuences in fasta format]
EXAMPLE
        [input] seq1= "ATCGTACCGA"
        [output] >seq1
                 ATCGTACCGA
'''
#Pedir un archivo con secuencias de DNA
input_file_name=input()
#Generar un archivo fasta con las secuencias del input
output_file=open("4_dna_sequences.fasta", "w")
#asiganar una variable al input file
input_file = open(input_file_name, "r")
#Leer lineas del archivo
input_file_content = input_file.readlines()
#cerrar archivo
input_file.close()
#For
for line in input_file_content:
    line_split= line.split("=")
    headers= line_split[0]
    seq=line_split[1]
    seq=seq.replace('"','')
    seq=seq.replace(' ','')
    seq=seq.replace('-','')
    #content=print(">"+str(headers),"\n",str(seq.upper()))
    content=">"+headers+"\n"+seq.upper()
    output_file.write(content)
output_file.close()
