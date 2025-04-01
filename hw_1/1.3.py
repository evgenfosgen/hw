import sys


def count_stats(text):
    lines = text.count("\n")
    words = len(text.split())
    bytes_count = len(text.encode('utf-8'))
    return lines, words, bytes_count


def wc_lite(filenames):
    total_lines, total_words, total_bytes = 0, 0, 0

    if filenames:
        for filename in filenames:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    text = file.read()
                lines, words, bytes_count = count_stats(text)
                print(f"{lines:8}{words:8}{bytes_count:8} {filename}")

                total_lines += lines
                total_words += words
                total_bytes += bytes_count

            except FileNotFoundError:
                print(f"ошибка, файл '{filename}' не найден.", file=sys.stderr)

        if len(filenames) > 1:
            print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")

    else:
        text = sys.stdin.read()
        lines, words, bytes_count = count_stats(text)
        print(f"{lines:8}{words:8}{bytes_count:8}")


if __name__ == "__main__":
    wc_lite(sys.argv[1:])

# python3 1.3.py test1.2.txt test1.2.2.txt
