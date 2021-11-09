from breeding_result import BreedingResult
from json_handling import JSON
from utility import *

class Flower:

    # list of all valid flower species
    species_list = ("rose", "tulip", "pansy", "cosmos", "lily", "hyacinth", "windflower", "mum")
    colors = ("black", "blue", "green", "orange", "pink", "purple", "red", "white", "yellow")

    # read data from json files
    color_data = JSON.readFromFile("json/colors.json")
    gene_data = JSON.readFromFile("json/genes.json")
    seed_data = JSON.readFromFile("json/seeds.json")

    def __init__(self, genes, species):
        self.genes = genes
        self.species = species
        self.color = Flower.getColor(genes, species)
        self.parents = []

    # flowers only need same genes and species to be equivalent
    def __eq__(self, other):
        if isinstance(other, Flower):
            return (self.genes, self.species, self.color) == (other.genes, other.species, other.color)
        else:
            return False

    # determines if flower available from seed bag
    def isSeed(self):
        return self.genes in Flower.seed_data[self.species]

    # find every possible pair of parents which can produce this flower
    # TODO: exclude parents that are equal to self: if we already have a flower we don't need to make it again!!!
    def getParents(self):
        for result in BreedingResult.all:
            for child in result.children:
                if child['genes'] == self.genes:
                    self.parents.append({'parents':(Flower(result.f1, self.species), Flower(result.f2, self.species)), 'prob':child['prob']})
                    break

    @staticmethod
    def getColor(genes, species):
        return Flower.color_data[decimal(genes, 3)][species]

    @staticmethod
    def getGenes(color, species):
        return Flower.gene_data[color][species]

    # generate flowers available from seed bags
    @staticmethod
    def getSeeds(species):
        seed_genes = Flower.seed_data[species]
        return [Flower(genes, species) for genes in seed_genes]
