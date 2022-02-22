import numpy as np


def local_binary_pattern(dataset):
    vetlbp = np.zeros([1, 256], dtype=int)
    matriz_pesos = np.array([1, 2, 4, 128, 0, 8, 64, 32, 16]).reshape([3, 3])

    for linha in range(1, dataset.shape[0] - 1):
        for coluna in range(1, dataset.shape[-1] - 1):
            linicio = linha - 1
            lfim = linha + 1
            cinicio = coluna - 1
            cfim = coluna + 1

            vizinhos_3x3 = dataset[linicio:lfim + 1, cinicio:cfim + 1]
            vizinhos_3x3_processada = np.zeros([3, 3])

            for i in range(0, 3):
                for j in range(0, 3):
                    if (vizinhos_3x3[i, j] >= vizinhos_3x3[1, 1]):
                        vizinhos_3x3_processada[i, j] = 1

            vallbp = round(sum(sum(vizinhos_3x3_processada * matriz_pesos)))
            vetlbp[0, vallbp] += 1

    return vetlbp

def histograma(dataset):
    histo = np.zeros([1, 256], dtype=int)
    for linha in range(dataset.shape[0]):
        for coluna in range(dataset.shape[-1]):
            histo[0, dataset[linha, coluna]] += 1
    return histo