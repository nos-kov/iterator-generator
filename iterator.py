class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):

        self.i = 0
        self.j = -1

        return self

    def __next__(self):

        if self.i < len(self.list_of_list)-1:
            
            if self.j < len(self.list_of_list[self.i]):
                if self.j == len(self.list_of_list[self.i])-1:
                    self.i += 1
                    self.j = -1
            self.j += 1
        else:
            if self.i == len(self.list_of_list) or self.j == len(self.list_of_list[self.i])-1:
                raise StopIteration
            else:
                self.j += 1

        return self.list_of_list[self.i][self.j]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()