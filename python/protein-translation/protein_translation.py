codon_to_protein = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand: str) -> bool | list:
    codon_chain = []
    for i in range(0, len(strand), 3):
        codon = strand[i : i + 3]
        codon_value = codon_to_protein.get(codon)
        if not codon_value:
            return False
        if codon_value.upper() == "STOP":
            return codon_chain
        codon_chain.append(codon_value)

    if not codon_chain:
        return False
    return codon_chain
