"""
Program Description: This program takes a given DNA sequence translates it to a protein sequence.

Author: Taaruni Ananya
"""

import helper

def transcription(dna_sequence):
    complement = ''
    
    # Replace Thyamine with Uracil
    replaced = dna_sequence.replace('T', 'U')

    # Create the Base Pair Complement
    for element in replaced:
        if element == 'A':
            complement += 'U'
        elif element == 'U':
            complement += 'A'
        elif element == 'G':
            complement += 'C'
        elif element == 'C':
            complement += 'G'

    mrna = complement
    return mrna

def translate(mrna):
    protein = ''
    triplets = []

    # Split mrna into nucleotide triplets
    triplets = helper.chunk(mrna, 3)

    # Replace Triplets with Amino Acids
    for triplet in triplets:
        if triplet in helper.amino_acids:
            protein += helper.amino_acids[triplet] + ' '

    return protein.strip()

dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

print()
print('DNA Sequence')
print(dna)

print()

print('mRNA Sequence')
mrna_sequence = transcription(dna)
print(mrna_sequence)

print()

print('Protein Sequence')
protein_sequence = translate(mrna_sequence)
print(protein_sequence)
print()
