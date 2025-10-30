MAPPING_DNA_TO_RNA = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand: str) -> str | bool:
    if any(n not in MAPPING_DNA_TO_RNA for n in dna_strand.upper()):
        return False

    return "".join(MAPPING_DNA_TO_RNA[n] for n in dna_strand.upper())
