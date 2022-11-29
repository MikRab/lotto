"""portal w którym logujesz się, sprawdza czy jestes pełnoletni 
i gra z Tobą w gre, kazdy gracz wpłaca 1 zł, gdy zbierze się
10 graczy, gra sie rozpoczyna, kto wygra zgarnia pule, jesli nikt
nie wygra, kolejna runda."""



import random


def draw_number(amount, total_amount):
    list_of_numbers = []
    for x in range(amount):
        number = random.randint(0, total_amount)
        if number is not list_of_numbers:
            list_of_numbers.append(number)
        elif number in list_of_numbers:
            continue
    return(list_of_numbers)


print(draw_number(6, 49))
