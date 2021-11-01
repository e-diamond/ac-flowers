from breeding_result import BreedingResult

f1 = input("First flower genes: ")
f2 = input("Second flower genes: ")

result = BreedingResult(f1, f2)
for i in result.children:
    print(i)
