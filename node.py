# from actor import Actor


class Node:
    # actors is a list of Actor
    def __init__(self, actors):
        self._actors = actors
        self._groups = list()
        self._current_value = 0

        self.update_groups()
        self.update_current_value()

    def get_actors(self):
        return self._actors

    def get_groups(self):
        return self._groups

    def get_current_value(self):
        return self._current_value

    def update_groups(self):
        for actor in self.get_actors():
            groups_of_actor = actor.get_groups()
            for ga in groups_of_actor:
                if ga not in self._groups:
                    self._groups.append(ga)

    def update_current_value(self):
        for actor in self.get_actors():
            self._current_value += actor.get_value()

    def print(self):
        for a in self.get_actors():
            print(a.get_index(), end='-')
