class Node:
    def __init__(self, actors, children_to_visit):
        self._actors = actors
        self._children_to_visit = children_to_visit

        self._groups = set()
        self._current_value = 0

        self.update_groups()
        self.update_current_value()

        self.isClosedNode = not self.have_more_child()
        self.isVisited = False

    def get_actors(self):
        return self._actors

    def get_children_to_visit(self):
        return self._children_to_visit

    def get_groups(self):
        return self._groups

    def get_current_value(self):
        return self._current_value

    def update_groups(self):
        for actor in self._actors:
            groups_of_actor = actor.get_groups()
            for ga in groups_of_actor:
                self._groups.add(ga)

    def have_more_child(self):
        if len(self._children_to_visit):
            return True
        return False

    def level(self):
        return len(self._actors)

    def update_current_value(self):
        for actor in self._actors:
            self._current_value += actor.get_value()

    def get_next_to_visit(self):
        if self.have_more_child():
            return self._children_to_visit.pop(0)

    def close_node(self):
        self.isClosedNode = True

    # def remove_child(self, actor):
    #     self._children_to_visit.remove(actor)

    def visit(self):
        self.isVisited = True

    def print(self):
        actors_sorted = sorted(self._actors, key=lambda x: x.get_index())
        for a in actors_sorted:
            print(a.get_index(), end=" ")
        print()
        print(self.get_current_value())

