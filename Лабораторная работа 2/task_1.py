money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

diff = spend - salary
money_capital -= diff # 1 месяц
months = 1

while money_capital > 0:
    spend *= 1+increase
    diff = spend - salary
    money_capital -= diff
    if money_capital < 0:
        break
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
