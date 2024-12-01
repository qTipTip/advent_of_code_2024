from pathlib import Path
import functools


def read_input(file: Path) -> tuple[list[int], list[int]]:
    l_list = []
    r_list = []

    with file.open("r") as infile:
        lines = infile.readlines()
        for line in lines:
            l, r = map(int, line.split())

            l_list.append(l)
            r_list.append(r)

    return l_list, r_list


input_file = Path(__file__).parent / "input.txt"
l_list, r_list = read_input(input_file)


def solve_1(l_list: list[int], r_list: list[int]):
    return sum(map(lambda x: abs(x[0] - x[1]), zip(sorted(l_list), sorted(r_list))))


print(solve_1(l_list, r_list))


@functools.lru_cache
def count_occurrences(x: int, list_of_numbers: tuple[int]) -> int:
    return sum(x == y for y in list_of_numbers)


def solve_2(l_list: list[int], r_list: list[int]) -> int:
    return sum(map(lambda x: x * count_occurrences(x, tuple(r_list)), l_list))


print(solve_2(l_list, r_list))
