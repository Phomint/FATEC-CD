def normaliza(dataset):
    img_normalizada = dataset
    for linha in range(dataset.shape[0]):
        for coluna in range(dataset.shape[-1]):
            img_normalizada[linha, coluna] = (dataset[linha, coluna] - dataset.min()) / (dataset.max() - dataset.min())

    return img_normalizada*255
