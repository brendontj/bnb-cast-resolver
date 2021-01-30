from reader import Reader
from problem import Problem
from actor import Actor


def main():
    problem_input = Reader()
    problem_input.exec()
    problem = Problem(problem_input.get_groups(), problem_input.get_actors(), problem_input.get_number_characters())
    problem.resolve()
    problem.possible_solution.print()
    print("Visited nodes = " + str(problem.visited_nodes))


if __name__ == '__main__':
    main()
