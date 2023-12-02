def main():
    # input_text = open('input/day02_test.txt').read()
    input_text = open('./input/day02.txt', 'r').read()
    print(f'Part One: {part_one(input_text)}')
    print(f'Part Two: {part_two(input_text)}')


def part_one(input_text):
    total = 0
    colours_max = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    lines = input_text.splitlines()

    for line in lines:
        game, handfuls = line.split(': ')
        game_no = int(game.removeprefix('Game '))
        possible = True

        for handful in handfuls.split('; '):
            for cubes in handful.split(', '):
                number, colour = cubes.split(' ')
                if int(number) > colours_max[colour]:
                    possible = False
                    break

        if possible:
            total = total + game_no

    return total


def part_two(input_text):
    total = 0
    lines = input_text.splitlines()

    for line in lines:
        game, handfuls = line.split(': ')
        min_colours = {}

        for handful in handfuls.split('; '):
            for cubes in handful.split(', '):
                number, colour = cubes.split(' ')

                if colour in min_colours:
                    min_colours[colour] = max(min_colours[colour], int(number))
                else:
                    min_colours[colour] = int(number)

        total = total + (min_colours['red'] * min_colours['green'] * min_colours['blue'])

    return total


if __name__ == '__main__':
    raise SystemExit(main())
