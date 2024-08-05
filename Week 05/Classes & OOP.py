class Laptops:
    # RAM = "8 GB"
    def __init__(self, name, RAM):
        print("adding new student in database...")
        self.name = name
        self.RAM = RAM

lap1 = Laptops("HP Elite Book - 3340", "8 GB")
print(lap1.name, lap1.RAM)
# print(lap1.RAM)