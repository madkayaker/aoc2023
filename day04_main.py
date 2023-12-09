def main():
    input_text = open('input/day04_test.txt').read()
    input_text = open('./input/day04.txt', 'r').read()
    print(f'Part One: {part_one(input_text)}')
    print(f'Part Two: {part_two(input_text)}')


def part_one(input_text):
    total = 0
    lines = input_text.splitlines()

    for i, line in enumerate(lines):
        points = 0
        win_nums, have_nums = line[line.find(': '):].split(' | ')
        win_nums = win_nums.split(' ')
        have_nums = have_nums.split(' ')

        for w in win_nums:
            if w == '':
                continue
            if w in have_nums:
                points = 1 if points == 0 else points * 2

        total = total + points

    return total


def part_two(input_text):
    total = 0
    cards = input_text.splitlines()
    count = {}

    for card_id, card in enumerate(cards, start=1):
        if card_id not in count:
            count[card_id] = 1
        else:
            count[card_id] = count[card_id] + 1

        wins = 0
        win_nums, have_nums = card[card.find(': '):].split(' | ')
        win_nums = win_nums.split(' ')
        have_nums = have_nums.split(' ')

        for _ in range(count[card_id]):
            for w in win_nums:
                if w == '':
                    continue
                if w in have_nums:
                    wins = wins + 1

            for i in range(1, wins + 1):
                if card_id + i not in count:
                    count[card_id + i] = 1
                else:
                    count[card_id + i] = count[card_id + i] + 1
                wins = wins - 1

    total = sum(count.values())

    return total


if __name__ == '__main__':
    raise SystemExit(main())
