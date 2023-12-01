import re


def main():
    input_text_test = open('input/day01_pt2_test.txt').read()
    input_text = open('./input/day01.txt', 'r').read()
    print(f'Part One: {part_one(input_text)}')
    print(f'Part Two: {part_two(input_text)}')


def part_one(input_text):
    total = 0

    try:
        for _, row in enumerate(input_text.split('\n')):
            numbers = re.findall('\d', row)

            if len(numbers) == 0:
                numbers.append(0)

            total = total + int(numbers[0] + numbers[-1])

    finally:
        return total


def part_two(input_text):
    total = 0

    words = (
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    )

    try:
        for _, row in enumerate(input_text.split('\n')):

            for i, word in enumerate(words):
                row = row.replace(word, word[0] + str(i + 1) + word[-1])

            numbers = re.findall('\d', row)
            if len(numbers) == 0:
                numbers.append(0)

            total = total + int(numbers[0] + numbers[-1])

    finally:
        return total


if __name__ == '__main__':
    raise SystemExit(main())
