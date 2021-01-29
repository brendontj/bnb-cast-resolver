class Actor:
    def __init__(self, idx, value, groups):
        self._index = idx
        self._value = value
        self._groups = groups

    def get_index(self):
        return self._index

    def get_value(self):
        return self._value

    def get_groups(self):
        return self._groups
