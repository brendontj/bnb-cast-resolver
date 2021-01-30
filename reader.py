import fileinput


class Reader:
    """Class responsible to read input of problem from stdin"""
    def __init__(self):
        self._actors = []
        self._groups = set()
        self._number_characters = 0

    def get_actors(self):
        return self._actors

    def get_groups(self):
        return self._groups

    def get_number_characters(self):
        return self._number_characters

    def process_line(self, line):
        line.split()


    def exec(self):
        input_lines = []
        for line in fileinput.input():
            input_lines.append(line.rstrip())

        self.process_first_line()
        print(input_lines)
