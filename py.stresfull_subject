"""
Source: https://py.checkio.org/en/mission/stressful-subject/

Description:
The function should recognise if a subject line is stressful. A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string.
Output: Boolean.
"""

def is_stressful(subj):   
    import re
    helps = re.search(r"(h|H)+\W?(E|e)+\W?(L|l)+\W?(p|P)+\W?", subj)
    urgent = re.search(r"(u|U)+\W?(r|R)+\W?(g|G)+\W?(e|E)+\W?(n|N)+\W?(t|T)+\W?", subj)
    asap = re.search(r"(a|A)+\W?(s|S)+\W?(a|A)+\W?(p|P)+\W?", subj)
    if helps or urgent or asap or subj[-3:]=="!!!" or subj.isupper() == True:
        return True
    else:
        return False
