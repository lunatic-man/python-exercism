def to_rna(dna_strand):
    """This function changes a DNA strand to give you the complementary RNA output.

	Parameters:
		dna_strand(str): The DNA strand which must be operated on

	Returns:
		str: The complementary RNA output"""

    mapping = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

    new_list = [mapping[key] for key in dna_strand]
    new_str = ''.join(new_list)
    return new_str
