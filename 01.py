from sys import stdin


def main():
    while True:
        contador = 0
        tamanho_segmento = 0
        
        tamanho_sequencia = (stdin.readline().strip())
        if tamanho_sequencia == None or tamanho_sequencia == "":
            break
        elif tamanho_sequencia == "%":
            print('%')
            continue

        n = int(tamanho_sequencia)
        dados_entrada = stdin.readline().split()
        sequencia = []

        for i in range(0, len(dados_entrada)):
            sequencia.append(int(dados_entrada[i]))

        for i in range(1, n):
            contador = contador + i
            if contador == n:
                tamanho_segmento = i
                break
            elif contador > n:
                tamanho_segmento = "NAO"
                break
        if tamanho_segmento == "NAO":
            print(tamanho_segmento)
            continue

        paridade = sequencia[0] % 2
        sequencia = sequencia[1:]

        for i in range(2, tamanho_segmento + 1):
            oposto = 0
            if paridade == 0:
                oposto = 1

            for j in sequencia[0:i]:
                if j % 2 == paridade:
                    tamanho_segmento = "NAO"
                    break

            sequencia = sequencia[i:]
            paridade = oposto

        print(tamanho_segmento)


if __name__ == "__main__":
    main()
