from flower import Flower
from breeding_result import BreedingResult

# determines if user has entered a valid flower
def valid(species, color):
    if species in Flower.species_list and color in Flower.colors:
        return Flower.getGenes(color, species) != None
    else:
        return False

"""
This solution is very beautiful, however it will, unfortunately,
run forever :(

def build(flower):
    if flower.isSeed():
        return True
    else:
        flower.getParents()
        for pair in flower.parents:
            for f in pair['flowers']:
                build(f)
"""

# TODO: DELETE level: for debugging only
# builds the family tree of a given flower
def build(flower, produced, level):
    print(level)

    # if flower is a seed, end recursion
    if flower.isSeed():
        return True
    else:
        # produced tracks all flowers that have been produced on a particular branch
        # this is better than just checking flower's direct parents
        # as loops can form over several generations, repeating infinitely 
        p_level = produced
        p_level.append(flower.genes)

        # get flower's parents
        flower.getParents(p_level)

        # p_seeds stores any parent pairs where both parents are seeds
        p_seeds = []
        # fill p_seeds
        for pair in flower.parents:
            f = pair['flowers']
            if f[0].isSeed() and f[1].isSeed():
                p_seeds.append(pair)
        # if p_seeds is not empty, flower's only parents become the pair with
        # the highest spawn probability
        if len(p_seeds) > 0:
            if len(p_seeds) > 1:
                # TODO: if two pairs have the same probability, choose the one with
                #       fewer distinct offspring
                p_seeds = max(p_seeds, key=lambda x: x['prob'])
                p_seeds = [p_seeds]
            flower.parents = p_seeds

        # build tree for each parent
        for pair in flower.parents:
            for p in pair['flowers']:
                build(p, p_level, level+1)


# determine species of interest
species = input("Flower species: ").lower()
if species == "chrysanthemum":
    species = "mum"
# determine target color
color = input("Target color: ").lower()

# check if user entered a valid flower
if valid(species, color):

    # calculate all possible breeding pairs
    BreedingResult.generateAll(species)

    # generate all flowers of the target color and species
    genes = Flower.getGenes(color, species)
    roots = [Flower(gene, species) for gene in genes]

    # build the family tree of each target flower
    for root in roots:
        build(root, [], 0)
        print("done")


else:
    print("Not a valid flower species")
