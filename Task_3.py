from pathlib import Path
from collections import Counter
import sys


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        raise ValueError("Invalid data format")
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]}


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                line_clean = line.strip()
                if line_clean:
                    logs.append(parse_log_line(line_clean))
        return logs
    except FileNotFoundError:
        print("File not found")
        return []


def filter_logs_by_level(logs: list, level: str) -> list:
    level_upper = level.upper()
    return [log for log in logs if log.get("level", "").upper() == level_upper]


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log.get("level", "").upper()
        if level:
            counts[level] = counts.get(level, 0) + 1
    return counts
    # return dict(Counter(log.get('level', '').upper() for log in logs if 'level' in log))


def display_log_counts(counts: dict):
    header_level = "Рівень логування"
    header_count = "Кількість"

    print(f"{header_level:<17} | {header_count}")
    print("-" * 18 + "|" + "-" * 10)
    for level, count in counts.items():
        print(f"{level:<17} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Будь ласка вкажіть шлях до файлу логів")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level_param = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level_param)
        print(f" \n Деталі логів для рівня'{level_param.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
