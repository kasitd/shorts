def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    if number == 0:
        return 0
    else:
        return (number% base + 10 * dec_to_base(int(number//base), base))
