ws=0
un=0
linux=0
netware=0
mac=0
outro=0
print ("""
           
           "Qual o melhor Sistema Operacional para uso em servidores?"

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
""")

while True:

  
    option =(input("Digite o número da sua opção: "))
    print (f"Você selecionou {option}")
    match option:
        case '1':
            ws += 1
        case '2':
            un += 1
        case '3':
            linux +=1
        case '4':
            netware +=1
        case '5':
            mac +=1
        case '6':
            outro +=1
        case '0':
            if total ==0:
                print ("Digite um número válido")
            else:
                print ("Programa Finalizado")
                break
        
        case _:
            print ("Invalid")
    total = ws + un + linux + netware + mac + outro

print (f"""
       
Sistema Operacional     Votos     %
       
------------------      -----     ----
Windows Server           {ws}     {round(ws*100/total)}%
Unix                     {un}     {round(un*100/total)}%
Linux                    {linux}     {round(linux*100/total)}%
Netware                  {netware}      {round(netware*100/total)}%
Mac OS                   {mac}      {round(mac*100/total)}%
Outro                    {outro}      {round(outro*100/total)}%
       
-------------------     -----      ----
Total                    {total}
       """
       )
            


            




    
