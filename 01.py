from sys import stdin


def main():
    while True:
        count = 0
        M = 0

        sequence_size = (stdin.readline().strip())
        if sequence_size == None or sequence_size == "":
            break
        elif sequence_size == "%":
            print('%')
            continue

        N = int(sequence_size)
        input_sequence = stdin.readline().split()
        sequence = []

        for i in range(0, len(input_sequence)):
            sequence.append(int(input_sequence[i]))

        for i in range(1, N):
            count = count + i
            if count == N:
                M = i
                break
            elif count > N:
                M = "NAO"
                break
        if M == "NAO":
            print(M)
            continue

        parity = sequence[0] % 2
        sequence = sequence[1:]

        for i in range(2, M + 1):
            opposite = 0
            if parity == 0:
                opposite = 1

            for j in sequence[0:i]:
                if j % 2 == parity:
                    M = "NAO"
                    break

            sequence = sequence[i:]
            parity = opposite

        print(M)
        print('%')   


if __name__ == "__main__":
    main()
