################ Solução que não leva em conta o valor final do intervalo na soma de pares ################
interval = []
sum_pairs = 0
count_value = 1
pair_found = False
for i in range(2):
    while True:
        try:
            value = int(input(f"Digite o {count_value}º valor para somar os pares do intervalo: "))
            interval.append(value)
            count_value+=1
            break
        except ValueError:
            print("Deve ser inteiro!")
interval.sort()
for i in range(interval[0], interval[1]):
    if i%2 == 0:
        sum_pairs+=i
        pair_found = True
else:
    if not pair_found:
        print(f"Não há pares no intervalo {tuple(interval)}")
    else:
        print(f"Soma dos valores pares foi: {sum_pairs}")

################ Solução que leva em conta o valor final do intervalo na soma de pares ################
interval = []
sum_pairs = 0
count_value = 1
pair_found = False
for i in range(2):
    while True:
        try:
            value = int(input(f"Digite o {count_value}º valor para somar os pares do intervalo: "))
            interval.append(value)
            count_value+=1
            break
        except ValueError:
            print("Deve ser inteiro!")
interval.sort()
for i in range(interval[0], interval[1]+1):
    if i%2 == 0:
        sum_pairs+=i
        pair_found = True
else:
    if not pair_found:
        print(f"Não há pares no intervalo {tuple(interval)}")
    else:
        print(f"Soma dos valores pares foi: {sum_pairs}")