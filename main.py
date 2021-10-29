from result_tree import ResultTree

result = ResultTree("1000", "1000")
children = result.root.children
for child in children:
    print("-----")
    print(child.data)
    print(child.prob)
