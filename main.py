from problem import Problem
from actor import Actor

def main():
    # fake_groups, fake_actors, fake_number_characters = process_input()

    #fake_groups = [1,2,3,...] list of int
    #fake_actors = [Actor(1), Actor(2), Actor(3)] list of actor
    #fake_number_characters = 2 // int
    fake_groups = set([1, 2, 3, 4, 5, 6])
    fake_actors = [Actor(1, 3, [1, 2,5,6]), Actor(2, 4, [1, 2,5,6]), Actor(3, 100, [1,2,6]), Actor(4, 999, [1,2,4]), Actor(5, 888,[3,5,6])]
    fake_number_characters = 2
    # fake_groups = set([1, 2])
    # fake_actors = [Actor(1, 5, [1]), Actor(2, 10,[2])]

    problem = Problem(fake_groups, fake_actors, fake_number_characters)
    node = problem.resolve()
    node.print()
    print("Visited nodes = " + str(problem.visited_nodes))


if __name__ == '__main__':
    main()
