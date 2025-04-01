import sys


def tail_lite(filename=None, num_lines=10):
    if filename:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"ошибка, файл '{filename}' не найден.", file=sys.stderr)
            return
    else:
        lines = sys.stdin.readlines()

    for line in lines[-num_lines:]:
        print(line, end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, filename in enumerate(sys.argv[1:], start=1):
            if len(sys.argv) > 2:
                print(f"=> {filename} <=")
            tail_lite(filename, num_lines=10)
            if i < len(sys.argv) - 1:
                print()
    else:
        tail_lite(num_lines=17)

# python3 1.2.py test1.2.txt test1.2.2.txt
