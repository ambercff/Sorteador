import random

vida = 200

num_sorteado = random.randint(0,100)

num_par = num_sorteado % 2

print(num_sorteado)

if num_par != 0:
    num_sorteado = random.randint(0,100)
    
else:
    for i in range(4,0,-1):
        num_usuario = int(input("digite um número de 0 a 100: "))

        if num_sorteado == num_usuario:
            print(f"Parabéns! Você ganhou.")
            break
        else:
            dano = abs((num_sorteado - num_usuario))

            if dano >= vida or i<= 1:
                print(f"Você perdeu! o número era {num_sorteado}")
                break

            vida -= dano

            print(f"Você errou. Restam {vida} pontos de vida e {i - 1} tentativas")