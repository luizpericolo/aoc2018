from itertools import cycle

def puzzle():
    acc = 0
    frequencies = set([acc])

    for line in cycle(open('../assets/input.txt', 'r')):
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