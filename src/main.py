import sys
import time

from reader import Reader
from problem import Problem
from columnar import columnar


def report(solution_time, visited_nodes, total_cost, actors):
    path = ""
    for a in actors:
        path += str(a.get_index()) + '->'
    path = path[:-2]
    headers = ['Total time(s)', 'Visited node', 'Total cost', 'Solution path']

    data = [
        [str(f'{solution_time:.20f}'), str(visited_nodes), str(total_cost), path],
    ]

    table = columnar(data, headers, no_borders=False)
    print(table, file=sys.stderr)


def main(args):
    problem_input = Reader()
    problem_input.exec()

    problem = Problem(problem_input.get_groups(), problem_input.get_actors(), problem_input.get_number_characters())

    if "-a" in args:
        problem._default_bound_function = False

    start = time.time()
    problem.resolve()
    end = time.time()
    try:
        problem.possible_solution.print()
        report(
            end-start,
            problem.visited_nodes,
            problem.possible_solution.get_current_value(),
            problem.possible_solution.get_actors()
        )
    except AttributeError:
        print('Inviável')


if __name__ == '__main__':
    main(sys.argv[1:])
