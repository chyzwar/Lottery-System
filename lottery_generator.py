from __future__ import print_function
import pandas as pd

# Read "human generated" combinations, and keep only numbers (not stars in
# this tutorial)
humandata = pd.read_csv(
    "winning_results.csv", sep=",")
humandata = humandata[['id', 'day', 'day_number', 'month', 'year', 'n1', 'n2', 'n3', 'n4', 'n5', 'd1', 'd2', 'cash', 'win']]

humandatalen = humandata.shape[0]

# Create a set of random combinations, with the same size as the "human
# generated" dataset
randomdata = []
for i in range(humandatalen):
    randomdata.append(sorted(np.random.choice(50, 5, replace=False) + 1))
randomdata = np.array(randomdata)
randomdata = pd.DataFrame(randomdata,
                          index=[
                              i + humandatalen for i in range(humandatalen)],
                          columns=['c1', 'c2', 'c3', 'c4', 'c5'])
randomdatalen = randomdata.shape[0]

# Concatenate the 2 datasets : human + random
alldata = humandata.append(randomdata)

print("Number of human euromillions combinations : ", humandatalen)
print("Number of random euromillions combinations : ", randomdatalen)
print(randomdata.head(10))
