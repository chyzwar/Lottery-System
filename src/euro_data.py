import pandas as pd
import numpy as np


class EuroData:

    def __init__(self, filename=None):
        if filename is None:
            self.filename = ""
        else:
            self.filename = filename

    def read_winners(self, filename):
        # Read result from past euro millions draws, data is cleaned
        # "winning_results.csv"
        winning_numbers = pd.read_csv(filename, sep=",")
        winning_numbers = winning_numbers[
            ['n1', 'n2', 'n3', 'n4', 'n5', 'd1', 'd2']]
        winning_numbers_len = winning_numbers.shape[0]
        return winning_numbers, winning_numbers_len

    def generate_random(self, winning_numbers_len):
        # Create a set of random combinationssem size as winning results
        randomdata = []
        for i in range(winning_numbers_len):
            randomdata.append(sorted(np.random.choice(
                50, 5, replace=False) + 1) + sorted(np.random.choice(11, 2, replace=False) + 1))
        randomdata = np.array(randomdata)
        randomdata = pd.DataFrame(randomdata,
                                  index=[
                                      i + winning_numbers_len for i in range(winning_numbers_len)],
                                  columns=['n1', 'n2', 'n3', 'n4', 'n5', 'd1', 'd2'])
        randomdata_len = randomdata.shape[0]
        return randomdata, randomdata_len

    def mix_results(winning_numbers, random_numbers):
        # Concatenate the 2 datasets : winners + random
        alldata = winning_numbers.append(random_numbers)
        alldata_len = alldata.shape[0]
        return alldata, alldata_len
