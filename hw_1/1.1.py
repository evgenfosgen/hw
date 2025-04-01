import sys


def nl_lite(filename=None):
    if filename:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()

    for i, line in enumerate(lines, start=1):
        print(f"{i}\t{line}", end='',)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        nl_lite(sys.argv[1])
    else:
        nl_lite()

# python3 1.1.py test.txt
