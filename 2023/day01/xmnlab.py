with open("input", "r") as f:
    content = f.readlines()


def part1(content):
    numbers = []
    for line in content:
        first_number = ""
        last_number = ""
        number = ""
        for c in line:
            if not c.isnumeric():
                continue
            if not first_number:
                first_number = c
            else:
                last_number = c

        if first_number:
            number = first_number
        if last_number:
            number += last_number
        else:
            number += number
        if number:
            numbers.append(int(number))


    print(sum(numbers))


def part2(content):
    numbers_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    numbers = []
    for line in content:
        first_number = ""
        last_number = ""
        number = ""
        number_text = ""
        for c in line:
            if not c.isnumeric():
                number_text += c

                found_number = ""
                for number_name in numbers_map.keys():
                    if number_name in number_text:
                        found_number = number_name
                        break
                if not found_number:
                    continue

                c = numbers_map[found_number]
            number_text = ""
            if not first_number:
                first_number = c
            else:
                last_number = c

        if first_number:
            number = first_number
        if last_number:
            number += last_number
        else:
            number += number
        if number:
            numbers.append(int(number))

    result = sum(numbers)
    print(result)
    return result

# part1(content)

test_data_part2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

assert part2(test_data_part2) == 281
part2(content)
