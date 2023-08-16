import random
import time

vida = 200

num_sorteado = random.randint(0,11)

lista = [0,1,1,2,3,5,8,13,21,34,55,89]
num_lista = lista[num_sorteado]

count = 1

tempo_total = 60
    
for i in range(4,0,-1):
    print(f"restam {round(tempo_total, 2)} segundos")
    antes = time.time()
    num_usuario = int(input("digite um número de 0 a 100: "))
    tempo_total -= time.time() - antes

    if tempo_total <= 0:
        print("Seu tempo acabou")
        break

    if num_lista == num_usuario:
        print(f"Parabéns! Você ganhou.")
        break
    else:
        dano = abs((num_lista - num_usuario))

        if dano >= vida or i<= 1:
            print(f"Você perdeu! o número era {num_lista}")
            break

        vida -= dano

        print(f"Você errou. Restam {vida} pontos de vida e {i - 1} tentativas")
