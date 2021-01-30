import fileinput


from actor import Actor


class Reader:
    """Class responsible to read input of problem from stdin"""
    def __init__(self):
        self._actors = []
        self._groups = set()

        self._number_characters = 0
        self._number_actors = 0
        self._number_groups = 0

    def get_actors(self):
        return self._actors

    def get_groups(self):
        return self._groups

    def get_number_characters(self):
        return self._number_characters

    @staticmethod
    def split_line(line):
        line = line.split()
        return line

    def define_variables(self, variables_list):
        self._number_groups = int(variables_list[0])
        self._number_actors = int(variables_list[1])
        self._number_characters = int(variables_list[2])

    def define_group(self):
        for i in range(self._number_groups):
            self._groups.add(i+1)

    def exec(self):
        input_lines = []
        for line in fileinput.input():
            input_lines.append(line.rstrip())
        try:
            first_line = input_lines[0]
            first_line = self.split_line(first_line)

            self.define_variables(first_line)
            self.define_group()

            current_line_idx = 1
            for i in range(self._number_actors):
                current_line = input_lines[current_line_idx]
                current_line = self.split_line(current_line)

                actor_cost = int(current_line[0])
                actor_number_groups = int(current_line[1])
                actor_groups = set()

                end_block_idx = current_line_idx+actor_number_groups+1
                for line_idx_group in range(current_line_idx+1, end_block_idx):
                    actor_groups.add(int(input_lines[line_idx_group]))

                self._actors.append(Actor(i+1, actor_cost, actor_groups))
                current_line_idx = end_block_idx

        except (ValueError, TypeError):
            print("Incorrect input format")

