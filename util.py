def read_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    A = [int(x) for x in lines[1].replace('\n', '').split(' ')]
    B = [int(x) for x in lines[2].replace('\n', '').split(' ')]
    C = [int(x) for x in lines[3].replace('\n', '').split(' ')]
    return int(lines[0]), A, B, C
