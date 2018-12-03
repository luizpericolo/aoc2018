def puzzle():
    acc = 0

    with open('../assets/input.txt', 'r') as f:
        for line in f:
            if line.strip():
                acc += int(line.strip())

    return acc


if __name__ == "__main__":
    output = puzzle()
    print(output)