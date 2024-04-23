import random # Importa o módulo random para gerar números aleatórios

def main():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")
    numero_secreto = random.randint(1, 100) # Gera um número aleatório entre 1 e 100
    tentativas = 0 # Inicializa o contador de tentativas

    while True: # Loop principal do jogo
        try:
        palpite = int(input("Faça o seu palpite: ")) # Solicita um palpite ao jogador
        tentativas += 1 # Incrementa o contador de tentativas

        if palpite < 1 or palpite > 100: # Verifica se o palpite está dentro do intervalo válido
        print("Por favor, digite um número entre 1 e 100.")
        continue # Reinicia o loop para pedir um novo palpite

        if palpite == numero_secreto: # Verifica se o palpite é igual ao número secreto
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break # Encerra o jogo
        elif palpite < numero_secreto: # Se o palpite for menor que o número secreto
        print("Tente um número maior.")
        else: # Se o palpite for maior que o número secreto
        print("Tente um número menor.")

        except ValueError: # Captura erros se o jogador não digitar um número
        print("Por favor, digite um número válido.")

        if __name__ == "__main__":
        main() # Chama a função main() para iniciar o jogo quando o script for executado