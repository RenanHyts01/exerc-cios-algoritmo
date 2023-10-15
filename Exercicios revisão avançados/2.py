def Validador():
    while True:
        try:
            valor = float(input("Digite o valor: "))
        except ValueError:
            print("Digite um valor valido")
        else:
            return valor


numero_de_funcionarios = 0

lista_de_salarios = []

while True:
    salario = Validador()
    if salario == 0:
        break
    lista_de_salarios.append(salario)
    numero_de_funcionarios += 1

pisos = 0

maior_abono = 0

valor_abono_total = 0

lista_de_salarios_abono = []

lista_de_abono = []

for c in lista_de_salarios:
    if (c * 1.2 - c) <= 100:
        pisos += 1
        valor_abono_total += 100
        lista_de_salarios_abono.append(100)
        lista_de_abono.append(100)
        if 100 > maior_abono:
            maior_abono = 100
    else:
        valor_abono_total += c * 1.2 - c
        lista_de_salarios_abono.append(c * 1.2)
        lista_de_abono.append(c * 1.2 - c)
        if c * 1.2 - c > maior_abono:
            maior_abono = c * 1.2 - c

print("Projeção de Gastos com Abono")
print("=======================================")

for c in range(1, len(lista_de_salarios) + 1):
    print(f"Salário:  {lista_de_salarios[c-1]:.2f}")
print("=======================================")
print("Salário               -    Abono")
for c in range(1, numero_de_funcionarios + 1):
    print(
        f"""
R$ {lista_de_salarios[c-1]:>15.2f}    -    R$ {lista_de_abono[c-1]:>9.2f}
"""
    )

print(
    f"""
Foram Processados {numero_de_funcionarios} colaboradores
Total gasto com abonos: R$  {valor_abono_total:.2f}
Valor mínimo pago a {pisos} colaboradores
Maior valor de abono pago: R$ {maior_abono:.2f}
"""
)