

my_fruits = {'apples', 'peach', 'bananas', 'pineapple', 'grape', 'melon', 'fig'}
bestie_fruits = {'mango', 'strawberry', 'melon', 'peach', 'pear'}

union_fruits = my_fruits.union(bestie_fruits)

intersection_fruits = my_fruits.intersection(bestie_fruits)

difference_fruits = my_fruits.difference(bestie_fruits)

print('Full list: ', union_fruits)
print('Intersection: ', intersection_fruits)
print('Bestie\'s friut: ', difference_fruits)