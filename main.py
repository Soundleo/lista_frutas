# criar uma lista de frutas
frutas = []
import os
from datetime import date



print (f'{'='*50}lista de compras{'='*50}')

while True:
    # inserindo uma nova prouta 
    nova_fruta = input("informe o nome da nova fruta ou deixe vazio para encerrar  \n").capitalize()

    if nova_fruta != '':
        # inserindo o nome na lista
        frutas.append(nova_fruta)
        continue
    else: 
        break


# exibir na tela a lista
os.system('cls')
for fruta in frutas:
    print(fruta)
dia = date.today()
print(dia)