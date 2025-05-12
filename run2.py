import sys

from collections import deque

# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def solve(data):
    """Задаём направление движения"""
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Направления движения
    n, m = len(data), len(data[0])  # Размеры лабиринта

    'Найдём старт и все ключи'
    starts = []
    total_keys = set()

    for i in range(n):
        for j in range(m):
            cell = data[i][j]
            if cell == '@':
                starts.append((i, j))
            elif 'a' <= cell <= 'z':
                total_keys.add(cell)

    'Создаём очередь и visited где уже были'
    queue = deque()
    queue.append((starts, set(), 0))  # позиции роботов, ключи, шаги
    visited = set()

    while queue:
        positions, keys, steps = queue.popleft()

        state_id = (tuple(positions), tuple(sorted(keys)))
        if state_id in visited:
            continue
        visited.add(state_id)

        'Если собрали все ключи - завершаем'
        if len(keys) == len(total_keys):
            return steps

        'Движение каждого робота'
        for i in range(4):
            x, y = positions[i]
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < n and 0 <= ny < m):  # Проверка выхода за границы
                    continue

                cell = data[nx][ny]  # Чтение символа в новой клетке

                if cell == '#':
                    continue  # Стена

                if 'A' <= cell <= 'Z' and cell.lower() not in keys:
                    continue  # Нашли дверь, но нет ключа

                new_keys = keys.copy()  # Копируем ключи, если находим новый - добавляем
                if 'a' <= cell <= 'z':
                    new_keys.add(cell)

                new_positions = positions.copy()  # Обновляем позиции и снова движение
                new_positions[i] = (nx, ny)

                queue.append((new_positions, new_keys, steps + 1))  # Добавляем новое состояние в очередь

    return -1  # Если не удалось собрать все ключи


def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()
