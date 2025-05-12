import sys

import collections

# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def solve(data):
    """Задаём направление движения"""
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = len(data), len(data[0])

    'Найдём старт и все ключи'
    starts = []
    total_keys = set()

    for i in range(n):
        for j in range(m):
            cell = data[i][j]
            if cell == '@':
                starts.append((i, j))
            elif 'a' <= ch <= 'z':
                total_keys.add(cell)


def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()
