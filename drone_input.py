def read_GATE(file):
    """ read data from file and populate gate vertex dictionary """
    gate = dict()
    i = 1
    try:
        with open(file) as input_file:
            for line in input_file:
                x, y, z = line.rstrip().split(" ")
                gate[i] = [float(x), float(y), float(z)]
                i += 1
        return gate
    except OSError as problem:
        print(f"There was a problem: {problem}")