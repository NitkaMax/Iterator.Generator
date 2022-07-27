nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

class FlatIterator:
    
    def __init__(self, main_list: list):
        self.main_list = main_list

    def __iter__(self):
        self.my_list = []
        for i in self.main_list:
            self.my_list += i
        return self

    def __next__(self):
        if not self.my_list:
            raise StopIteration
        return self.my_list.pop(0)

for item in FlatIterator(nested_list):
    print(item)

print('\n'+'*' * 10 + '\n')

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)