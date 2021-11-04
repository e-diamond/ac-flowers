from flower import Flower
from breeding_result import BreedingResult

# determine species of interest
species = input("Flower species: ").lower()
if species == "chrysanthemum":
    species = "mum"

# check if species is valid
if species in Flower.species_list:

    # generate flowers produced by seeds
    seeds = Flower.getSeeds(species)

    produced = []
    for i in range(2):
        print("GENERATION", i, "\n")

        # generate breeding pairs
        pairs = []
        for i in range(len(seeds)):
            for j in range(i, len(seeds)):
                if seeds[j] in produced:
                    continue
                else:
                    pairs.append(BreedingResult(seeds[i], seeds[j]))

        new_gen = []
        for pair in pairs:
            print("Parents: ", pair.f1.genes, pair.f1.color, pair.f2.genes, pair.f2.color)
            for child in pair.children:
                print(child[0].genes, child[0].color, child[1])
                new_gen.append(child[0])
        print("\n\n")

        produced = produced + seeds
        seeds = seeds + new_gen


else:
    print("Not a valid flower species")
