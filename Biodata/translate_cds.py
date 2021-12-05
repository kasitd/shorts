from Bio.Seq import Seq


def translate_cds(cds: str, translation_table: str) -> str:
    """
    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table as defined in
           Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """
    clean_cds = "".join(c for c in cds if c.isalpha())
    nt_seq = Seq(clean_cds)
    aa_seq = nt_seq.translate(table=translation_table, cds=True)
    return str(aa_seq)