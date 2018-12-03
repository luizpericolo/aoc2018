from itertools import cycle

def puzzle():
    acc = 0
    frequencies = set([acc])

    input_file = open('../assets/input.txt', 'r')
    lines = [line.strip() for line in input_file.readlines()]
    lines = filter(lambda line: line, lines)

    for line in cycle(lines):
        # import pudb; pudb.set_trace()
        if line.strip():
            frequency = int(line.strip())
            acc += frequency
            if acc in frequencies:
                return acc
            else:
                frequencies.add(acc)

if __name__ == "__main__":
    output = puzzle()
    print(output)