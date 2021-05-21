import utilitarios

print('Programa de auxílio á Mestres de Obras!')
print('Criado por: @im_sauannn')
print()
print()
print('''
                    CALCULADORA DE FUNDAÇÃO''')
while True:
    print('''
                    ***********************
                    * BALDRAME CALCULATOR *
                    ***********************
''')
    escolha_baldrame = str(input('''Deseja calcular os BALDRAMES?
Digite 'S' para SIM!
Digite 'N' para NÃO!
------------------> ''')).strip().lower()[0]
    print()
    if 'n' in escolha_baldrame:
        total_b = 0
        break
    
    if 's' in escolha_baldrame:
        total_b = utilitarios.baldrame()
        utilitarios.linha()
        break

while True:
    print('''
                    ********************
                    * BLOCO CALCULATOR * 
                    ********************
''')
    escolha_bloco = str(input('''Deseja calcular os BLOCOS DE COROAMENTO?
Digite 'S' para SIM!
Digite 'N' para NÃO!
------------------> ''')).strip().lower()[0]
    print()
    if 'n' in escolha_bloco:
        total_bl = 0
        break
    
    if 's' in escolha_bloco:
        total_bl = utilitarios.bloco()
        utilitarios.linha()
        break

while True:
    print('''
                    **********************
                    * ESTACAS CALCULATOR * 
                    **********************
''')
    escolha_estaca = str(input('''Deseja calcular as ESTACAS?
Digite 'S' para SIM!
Digite 'N' para NÃO!
------------------> ''')).strip().lower()[0]
    print()
    if 'n' in escolha_estaca:
        total_e = 0
        break
    
    if 's' in escolha_estaca:
        total_e = utilitarios.estaca()
        utilitarios.linha()
        break

print(f'CONCRETO TOTAL: {total_b + total_bl + total_e:.2f}m3')
input()
