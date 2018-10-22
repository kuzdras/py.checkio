"""
Source: https://py.checkio.org/en/mission/pawn-brotherhood/

Description:
A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.
You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer.
"""

def safe_pawns(pawns: set) -> int:
    i = 0
    indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        indexes.add((row,col))
    
    for row, col in indexes:
        safe = ((row -1, col -1) in indexes) or ((row -1, col + 1) in indexes)
        if safe:
            i+=1
    return i
