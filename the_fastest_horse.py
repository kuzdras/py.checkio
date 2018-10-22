"""
Source: https://py.checkio.org/en/mission/the-fastest-horse/

Description: 
We have some horse racing statistics (each horse’s time in each race)
You have to find the number of the horse which has the most wins.
For example: if the results are [[“1:13”, “1:26”, “1:11”], [“1:10”, “1:18”, “1:14”], [“1:20”, “1:23”, “1:15”]] then the 3rd horse is the fastest, because it has won 2 races out of 3.
Every element in the list - is a string in format m:ss, for example, "1:05" or "2:22". 1:00 <= time <= 5:00

Input: Racing time as an array of arrays.
Output: The number of the fastest horse that has the most wins (Important: in this task the horse numbers starts from "1", not from "0")
"""

def fastest_horse(horses: list) -> int:
    new_race = []
    n_races = []
    for race in range(len(horses)):
        for r in horses[race]:
            a = r.replace(":","")
            new_race.append(int(a))
        n_races.append(new_race)
        new_race = []

    horse_list = [x for x in zip(*n_races)]
    fastest = []
    for n in n_races:
        fastest.append(min(n))

    scores  = []
    for run_time in fastest:
        for horse in horse_list:
            if run_time in horse:
                scores.append(horse_list.index(horse) + 1)

    return max(scores, key = scores.count)
