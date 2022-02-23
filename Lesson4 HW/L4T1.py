from sys import argv

pyname, sname, wtime, hcost, bonus = argv

print("Скрипт: ", pyname)
print("Сотрудник: ", sname)
print("Проработал часов: ", wtime)
print("По ставке в час: ", hcost)
print("За рвение + премия: ", bonus)
income = int(wtime)*int(hcost) + int(bonus)
print(f'В этом месяце сотрудник {sname} получит {income} рублей')