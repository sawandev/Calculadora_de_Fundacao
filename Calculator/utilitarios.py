def baldrame():
    prof_b = float(input('PROFUNDIDADE do Baldrame (EM METROS): '))
    larg_b = float(input('LARGURA do Baldrame (EM METROS): '))
    comp_b = float(input('COMPRIMENTO do Baldrame (EM METROS): '))
    quant_b = int(input('Insira a QUANTIDADE de Baldrame que você precisa calcular: '))
    print()   
    total_b = prof_b * larg_b * comp_b
    total_b *= quant_b
    print(f'Você precisará de {total_b:.2f}m3 de concreto para os BALDRAMES.')
    return total_b


def bloco():
    prof_bl = float(input('PROFUNDIDADE do Bloco de Coroamento (EM METROS): '))
    larg_bl = float(input('LARGURA do Bloco de Coroamento (EM METROS): '))
    comp_bl = float(input('COMPRIMENTO do Bloco de Coroamento (EM METROS): '))
    quant_bl = int(input('Insira a QUANTIDADE de Blocos que você precisa calcular: '))
    print()
    total_bl = prof_bl * larg_bl * comp_bl
    total_bl *= quant_bl
    print(f'Você precisará de {total_bl:.2f}m3 de concreto para os BLOCOS DE COROAMENTO.')
    return total_bl


def estaca():
    diam_e = float(input('DIÂMETRO da Estaca (EM CENTÍMETROS): '))
    prof_e = float(input('PROFUNDIDADE da Estaca (EM METROS): '))
    quant_e = int(input('Insira a QUANTIDADE de Estacas que você precisa calcular: '))
    print()
    raio_e = (diam_e / 2) / 100
    area_e = 3.14 * (raio_e) ** 2
    total_e = area_e * prof_e
    total_e *= quant_e
    print(f'Você precisará de {total_e:.2f}m3 de concreto para as ESTACAS.')
    return total_e

def linha():
    print('_' * 80)
