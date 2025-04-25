# Desafio: Adivinhe a Palavra Misteriosa
import random

# Lista de palavras possíveis
palavras = ["gato", "banana", "chocolate", "bolo", "casa"]
palavra_secreta = random.choice(palavras)

# Configurações iniciais do jogo
vida = 5
tentativas = 1

print("🎮 Olá! Seja bem-vindo ao jogo da palavra misteriosa!")
print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
print(f"Você tem {vida} vidas. Boa sorte!\n")

# Primeira tentativa
escolha = input(f"Tentativa {tentativas} - Qual é a palavra? ").lower()

# Loop do jogo
while vida > 0 and escolha != palavra_secreta:
    vida -= 1
    tentativas += 1
    print(f"❌ Errado! Você perdeu uma vida. Vidas restantes: {vida}\n")
    
    if vida > 0:
        escolha = input(f"Tentativa {tentativas} - Tente novamente: ").lower()

# Verifica se ganhou ou perdeu
if escolha == palavra_secreta:
    print(f"🎉 Parabéns! Você acertou. A palavra secreta era '{palavra_secreta}'.")
else:
    print(f"💀 Game Over! A palavra secreta era '{palavra_secreta}'.")

print("✅ Jogo encerrado.")