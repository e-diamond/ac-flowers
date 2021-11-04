from json_handling import JSON
from utility import *

class Flower:

    # list of all valid flower species
    species_list = ("rose", "tulip", "pansy", "cosmos", "lily", "hyacinth", "windflower", "mum")

    # read data from json files
    color_data = JSON.readFromFile("json/colors.json")
    seed_data = JSON.readFromFile("json/seeds.json")

    def __init__(self, genes, species):
        self.genes = genes
        self.species = species
        self.color = Flower.getColor(genes, species)

    # flowers with the same attributes are equivalent
    def __eq__(self, other):
        if isinstance(other, Flower):
            return self.__dict__ == other.__dict__
        else:
            return False

    def isSeed(self):
        return self.genes in Flower.seed_data[self.species]

    @staticmethod
    def getColor(genes, species):
        return Flower.color_data[decimal(genes, 3)][species]

    # generate flowers available from seed bags
    @staticmethod
    def getSeeds(species):
        seed_genes = Flower.seed_data[species]
        return [Flower(genes, species) for genes in seed_genes]
