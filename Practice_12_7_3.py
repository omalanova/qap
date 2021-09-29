per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита: "))
dohod = [round((i*money)/100) for i in list(per_cent.values())]
print(dohod)
print("Максимальная сумма, которую вы можете заработать - ", round(max(dohod)))
