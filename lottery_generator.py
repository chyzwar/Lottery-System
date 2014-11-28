from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split

# Read result from past euro millions draws, data is cleaned
winning_numbers = pd.read_csv("winning_results.csv", sep=",")
winning_numbers = winning_numbers[['n1', 'n2', 'n3', 'n4', 'n5', 'd1', 'd2']]
winning_numbers_len = winning_numbers.shape[0]
print(winning_numbers_len)


# Create a set of random combinationssem size as winning results
randomdata = []
for i in range(winning_numbers_len):
    randomdata.append(sorted(np.random.choice(50, 5, replace=False) + 1) + sorted(np.random.choice(11, 2, replace=False) + 1))
randomdata = np.array(randomdata)
randomdata = pd.DataFrame(randomdata,
                          index=[
                              i + winning_numbers_len for i in range(winning_numbers_len)],
                          columns=['n1', 'n2', 'n3', 'n4', 'n5', 'd1', 'd2'])
randomdata_len = randomdata.shape[0]


# Concatenate the 2 datasets : winners + random
alldata = winning_numbers.append(randomdata)

print("Number of past winning euromillions combinations : ", winning_numbers_len)
print("Statistical properties of winning resuslts data")
print(winning_numbers.describe())

print("Number of random generated euromillions combinations : ", randomdata_len)
print("Statistical properties of random data")
print(randomdata.describe())


# Heat map for best numbers, More work needed
print("Numbers that are most offten in winners combinations:")
freqs = []
for val in range(50):
    count = ((winning_numbers['n1'] == val+1).sum() +
             (winning_numbers['n2'] == val+1).sum() +
             (winning_numbers['n3'] == val+1).sum() +
             (winning_numbers['n4'] == val+1).sum() +
             (winning_numbers['n5'] == val+1).sum())
    freqs.append(count)

ax = plt.gca()
ax.invert_yaxis()
plt.gcf().set_size_inches(20, 25)
heatmap = plt.pcolor(np.reshape(np.array(freqs), (10, 5)), cmap=plt.cm.Blues)
plt.show()




# Machine Learning part
X = np.array(alldata)
# We will code with "0" the human combinations, and with "1" the random combinations
y = np.array([0] * winning_numbers + [1] * randomdata_len)

# We split our data set in 2 parts :
# A "train set" (80% of the available data) : used to train the model
# A "test set" (20% of the available data) : used to evaluate the model performance
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=43)

# In this example we use a Random Forest model. Many other are available in the scikit-learn library
model = RandomForestClassifier(n_estimators=100)

# We train the model on the "train set"
model.fit(X_train, y_train)
