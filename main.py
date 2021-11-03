from flower import Flower
from breeding_result import BreedingResult
from json_handling import JSON

flower_types = ("rose", "tulip", "pansy", "cosmos", "lily", "hyacinth", "windflower", "mum")

species = input("Flower species: ").lower()
if species == "chrysanthemum":
    species = "mum"

if species in flower_types:
    # get seed genes for species
    seed_data = JSON.readFromFile("json/seeds.json")
    seed_genes = seed_data[species]

    # generate flowers produced by seeds
    seeds = [Flower(genes, species) for genes in seed_genes]

    # generate breeding pairs
    pairs = []
    for i in range(len(seeds)):
        for j in range(i, len(seeds)):
            pairs.append(BreedingResult(seeds[i], seeds[j]))

    for pair in pairs:
        print("Parents: ", pair.f1.genes, pair.f1.color, pair.f2.genes, pair.f2.color)
        for child in pair.children:
            print(child[0].genes, child[0].color, child[1])


else:
    print("Not a valid flower species")
