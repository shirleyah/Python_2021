'''
NAME
	[get_hydrophilic_aminoacids].py
VERSION
	[0.1]
AUTHOR
	Diana H. Oaxaca <hoaxacadiana@gmail.com>
DATE
	[06/06/2021]
DESCRIPTION
	[Programa que utiliza una funcion para calcular el porcentaje de
     amoniacidos hidrofilicos de una secuencia proteica]
CATEGORY
	[Secuencia proteica]
USAGE
	[get_hydrophilic_aminoacids.py]
ARGUMENTS
	NA
FUNCTIONS
	[get_aa_content] [protein, aminoacids]
	[Obtain percentage of aminoacids from protein sequence]
INPUT
	[Secuencia de aminoacidos]
OUTPUT
	[Porcentaje de aminoacidos hidrofilicos]
EXAMPLE
	[input: MSRSLLLRFLLFLLLLPPLP]
	[output: The percentage of hydrophilic aminoacids in your protein is: 65.0 ]
GITHUB LINK
	https://github.com/DianaOaxaca/Python_2021/blob/master/src/get_hydrophilic_aminoacids.py
'''
#Obtain percentage of aminoacids from protein sequence
def get_aa_content(protein, aminoacids):
    lenght = len(protein)
    percentage = 0
    for aa in aminoacids:
        aa_count = protein.upper().count(aa)
        percentage += aa_count * 100 / lenght
    return percentage

#Define hydrophilic aminoacids
hydrophilic_aa = ['A','I','L','M','F','W','Y','V']

#Analyze the user's protein
print("Introduce sequence protein to analyze")
protein_target =  input()
print("The percentage of hydrophilic aminoacids in your protein is: " + str(get_aa_content(protein_target, hydrophilic_aa)))

#Probe the code
assert get_aa_content("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_content("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_content("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_content("MSRSLLLRFLLFLLLLPPLP", hydrophilic_aa) == 65
