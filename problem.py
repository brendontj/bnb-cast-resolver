import queue
import sys

from node import Node

INFINITE = sys.maxsize


class Problem:
    def __init__(self, groups, actors, number_characters):
        self._groups = groups
        self._actors = actors
        self._number_characters = number_characters

        self._max_cost = INFINITE
        self._queue = self.initialize_queue()
        self.visited_nodes = 0

        self._default_bound_function = True

    def get_groups(self):
        return self._groups

    def get_actors(self):
        return self._actors

    def max_level(self):
        return self._number_characters

    def get_queue(self):
        return self._queue

    def increases_visited_nodes(self):
        self.visited_nodes += 1

    def get_actors_sorted_by_value(self):
        return sorted(self._actors, key=lambda x: x.get_value())

    def initialize_queue(self):
        """Initialize a empty queue"""
        q = queue.Queue()
        return q

    def is_possible_solution(self, candidate_node):
        """Check if the candidate node is a possible solution"""
        if candidate_node.get_current_value() < self._max_cost and \
                candidate_node.get_groups() == self._groups and candidate_node.level() == self.max_level():
            return True
        return False

    def default_bound_function(self, node_candidate):
        """Check if the next node value with the future path can be a solution of the problem"""
        next_actor_to_visit = node_candidate.get_next_to_visit()  # Pick the next actor to visit
        actors_of_new_node = node_candidate.get_actors().copy()

        if node_candidate.get_current_value() + next_actor_to_visit.get_value() > self._max_cost:
            return

        actors_of_new_node.append(next_actor_to_visit)
        new_node_children_to_visit = node_candidate.get_children_to_visit().copy()
        new_node = Node(actors_of_new_node, new_node_children_to_visit)
        self._queue.put(new_node)

    def resolve(self):
        """Resolver of the problem: creates a tree of execution with the node queue of the Problem class"""
        possible_solution = None
        for i in range(0, len(self.get_actors_sorted_by_value())):
            node = Node([self.get_actors_sorted_by_value()[i]], self.get_actors_sorted_by_value()[i+1:])
            self._queue.put(node)  # Put initial node a child of root and has all actors with higher cost then him to visit

            while not self._queue.empty():
                candidate = self._queue.get()

                if not candidate.isVisited:
                    self.increases_visited_nodes()

                if self.is_possible_solution(candidate) and not candidate.isVisited:
                    self._max_cost = candidate.get_current_value()
                    possible_solution = candidate
                else:
                    if candidate.have_more_child():
                        if self._default_bound_function:
                            self.default_bound_function(candidate)

                        if candidate.have_more_child():
                            self._queue.put(candidate)  # Enqueue visited candidate to generate new node with other child
                    else:
                        candidate.close_node()
                candidate.visit()
        return possible_solution
