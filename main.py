import random
from pygame import*
import sys

init()

vida = 6
lista_palavras = ["arroz", "banana", "queijo", "alface", "frango"]

palavra_escolhida = random.choice(lista_palavras)
letras_acertadas = ["_"] * len(palavra_escolhida)

while vida >=0 and "_" in  letras_acertadas:
    letra = input("Qual palavra voce quer?")
    if letra == palavra_escolhida:
        print("Acertou!")
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
             letras_acertadas[i] = letra
        print(letras_acertadas)
    else:
       print("Errou!")
       vida = vida-1
       print(f"sobram {vida} vidas")

    if "_" not in letras_acertadas:
        print(f"\nParabens! a palavra era {palavra_escolhida}")
   
    else:
        print(f"\nGame Over! A palavra era {palavra_escolhida}")       
   
  






background_color = (245, 178, 64)
 
window = display.set_mode((1280, 720))

window.fill(background_color)