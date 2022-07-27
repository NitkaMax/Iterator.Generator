nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

class FlatIterator:
    my_list = []

    def __init__(self, main_list: list):
        self.main_list = main_list

    def __iter__(self):
        self.extract_from_the_list(self.main_list)
        return self

    def __next__(self):
        if not self.my_list:
            raise StopIteration
        return self.my_list.pop(0)

    def extract_from_the_list(self, initial_list):
        for item in initial_list:
            if isinstance(item, list):
                self.extract_from_the_list(item)
                continue
            else:
                self.my_list.append(item)

for item in FlatIterator(nested_list):
    print(item)

print('\n'+'*' * 10 + '\n')

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)