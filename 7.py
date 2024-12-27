class IterableWithGenerator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        
        return (item ** 2 for item in self.data)  

iterable_object = IterableWithGenerator([1, 2, 3, 4, 5])

for value in iterable_object:
    print(value)
