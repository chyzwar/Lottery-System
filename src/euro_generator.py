import euro_analysis as ea
import euro_data as ed
import random
import pprint


class EuroGenerator:

    def build_weights_data(self):
        data = ed.EuroData("../data/winning_results.csv")
        analysis = ea.EuroAnalysis()

        winning_numbers, num_len = data.read_winners(
            "../data/winning_results.csv")

        winning_freqs = analysis.number_freq(winning_numbers)
        dips_freqs = analysis.dip_freq(winning_numbers)

        weights_numbers = [float(x) / float(num_len) for x in winning_freqs]
        weights_dips = [float(x) / float(num_len) for x in dips_freqs]

        return weights_numbers, weights_dips

    def generate_euromilions(self, number):
        weights_numbers, weights_dips = self.build_weights_data()
        results = [[[], []] for _ in range(0, number)]

        for j in range(0, number):
            for i in range(1,  50):
                number = self.weighted_choice(weights_numbers)
                dips = self.weighted_choice(weights_dips)
                results[j][0].append(number)
                results[j][1].append(dips)

        final_results = []
        for res in results:
            final_results.append(sorted(random.sample(set(res[0]), 5)))
            final_results.append(sorted(random.sample(set(res[1]), 2)))
        return final_results

    def weighted_choice(self, weights):

        total = 0
        winner = 0
        for i, w in enumerate(weights, start=1):
            total += w
            if random.random() * total < w:
                winner = i
        return winner


generator = EuroGenerator()
pp = pprint.PrettyPrinter(depth=7)
pp.pprint(generator.generate_euromilions(8))
