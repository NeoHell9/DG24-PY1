# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, divider=","):
    participants1 = set(str1.split(divider))
    participants2 = set(str2.split(divider))

    common = participants1.intersection(participants2)

    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
divider = "|"
answer = find_common_participants(participants_first_group, participants_second_group, divider)
print(answer)