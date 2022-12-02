import numpy as np
import pandas as pd

from day_2_input import a

df = pd.DataFrame(a)
def payoff(theirs, mine):
    payoff = 0
    if (theirs, mine) in [("A", "X"), ("B", "Y"), ("C", "Z")]:
        payoff += 3
    elif (theirs, mine) in [("A", "Y"), ("B", "Z"), ("C", "X")]:
        payoff += 6
    if mine == "X":
        payoff += 1
    elif mine == "Y":
        payoff += 2
    else:
        payoff += 3
    return payoff
pay1 = df.apply(lambda game: payoff(*game), axis=1).sum()
print("Total payoff for part 1: ", pay1)

m = {"A":0, "B":1, "C":2, "X":-1, "Y":0, "Z":1 }
rm = ["X","Y","Z"]
df[2] = df.apply(lambda game: rm[(m[game[0]] + m[game[1]])%3], axis=1)
pay2 = df.apply(lambda game: payoff(game[0], game[2]), axis=1).sum()
print("Total payoff for part 2: ", pay2)

