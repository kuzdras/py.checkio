"""
Source: https://py.checkio.org/en/mission/pangram/

Description:
For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and punctuation symbols. You need to check if the sentence is a pangram or not. Case does not matter.

Input: A text as a string.
Output: Whether the sentence is a pangram or not as a boolean.
"""

import re
def check_pangram(text):
    return len(set(re.sub(r"[^a-z]|\s","",text.lower()))) == 26
