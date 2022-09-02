def count_people():
    group = int(input("Введите количество групп: "))
    total = 0
    for man in range(group):
        people = int(input(f"Количество человек в {man + 1} группе: "))
        days = int(input(f"Количество занятий с {man + 1} группой: "))
        total += people * days
    return total


def count_mk():
    amount_mk = int(input("Количество проведенных МК: "))
    cost_mk = 15
    return amount_mk * cost_mk


def work_out():
    count_work_out = int(input("Введите количество отработок: "))
    cost_work_out = 14.4
    return count_work_out * cost_work_out


def calculate():
    price = float(input("Стоимость за человека: "))
    without_tax = 0.86
    total = round(((count_people() * price) + work_out() + count_mk()), 2)
    total_without_tax = round((total * without_tax), 2)
    return total, total_without_tax

def print_result():
    total, total_without_tax = calculate()
    print(f'Итого грязными {total} бел.руб.\nЧистыми {total_without_tax} бел.руб')



print_result()