from typing import Callable
import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    pattern = r"\d+\.\d+"
    for number in re.findall(pattern, text):
        yield float(number)


def sum_profit(text: str, func: Callable):
    total_sum = 0
    for i in func(text):
        total_sum += i
    return total_sum


profit = sum_profit(text, generator_numbers)
print(f"Загальний дохід працівника складає: {profit:.2f} доларів.")
