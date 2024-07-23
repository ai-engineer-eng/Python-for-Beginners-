#make list comprehension of this problem

animals = ["lion", "tiger", "moneky", "elephent", "frog"]
filtered_animals = []
# for animal in animals:
#     filtered_animals.append(animal.title())
# print(filtered_animals)

filtered_animals = [animal.title() for animal in animals]
print(filtered_animals)