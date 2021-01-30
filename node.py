# from actor import Actor


class Node:
    def __init__(self, actors):
        self._actors = actors
        self._groups = set()
        self._current_value = 0
        self._chields_to_be_visited = set()
        self.isClosedNode = False

        self.update_groups()
        self.update_current_value()

    def get_actors(self):
        return self._actors

    def get_groups(self):
        return self._groups

    def get_current_value(self):
        return self._current_value

    def update_groups(self):
        for actor in self._actors:
            groups_of_actor = actor.get_groups()
            for ga in groups_of_actor:
                self._groups.add(ga)

    def have_more_chields(self):
        if len(self._chields_to_be_visited):
            return True
        return False

    def level(self):
        return len(self._actors)

    def update_current_value(self):
        for actor in self._actors:
            self._current_value += actor.get_value()
