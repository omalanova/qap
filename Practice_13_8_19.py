def tickets():
    k = int(input("Введите количество приобретаемых билетов: "))
    spisok = []
    for i in range(1, k + 1):
        age = int(input(f"Введите возраст {i} -го посетителя: "))
        if 18 <= age <= 24: 
            spisok.append(990)
        elif age >= 25:
            spisok.append(1390)
        else:
            spisok.append(0)
    if len(spisok) >= 4:
        return int(sum(spisok) * 0.9)
    return sum(spisok)

print(f"К оплате {tickets()} руб.")
