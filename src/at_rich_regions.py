'''
NAME
	[at_rich_regions].py
VERSION
	[0.1]
AUTHOR
	Diana H. Oaxaca <hoaxacadiana@gmail.com>
DATE
	[010/06/2021]
DESCRIPTION
	[Program that obtain AT rich regions in a sequencen of DNA]
CATEGORY
	[dna sequence]
USAGE
	[at_rich_regions][NA]
ARGUMENTS
	NA
	
FUNCTIONS
	[check_seq] [dna]
	[function that obtain rich AT regions from dna sequences, value errors and return it]
INPUT
	[dna sequence]
OUTPUT
	[Sentence with at rich regions or error if there are, see example]
EXAMPLE
    at_rich_regions.py
	The AT rich regions are: ATTATAT
    The AT rich regions are: AAATTATA
GITHUB LINK
	
'''

import re
class AmbiguousBaseError(Exception):
    pass

def check_seq(dna):
    check = re.finditer(r"[^ATGC]", dna)
    try:
        if re.search(r"[^ATGC]", dna):
            raise AmbiguousBaseError("ambiguous base found!")
        high_at = re.finditer(r'(([AT]){5,})', dna)
        for i in high_at:
            print("The AT rich regions are: " + i.group())
    except AmbiguousBaseError:
        error = check.group()
        position = check.start()
        print("The error caracter is: " + error + " and start in the position " + position)

dna = "CTGCATTATATCGTACGAAATTATCGCGCG"
check_seq(dna)