import queue


from node import Node

INFINITE = 99999999


class Problem:
    def __init__(self, groups, actors, number_characters):
        self._groups = groups
        self._actors = actors
        self._number_characters = number_characters

        self._bound_value = INFINITE
        self._queue = self.initialize_queue()

    def get_groups(self):
        return self._groups

    def get_actors(self):
        return self._actors

    def max_level(self):
        return self._number_characters

    def get_queue(self):
        return self._queue

    def get_actors_sorted_by_value(self):
        return sorted(self._actors, key=lambda x: x.get_value())

    def initialize_queue(self):
        """Initialize a empty queue"""
        q = queue.Queue()
        return q

    def is_possible_solution(self, candidate_node):
        """Check if the candidate node is a possible solution"""
        if candidate_node.get_current_value() <= self._bound_value and \
                candidate_node.get_groups() == self._groups and candidate_node.level() == self.max_level():
            return True
        return False

    def resolve(self):
        """Resolver of the problem: creates a tree of execution with the node queue of the Problem class"""
        possible_solution = None
        for i in range(0, len(self.get_actors_sorted_by_value())):
            node = Node([self.get_actors_sorted_by_value()[i]], self.get_actors_sorted_by_value()[i+1:])
            self._queue.put(node)  # Put initial node a child of root and has all actors with higher cost then him to visit

            while not self._queue.empty():
                candidate = self._queue.get()

                if self.is_possible_solution(candidate) and not candidate.isVisited:
                    self._bound_value = candidate.get_current_value()
                    possible_solution = candidate
                else:
                    if candidate.have_more_childs():
                        next_actor_to_visit = candidate.get_next_to_be_visited()  # Pick the next actor to visit
                        candidate.remove_chield(next_actor_to_visit)  # Update actual node

                        actors_of_new_node = candidate.get_actors().copy()
                        actors_of_new_node.append(next_actor_to_visit)
                        new_node = Node(actors_of_new_node)

                        if candidate.have_more_childs():
                            self._queue(candidate)  # Enqueue visited candidate to generate new node with other child

                        self._queue(new_node)

                    else:
                        candidate.close_node()

                candidate.visit()

        return possible_solution
