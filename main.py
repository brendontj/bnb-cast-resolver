from problem import Problem
from actor import Actor

def main():
    # fake_groups, fake_actors, fake_number_characters = process_input()

    #fake_groups = [1,2,3,...] list of int
    #fake_actors = [Actor(1), Actor(2), Actor(3)] list of actor
    #fake_number_characters = 2 // int
    fake_groups = [1, 2]
    fake_actors = [Actor(1, 10, [1, 2]), Actor(2, 20, [2]), Actor(3, 5, [1, 2])]
    fake_number_characters = 2

    problem = Problem(fake_groups, fake_actors, fake_number_characters)
    node = problem.resolve()
    node.print()


if __name__ == '__main__':
    main()
