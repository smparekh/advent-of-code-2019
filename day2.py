def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def run_opcode(inputs, pos):
    # read opcode
    if inputs[pos] == 1:
        inputs[inputs[pos+3]] = add(inputs[inputs[pos+1]], inputs[inputs[pos+2]])
    elif inputs[pos] == 2:
        inputs[inputs[pos+3]] = multiply(inputs[inputs[pos+1]], inputs[inputs[pos+2]])
    return inputs


def run(in_commands):
    pos = 0
    inputs = run_opcode(in_commands, pos)
    while pos + 4 < len(inputs) and pos + 4 != 99:
        pos = pos + 4
        inputs = run_opcode(inputs, pos)
    return inputs


def part2(initial_set):
    noun = 0
    verb = 0
    expected = 19690720
    result = run(initial_set.copy())
    # print(result)
    print('Dumb search proceeding...')
    while noun < 99:
        while verb < 99:
            if result[0] != expected:
                new_run = initial_set.copy()
                new_run[1] = noun
                new_run[2] = verb
                result = run(new_run)
                # print('---')
                # print(result)
                # print('---')
                verb += 1
            else:
                break
        noun += 1
        verb = 0
    print(result)


if __name__ == '__main__':
    with open('inputs_day2.txt', 'r') as commands_file:
        commands = [int(x.strip()) for x in commands_file.readline().split(',')]
        print('Inputs:')
        print(commands)
        print('Part 1 solution:')
        print(run(commands.copy()))
        print('Part 2 solution:')
        part2(commands)
