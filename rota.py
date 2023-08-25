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
    lista = []
    for i in range(len(arrayT[coluna_atual])):
        lista.append(arrayT[coluna_atual])

    if str(type) == 'd':
        return min(lista[coluna_atual]), i
    elif str(type) == 'v':
        return max(lista[coluna_atual]), i
    else:
        return



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
    tempo = []
    sq1, sq2  = verify_sq(array_vel), verify_sq(array_dist)

    if sq1 and sq2:
        pos_ate_final = len(array_vel[0]) - coluna

        while pos_ate_final > 0:

            best_vel, pos = get_best_value(array_vel, coluna, 'v')
            contra = array_vel[pos]
            best_dist, pos = get_best_value(array_dist, coluna, 'd')
            contra2 = array_dist[pos]

            tempo.append(best_vel / contra)
            tempo.append(contra2 / best_dist)

            coluna += 1
            pos_ate_final -= 1

    print(tempo)
    # return min(list(tempo))

posicao = 0
x = build_path(aVelMedia, aDistancia, posicao)

print(x)