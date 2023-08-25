# import sys
# import subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])

import numpy as np

aDistancia = [
        [41.3, 21.0, 12.8],
        [31.0, 25.6, 14.0],
        [32.5, 28.4, 11.0]
    ]

aVelMedia = [
        [31.0, 41.0, 32.5],
        [27.0, 44.0, 33.0],
        [34.0, 48.0, 20.6]
    ]

def get_best_value(array, coluna_atual, type):
    arrayT = np.transpose(array)
    print(arrayT)
    lista = []
    for i in range(len(arrayT[coluna_atual])):
        lista.append(arrayT[coluna_atual])
    print(lista)

    if str(type) == 'd':
        print('distancia')
        return min(lista[coluna_atual])
    elif str(type) == 'v':
        print('velocidade')
        return max(lista[coluna_atual])
    else:
        return

posicao = 1

distancia = get_best_value(aDistancia, posicao, 'd')
print(distancia)

velocidade = get_best_value(aVelMedia, posicao, 'v')
print(velocidade)


def verify_sq(array):
    altura = len(array)
    largura = len(array[0])

    if altura != largura:
        print("A matriz não é quadrada")
        return False
    else:
        return True

# def verify_arrays_eq(array_vel, array_dist):
#     pass

# def verify_div_zero(val_vel, vel_dist):
#     pass

def build_path(array_vel, array_dist, coluna):
    sq1, sq2  = verify_sq(array_vel), verify_sq(array_dist)

    tempo = []

    if sq1 and sq2:
        pos_ate_final = len(array_vel[0]) - coluna

        while pos_ate_final > 0:

            best_vel = get_best_value(array_vel, coluna, 'v')
            print("best_vel", best_vel)

            best_dist = get_best_value(array_dist, coluna, 'd')
            print("best_dist", best_dist)

            tempo.append(best_dist / best_vel)

            coluna += 1
            pos_ate_final -= 1

    return min(tempo)


