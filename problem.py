import queue


from node import Node


class Problem:
    def __init__(self, groups, actors, number_characters):
        self._groups = groups
        self._actors = actors
        self._number_characters = number_characters

        self._bound_function_value = 100000
        self._queue = self.initialize_queue()

    def get_groups(self):
        return self._groups

    def get_actors(self):
        return self._actors

    def get_number_characters(self):
        return self._number_characters

    def get_queue(self):
        return self._queue

    def get_actors_reverse_sorted_by_value(self):
        return sorted(self._actors, key=lambda x: x.get_value())

    def initialize_queue(self):
        q = queue.Queue()

        for actor in self.get_actors_reverse_sorted_by_value():
            actors = list()
            actors.append(actor)
            node = Node(actors)
            q.put(node)
        return q

    def resolve(self):
        candidate = None
        while not self._queue.empty():
            n = self._queue.get()

            if n.get_current_value() < self._bound_function_value and \
                    n.get_groups() == self._groups and len(n.get_actors()) == self.get_number_characters():

                self._bound_function_value = n.get_current_value()
                candidate = n
            else:
                for a in self.get_actors_reverse_sorted_by_value():
                    if a not in n.get_actors():
                        actors_of_new_node = n.get_actors().copy()
                        actors_of_new_node.append(a)
                        new_node = Node(actors_of_new_node)
                        self._queue.put(new_node)

        return candidate
