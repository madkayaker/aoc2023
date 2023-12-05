import re


def main():
    input_text = open('input/day03_test.txt').read()
    # input_text = open('./input/day03.txt', 'r').read()
    print(f'Part One: {part_one(input_text)}')
    print(f'Part Two: {part_two(input_text)}')


def part_one(input_text):
    total = 0
    lines = input_text.splitlines()

    for i, line in enumerate(lines):
        numbers = re.compile(r'\d{1,}').finditer(line)
        for match in numbers:
            if i != 0:
                if match.start() == 0:
                    row_above = lines[i - 1][match.start():match.end() + 1]
                else:
                    row_above = lines[i - 1][match.start() - 1:match.end() + 1]
            else:
                row_above = ''

            if re.findall(r'[^\d|^.]', row_above):
                total = total + int(match.group(0))
                continue

            if i + 1 != len(lines):
                if match.start() == 0:
                    row_below = lines[i + 1][match.start():match.end() + 1]
                else:
                    row_below = lines[i + 1][match.start() - 1:match.end() + 1]
            else:
                row_below = ''

            if re.findall(r'[^\d|^.]', row_below):
                total = total + int(match.group(0))
                continue

            if match.start() == 0:
                left = ''
            else:
                left = line[match.start() - 1]

            if match.end() == len(line):
                right = ''
            else:
                right = line[match.end()]

            if re.findall(r'[^\d|^.]', left):
                total = total + int(match.group(0))
                continue

            if re.findall(r'[^\d|^.]', right):
                total = total + int(match.group(0))
                continue

    return total


def part_two(input_text):
    total = 0
    lines = input_text.splitlines()

    for i, line in enumerate(lines):
        print(line)

    return total


if __name__ == '__main__':
    raise SystemExit(main())
