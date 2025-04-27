import json
import sys
from datetime import datetime


def check_capacity(max_capacity: int, guests: list) -> bool:
    events = []

    for guest in guests:
        check_in = datetime.strptime(guest["check-in"], "%Y-%m-%d")
        check_out = datetime.strptime(guest["check-out"], "%Y-%m-%d")

        # +1 на дату заселения, -1 на дату выселения
        events.append((check_in, 1))
        events.append((check_out, -1))

    # Сортировка событий по дате, если даты совпадают - сначала -1, потом +1
    events.sort()

    current_guests = 0
    for date, change in events:
        current_guests += change
        if current_guests > max_capacity:
            return False
    return True


if __name__ == "__main__":
    # Чтение входных данных
    max_capacity = int(input())
    n = int(input())

    guests = []
    for _ in range(n):
        guest_json = sys.stdin.readline()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)

    result = check_capacity(max_capacity, guests)
    print(result)
