def main():
    input_text = open('input/day05_test.txt').read()
    # input_text = open('./input/day05.txt', 'r').read()
    print(f'Part One: {part_one(input_text)}')
    print(f'Part Two: {part_two(input_text)}')


def part_one(input_text):
    seed_map = {}
    seeds = input_text.split('\n\n')[0].replace('seeds: ', '').split(' ')
    seeds = [eval(s) for s in seeds]

    for seed in seeds:
        print(seed)
        number = seed
        q = number

        maps = input_text.split('\n\n')[1:]
        print(maps)
        for x in maps:
            map = x.split('\n')[1:]
            print('map ', map)
            for row in map:
                print(f'row {row}')
                test = row.split(' ')
                d, s, i = [eval(x) for x in test]
                print(f'd {d}, s {s}, i {i}, number {number}, q {q}')
                if s <= number and number < (s + i):
                    print('got a thing')
                    q = number - s + d
                else:
                    print('not got a thing')
                    continue

                print(f'{x.split(":")[0]}: {q}')
            number = q
        seed_map[seed] = q

    return min(seed_map.values())


def part_two(input_text):

    return


if __name__ == '__main__':
    raise SystemExit(main())
