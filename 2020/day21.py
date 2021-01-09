import re
from collections import Counter

with open('input_files/day21') as f:
    foods = f.read().splitlines()

count = Counter()
known = {}
for food in foods:
    ingredients, allergens = re.match(r'(.+) \(contains (.+)\)', food).groups()
    ingredients = ingredients.split()
    count.update(ingredients)
    for allergen in allergens.split(', '):
        if allergen in known:
            known[allergen] &= set(ingredients)
        else:
            known[allergen] = set(ingredients)

unsafe_ingredients = set.union(*known.values())

print(sum(c for ingredient, c in count.items() if ingredient not in unsafe_ingredients))

matched = set()
while len(matched) < len(known):
    for allergen, ingredients in known.items():
        if len(ingredients) == 1:
            matched.update(ingredients)
        else:
            known[allergen] -= matched

print(','.join(ingredient.pop() for _, ingredient in sorted(known.items())))
