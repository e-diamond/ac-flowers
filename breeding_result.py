
class BreedingResult:

    # lists probabilities of each gene pair outcome
    combinations = {
                    '00':[("0", 1.0)],
                    '01':[("0", 0.5), ("1", 0.5)],
                    '02':[("1", 1.0)],
                    '11':[("0", 0.25), ("1", 0.5), ("2", 0.25)],
                    '12':[("1", 0.5), ("2", 0.5)],
                    '22':[("2", 1.0)]
    }

    # each instance of BreedingResult calculates potential children of two specific flowers
    def __init__(self, f1, f2):
        # generates list of keys for accessing combinations
        self.keys = [''.join(sorted(i)) for i in zip(f1, f2)]

        # create list of children and spawn probabilities
        self.children = []
        self.offspring(0, "", 1)

    # recursively finds children & probs by looping through dict entries listed in self.keys
    def offspring(self, index, string, prob):

        if index == len(self.keys):
            for i in BreedingResult.combinations[self.keys[index-1]]:
                self.children.append((string, prob))
                return True
        else:
            for i in BreedingResult.combinations[self.keys[index]]:
                self.offspring(index+1, string+i[0], prob*i[1])
