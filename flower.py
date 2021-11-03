from json_handling import JSON
from utility import *

class Flower:

    color_data = JSON.readFromFile("json/colors.json")

    def __init__(self, genes, species):
        self.genes = genes
        self.species = species
        self.color = Flower.getColor(genes, species)

    @staticmethod
    def getColor(genes, species):
        return Flower.color_data[decimal(genes, 3)][species]
