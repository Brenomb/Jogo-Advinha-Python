from random import randint;

print(
    "Bem vindo ao jogo de adivinhação de números!\n"
    "O jogo consiste em adivinhar um número entre 1 e 100\n"
    "Você terá 10 tentativas para acertar o número\n"
    "Você pode escolher entre Advinhar ou Escolher o Número\n"
    "Advinhar: O computador escolhe um número e você tenta adivinhar\n"
    "Escolher o Número: Você escolhe um número e o computador tenta adivinhar\n")

while True:
    modoDeJogo = int(input("Selecione o modo de jogo: \n1 - Advinhar || 2 - Escolher \n"))
    if modoDeJogo == 1 or modoDeJogo == 2:
        dificuldadeJogo = int(input("Selecione a dificuldade: \n 1 - Fácil (com dicas) || 2 - Difícil (sem dicas)\n"))
        if dificuldadeJogo == 1 or dificuldadeJogo == 2:
            break


cTentativas = 0
match dificuldadeJogo:
    case 1: # Dificuldade Facil (com dicas)
        match modoDeJogo:
            case 1: # Modo de jogo onde o player advinha na dificuldade fácil
                numeroPC = randint(0,100)
                numeroJogador = int(input("Tente advinhar o número  "))

                while numeroJogador != numeroPC:
                    if numeroJogador > numeroPC:
                        cTentativas += 1
                        print(f"Você ainda tem {10-cTentativas} tentativas")
                        numeroJogador = int(input("chuta mais baixo "))
                    else:
                        cTentativas += 1
                        print(f"Você ainda tem {10-cTentativas} tentativas")
                        numeroJogador = int(input("chuta mais alto "))

                    if cTentativas == 9:
                        print("Suas tentativas acabaram :( ")
                        break
                if numeroJogador == numeroPC:
                    print(f"Parabéns! Você acertou com {cTentativas + 1} tentativas ")
            
            case 2: # Modo de jogo Fácil onde o player da instruções à maquina e ela quem tem que advinhar o número
                inicio = 0
                fim = 100
                numeroPC = randint(inicio,fim)
                cTentativas = 0
                input("Vamos lá! Pense em um número e quando quiser começar pressione qualquer tecla")
                
                while True:
                    print(f"O número que você pensou é {numeroPC}? ")
                    chute = input("Para responder diga S ou N ").upper
                    if chute == "S":
                        print(f"UHUUUUUL! Consegui na {cTentativas} ")
                        break
                    elif chute == "N":
                        print("O número é maior ou menor? ")
                        pergunta = input("Para responder escreva 'maior' ou 'menor' ").lower
                        if pergunta == "maior":
                            inicio = numeroPC
                        elif pergunta == "menor":
                            fim = numeroPC
                                
                    numeroPC == randint(inicio,fim)