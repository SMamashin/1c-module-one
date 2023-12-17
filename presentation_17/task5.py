class CountLen:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

data = CountLen(['name', 'info', 'age', 'city', 'auto'])

print(f'Количество элементов: {len(data)}')
