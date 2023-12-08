#POSIÇÕES DO TABULEIRO
matriz = [0,1,2,
          3,4,5,
          6,7,8]
msg = ""

#TAMANHO DO TABULEIRO
slot = []

#CONTADOR DE JOGADAS
jogada = 0

#PRIMEIRA IMPRESSÃO DO TABULEIRO
print("",matriz[0],"|",matriz[1],"|",matriz[2],'\n---+---+---\n'
      ,matriz[3],"|",matriz[4],"|",matriz[5],'\n---+---+---\n'
      ,matriz[6],"|",matriz[7],"|",matriz[8],'\n')

#EXECUTAR JOGADA DO JOGADOR X
def Jogar():
    try:
        lugar = int(input("Onde você quer jogar ?:"))

        if lugar > 8 or lugar < 0:
            print ("Digite um número de 0 a 8")
            global jogada
            jogada -= 1
            return jogada
        else:
            if matriz[lugar] == "X" or matriz[lugar] == "O":
                print("Já jogaram aí, amigo")
                jogada -= 1
                return jogada
                
            else:
                matriz.pop(lugar)
                matriz.insert(lugar,"X")
                slot.append(1)
                print("",matriz[0],"|",matriz[1],"|",matriz[2],'\n---+---+---\n'
                        ,matriz[3],"|",matriz[4],"|",matriz[5],'\n---+---+---\n'
                        ,matriz[6],"|",matriz[7],"|",matriz[8],'\n')
            
    except ValueError:
        print("Digita certo")
        jogada -= 1
        return jogada
    
#EXECUTAR JOGADA DO JOGADOR O
def Jogar0():
    try:
        lugar = int(input("Onde você quer jogar ?:"))

        if lugar > 8 or lugar < 0:
            print ("Digite um número de 0 a 8")
            global jogada
            jogada -= 1
            return jogada
        else:
            if matriz[lugar] == "X" or matriz[lugar] == "O":
                print("Já jogaram aí, amigo")
                jogada -= 1
                return jogada
                
            else:
                matriz.pop(lugar)
                matriz.insert(lugar,"O")
                slot.append(1)
                print("",matriz[0],"|",matriz[1],"|",matriz[2],'\n---+---+---\n'
                        ,matriz[3],"|",matriz[4],"|",matriz[5],'\n---+---+---\n'
                        ,matriz[6],"|",matriz[7],"|",matriz[8],'\n')
            
    except ValueError:
        print("Digita certo")
        jogada -= 1
        return jogada

#VERIFICADOR DE RESULTADO
def VerificacaoDeJogo():
    #VERIFICAÇÃO EM LINHA
    if matriz[0] == matriz[1] == matriz[2]:
        if matriz[0] == "X":
            global msg
            msg = "Jogador X ganhou !"
            print(msg)
        elif matriz[0] == "O":
            msg = "Jogador O ganhou !"
            print(msg)
    if matriz[3] == matriz[4] == matriz[5]:
        if matriz[3] == "X":
            msg = "Jogador X ganhou !"
            print(msg)
        elif matriz[3] == "O":
            msg = "Jogador O ganhou !"
            print(msg)
    if matriz[6] == matriz[7] == matriz[8]:
        if matriz[6] == "X":
            msg = "Jogador X ganhou !"
            print(msg)
        elif matriz[6] == "O":
            msg = "Jogador O ganhou !"
            print(msg)
    
    #VERIFICAÇÃO EM COLUNA
    if matriz[0] == matriz[3] == matriz[6]:
        if matriz[0] == "X":
            msg = "Jogador X ganhou !"
            print(msg)
        elif matriz[0] == "O":
            msg = "Jogador O ganhou !"
            print(msg)
    if matriz[1] == matriz[4] == matriz[7]:
        if matriz[1] == "X":
            msg = "Jogador X ganhou !"
            print(msg)
        elif matriz[1] == "O":
            msg = "Jogador O ganhou !"
            print(msg)
    if matriz[2] == matriz[5] == matriz[8]:
        if matriz[2] == "X":
            msg = "Jogador X ganhou !"
            print(msg)
        elif matriz[2] == "O":
            msg = "Jogador O ganhou !"
            print(msg)
    
    #VERIFICAÇÃO EM DIAGONAL
    if matriz[0] == matriz[4] == matriz[8]:
        if matriz[0] == "X":
            msg = "Jogador X ganhou !"
            print(msg)
        elif matriz[0] == "O":
            msg = "Jogador O ganhou !"
            print(msg)
    if matriz[2] == matriz[4] == matriz[6]:
        if matriz[2] == "X":
            msg = "Jogador X ganhou !"
            print(msg)
        elif matriz[2] == "O":
            msg = "Jogador O ganhou !"
            print(msg)
    
    #VERIFICAR SE DEU VELHA
    if msg == "" and len(slot) >= 9:
        msg = "Deu velha !"
        print (msg)

#JOGO SENDO EXECUTADO
while jogada+1 <= 9:
    #print(jogada) <- Utilizado para verificar quantidade de jogadas

    if jogada%2 == 0:
        Jogar()
    else:
        Jogar0()
    
    jogada += 1

    VerificacaoDeJogo()
    if msg != "":
        break