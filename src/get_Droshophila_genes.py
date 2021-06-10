'''
NAME
	[get_Droshophila_genes].py
VERSION
	[0.1]
AUTHOR
	Diana H. Oaxaca <hoaxacadiana@gmail.com>
DATE
	[06/06/2021]
DESCRIPTION
	[Program that obtain specific genes from file genes]
CATEGORY
	[dna sequence]
USAGE
	[get_Droshophila_genes.py][NA]
ARGUMENTS
	NA
	
FUNCTIONS
	[function name] [NA]
	[description]
INPUT
	[6-data.csv]
OUTPUT
	[specific genes, see example]
EXAMPLE
	[input: 6-data.csv]
    [output: Genes between 90 to 110 length are: kdy647
	Genes of D. melanogaster and D. simulans are: kdy533
	Genes between 90 to 110 length are: kdy533
	The genes names that start with 'k' and 'h' but aren't from D. melanogaster are: kdy533
	The genes names that start with 'k' and 'h' but aren't from D. melanogaster are: hdt739
	The genes names that start with 'k' and 'h' but aren't from D. melanogaster are: hdu045
	Genes between 90 to 110 length are: teg436
	The genes with high AT content is: kdy647
	The genes with medium AT content is: jdg766
	The genes with medium AT content is: kdy533
	The genes with low AT content is: hdt739
	The genes with medium AT content is: hdu045
	Genes with low AT content and high expression levels are: teg436
	The genes with medium AT content is: teg436]
	
GITHUB LINK
	https://github.com/DianaOaxaca/Python_2021/blob/master/src/get_Droshophila_genes.py
	
'''

#Define D. melanogaster or D. simulans genes and genes between 90 and 110 bases, 
# and genes names that start with 'k' and 'h' but aren't from D. melanogaster
def specific_genes(data):
	for lines in data:
		lines_split = lines.split(',')
		specie = lines_split[0]
		if specie == "Drosophila melanogaster'" or specie == "Drosophila simulans":
				genes_per_specie = lines_split[2]
				print("Genes of D. melanogaster and D. simulans are: " + genes_per_specie)
		if len(lines_split[1]) >= 90 and  len(lines_split[1]) <= 110:
				print("Genes between 90 to 110 length are: "  + lines_split[2])
		k_star = lines_split[2].startswith("k")
		h_star = lines_split[2].startswith("h")
		if (k_star or h_star) and lines_split[0] != "Drosophila melanogaster":
				print("The genes names that start with 'k' and 'h' but aren't from D. melanogaster are: " + lines_split[2])


#Define AT content
def at_rich(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return at_content


#Define specific AT content genes and expression level
def specific_at_genes(data):
	for line in data:
		split_lines = line.split(',')
		if at_rich(split_lines[1]) < 0.5 and int(split_lines[3]) > 200:
			print("Genes with low AT content and high expression levels are: " + split_lines[2])
		if at_rich(split_lines[1]) > 0.65:
			print("The genes with high AT content is: " + split_lines[2])
		elif at_rich(split_lines[1]) < 0.45:
			print("The genes with low AT content is: " + split_lines[2])
		else:
			print("The genes with medium AT content is: " + split_lines[2])


#read file
input_file = open("data/6-data.csv", "r")
data = input_file.readlines()
input_file.close()

#print results
specific_genes(data)
specific_at_genes(data)
