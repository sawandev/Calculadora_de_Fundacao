from interface_code import *
from math_code import *
from time import sleep


def main():
    while True:
        resposta = menu([
            'Calcular os BALDRAMES', 
            'Calcular os BLOCOS DE COROAMENTO', 
            'Calcular as ESTACAS',
            'Calcular BALDRAMES e BLOCOS DE COROAMENTO',
            'Calcular BALDRAMES e ESTACAS',
            'Calcular BLOCOS DE COROAMENTO e ESTACAS', 
            'Calcular TUDO',
            'Sair'])
        
        if resposta == 1:
            total_b = baldrame()
            cabeçalho(f'Você precisará de {total_b:.2f}m3 de concreto.')
            break

        elif resposta == 2:
            total_bl = bloco()
            cabeçalho(f'Você precisará de {total_bl:.2f}m3 de concreto.')
            break

        elif resposta == 3:
            total_e = estaca()
            cabeçalho(f'Você precisará de {total_e:.2f}m3 de concreto.')
            break

        elif resposta == 4:
            total_b = baldrame()
            total_bl = bloco()
            cabeçalho(f'Você precisará de {total_b + total_bl:.2f}m3 de concreto.')
            break

        elif resposta == 5:
            total_b = baldrame()
            total_e = estaca()
            cabeçalho(f'Você precisará de {total_b + total_e:.2f}m3 de concreto.')
            break

        elif resposta == 6:
            total_bl = bloco()
            total_e = estaca()
            cabeçalho(f'Você precisará de {total_bl + total_e:.2f}m3 de concreto.')
            break

        elif resposta == 7:
            total_b = baldrame()
            total_bl = bloco()
            total_e = estaca()
            cabeçalho(f'Você precisará de {total_b + total_bl + total_e:.2f}m3 de concreto.')
            break
        
        elif resposta == 8:
            break

        sleep(2)

if __name__ == '__main__':
    main()