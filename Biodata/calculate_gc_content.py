from collections import Counter

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    c = Counter(sequence.lower())
    T = c['t']
    G = c['g']
    C = c['c']
    A = c['a']
    TOTAL = T+G+C+A
    GC_content = round(((G+C)/(A+T+G+C))*100, 2)
    return GC_content