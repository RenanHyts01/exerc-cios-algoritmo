numero_de_carros = 0
lista_de_carros = []
lista_numero_de_consumo = []


def Validar():
    try:
        consumo = float(input("Digite o consumo do carro: "))
        return consumo
    except ValueError:
        print("Digite um valor válido.")


while numero_de_carros < 5:
    numero_de_carros += 1
    lista_de_carros.append(input("Digite o nome do carro: "))
    lista_numero_de_consumo.append(Validar())

print("Relatório Final")
for c in range(1, 6):
    consumo = 1000 / lista_numero_de_consumo[c - 1]
    consumo_redondo = round(consumo, 1)
    print(
        f"""
    {c} - {lista_de_carros[c - 1]:<15} - {lista_numero_de_consumo[c - 1]:>15} - {consumo_redondo:>13} Litros - R$ {1000 / lista_numero_de_consumo[c - 1] * 2.25:>13.2f}
"""
    )