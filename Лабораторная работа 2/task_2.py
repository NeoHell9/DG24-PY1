salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = spend - salary

for i in range (1, months):
    spend *= 1+increase
    diff = spend - salary
    money_capital += diff

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
