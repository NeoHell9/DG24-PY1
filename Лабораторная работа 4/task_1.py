# TODO решите задачу
import json

def task(filename="input.json") -> float:
    with open(filename, "r") as file:
        data = json.load(file)

    total_sum = sum(item["score"] * item["weight"] for item in data)

    return round(total_sum, 3)

print(task("input.json"))
