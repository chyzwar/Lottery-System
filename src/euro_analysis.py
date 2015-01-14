import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split


class EuroAnalysis:

    def number_freq(self, number_list):
        """Numbers that are most offten in winners combinations"""
        freqs = []
        for val in range(50):
            count = ((number_list['n1'] == val + 1).sum() +
                     (number_list['n2'] == val + 1).sum() +
                     (number_list['n3'] == val + 1).sum() +
                     (number_list['n4'] == val + 1).sum() +
                     (number_list['n5'] == val + 1).sum())
            freqs.append(count)
        return freqs
