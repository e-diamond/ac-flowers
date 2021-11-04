from flower import Flower
from breeding_result import BreedingResult

# determines if user has entered a valid flower
def valid(species, color):
    if species in Flower.species_list and color in Flower.colors:
        return Flower.getGenes(color, species) != None
    else:
        return False

# find flowers with maximum probability
def maxProb(flowers):
    max_prob = max([flower.prob for flower in flowers])
    return [flower for flower in flowers if flower.prob == max_prob]


# determine species of interest
species = input("Flower species: ").lower()
if species == "chrysanthemum":
    species = "mum"
# determine target color
color = input("Target color: ").lower()
# get probability threshold
threshold = float(input("Probability threshold: "))

# check if flower is valid
if valid(species, color):

    # fetch starting flowers
    flowers = Flower.getSeeds(species)

    # when found, exit loop
    found = False
    # list of flowers that have already been bred
    produced = []
    # list of flowers that fulfill search criteria
    targets = []

    while not found:
        print("----------------NEW GENERATION--------------------")

        # create list of pairs to breed
        pairs = []
        for i in range(len(flowers)):
            for j in range(i, len(flowers)):
                # breed flowers from previous generations only with ones from the new genration
                if flowers[j] not in produced:
                    pairs.append(BreedingResult(flowers[i], flowers[j]))

        # update list of produced flowers
        produced = [flower for flower in flowers]

        # create list of any flowers that fulfill the search criteria
        # TODO: discard duplicate flowers: use only one with the highest spawn probability
        for pair in pairs:
            for child in pair.children:
                flowers.append(child)
                if child.color == color and child.prob >= threshold:
                    parent1 = child.parents.f1
                    parent2 = child.parents.f2
                    # exclude results where a parent has the same color - by definition we don't have this color!!!
                    if parent1.color != child.color and parent2.color != child.color:
                        found = True
                        targets.append(child)

    # find child flowers with the maximum probability
    targets = maxProb(targets)
    for target in targets:
        parent1 = target.parents.f1
        parent2 = target.parents.f2
        print("Parents:", parent1.genes, parent1.color, parent2.genes, parent2.color)
        print(target.color, target.species, target.prob)


else:
    print("Not a valid flower species")
