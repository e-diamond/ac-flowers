from utility import *

"""This class deals only in gene strings, not Flower objects"""
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

    # stores the offspring of every possible flower combination
    all = []

    # each instance of BreedingResult calculates potential children of two specific genes
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

        # generates list of keys for accessing combinations
        self.keys = [''.join(sorted(i)) for i in zip(f1, f2)]

        # create list of children and spawn probabilities
        self.children = []
        self.offspring(0, "", 1)

    # recursively finds children & probs by looping through dict entries listed in self.keys
    def offspring(self, index, string, prob):

        if index == len(self.keys):
            for i in BreedingResult.combinations[self.keys[index-1]]:
                self.children.append({'genes':string, 'prob':prob})
                return True
        else:
            for i in BreedingResult.combinations[self.keys[index]]:
                self.offspring(index+1, string+i[0], prob*i[1])

    # generates the offspring of every possible flower combination
    @classmethod
    def generateAll(cls, species=None):
        # account for roses having an extra gene
        if species == "rose":
            genes = [pad(ternary(i, 10), 4) for i in range(81)]
        else:
            genes = [pad(ternary(i, 10), 3) for i in range(27)]

        for i in range(len(genes)):
            for j in range(i, len(genes)):
                cls.all.append(BreedingResult(genes[i], genes[j]))

    # clear 'all' list if changing species is required (only to and from rose)
    @classmethod
    def clearAll(cls):
        cls.all = []
