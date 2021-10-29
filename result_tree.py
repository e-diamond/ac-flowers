
# creates an entire Tree object
class ResultTree:

    def __init__(self, f1, f2):
        self.__genes = list(zip(f1, f2))
        self.root = self.makeTree()

    # creates leaf objects
    class TreeNode:
        def __init__(self, data=None, probability=None):
            self.children = []
            self.data = data
            self.prob = probability

    # initialises root node
    def makeTree(self):
        root = self.TreeNode()
        self.addNodes(root, 0)
        return root

    # recursively adds child nodes
    def addNodes(self, current, target):
        # end condition
        if target >= len(self.__genes):
            return True
        else:
            gene = self.__genes[target]

            # probabilities for each gene pair outcome
            if gene == ("0", "0"):
                current.children.append(self.TreeNode("0", 1))
            elif gene == ("0", "1") or gene == ("1", "0"):
                current.children.append(self.TreeNode("0", 0.5))
                current.children.append(self.TreeNode("1", 0.5))
            elif gene == ("0", "2") or gene == ("2", "0"):
                current.children.append(self.TreeNode("1", 1))
            elif gene == ("1", "1"):
                current.children.append(self.TreeNode("0", 0.25))
                current.children.append(self.TreeNode("1", 0.5))
                current.children.append(self.TreeNode("2", 0.25))
            elif gene == ("1", "2") or gene == ("2", "1"):
                current.children.append(self.TreeNode("1", 0.5))
                current.children.append(self.TreeNode("2", 0.5))
            elif gene == ("2", "2"):
                current.children.append(self.TreeNode("2", 1))

            # recurse into child nodes 
            for child in current.children:
                self.addNodes(child, target+1)
