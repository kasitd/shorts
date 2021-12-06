import re


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    en = re.findall(r'(?:<code>([\s\S]*?)</code>)', org_text)
    tr = re.findall(r'(?:<code>([\s\S]*?)</code>)', trans_text)
    en_pre = re.findall(r'(?:<pre>([\s\S]*?)</pre>)', org_text)
    tr_pre = re.findall(r'(?:<pre>([\s\S]*?)</pre>)', trans_text)
    #print(en_pre)
    for eng, trans in zip(en, tr):
        #print(eng, trans)
        fixed = trans_text.replace(trans, eng)
        trans_text = fixed


    for eng_pre, trans_pre in zip(en_pre, tr_pre):
        fixed2 = fixed.replace(trans_pre, eng_pre)
        trans_text2 = fixed2
    return fixed2