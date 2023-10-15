# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125

lista1 = ["alexandre", "anderson", "antonio", "carlos", "cesar", "rosemary"]
lista2 = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]

while True:
    print(
        f"""
1 - Ler arquivo: "usuarios.txt"
2 - Gerar arquivo: "relatorio.txt"
3 - Sair
        """
    )
    op = input("Digite a opção desejada: ")
    match op:
        case "1":
            print("Lendo arquivo...")
            print("-" * 50)
            for c in range(0, 6):
                print(f"{lista1[c]} {lista2[c]}")
            print("-" * 50)
        case "2":
            print("Gerando arquivo...")
            print("------------------------------------------------------------------------")
            print(
                f"""
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

                  """
            )
        case "3":
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")