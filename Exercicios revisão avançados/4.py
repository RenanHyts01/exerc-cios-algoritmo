quantidade_de_mouse = 100
n_esfera = 40
n_limpeza = 30
n_cabo_conector = 15
n_quebrado = 15

print(
    f"""
{"-"*50}
Digite a opção do problema encontrado!
1 - Necessita de esfera
2 - Necessita de limpeza
3 - Necessita troca do cabo ou conector
4 - Quebrado ou inutilizado
5 - Mostrar menu
0 - Finalizar
{"-"*50}
          """
)
while True:
    op = input("Digite a opção que corresponde ao mouse analisado: \n --->  ")
    match op:
        case "1":
            print("+1 mouse necessitando de esfera...")
            n_esfera += 1
            quantidade_de_mouse += 1
        case "2":
            print("+1 mouse necessitando de limpeza...")
            n_limpeza += 1
            quantidade_de_mouse += 1
        case "3":
            print("+1 mouse necessitando de troca de cabo ou conector...")
            n_cabo_conector += 1
            quantidade_de_mouse += 1
        case "4":
            print("+1 mouse quebrado ou inutilizado...")
            n_quebrado += 1
            quantidade_de_mouse += 1
        case "5":
            print(
                f"""
{"-"*50}
Digite a opção do problema encontrado!
1 - Necessita de esfera
2 - Necessita de limpeza
3 - Necessita troca do cabo ou conector
4 - Quebrado ou inutilizado
5 - Mostrar menu
0 - Finalizar
{"-"*50}
          """
            )
        case "0":
            n_quebrado_p = n_quebrado * 100 / quantidade_de_mouse
            n_esfera_p = n_esfera * 100 / quantidade_de_mouse
            n_limpeza_p = n_limpeza * 100 / quantidade_de_mouse
            n_cabo_conector_p = n_cabo_conector * 100 / quantidade_de_mouse

            print(
                f"""
Quantidade de mouses: {quantidade_de_mouse}

Situação                          Quantidade            Percentual
1- necessita da esfera                    {n_esfera}                   {round(n_esfera_p)}%
2- necessita de limpeza                   {n_limpeza}                   {round(n_limpeza_p)}%
3- necessita troca do cabo ou conector    {n_cabo_conector}                   {round(n_cabo_conector_p)}%
4- quebrado ou inutilizado                {n_cabo_conector}                   {round(n_quebrado_p)}%
                  """
            )
            break
        case _:
            print("Digite uma opção valida!")