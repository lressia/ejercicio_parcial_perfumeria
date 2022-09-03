import random
from registro_perfumeria import *

def azar():
    num = random.randint(0, 300)
    importe = random.random() * 1000 + 1
    tipo = random.choice(['A', 'B', 'C', 'E'])
    apellido = random.choice(['Ressia', 'Fernandez', 'Mansilla', 'Trump'])
    perfume = random.randint(0, 17)

    return num, importe, tipo, apellido, perfume

def validate(n):
    while n < 0:
        n = int(input('Por favor introduzca un numero mayor a cero'))
    return n

def sort(v):
    x = int(input('Introduzca un numero: '))
    t = input('Introduzca un tipo de factura(A, B, C, E): ').upper()
    aux = []
    for i in range(len(v)):
        if v[i].importe > x and v[i].tipo != t:
            aux += v[i:i+1]
    for i in range(len(aux)):
        for j in range(len(aux)):
            if aux[i].apellido < aux[j].apellido:
                aux[i], aux[j] = aux[j], aux[i]
    for i in range(len(aux)):
        write(aux[i])

def importe(v):
    z = int(input('Introduzca un numero(menor a 18): '))
    aux = [0] * len(v)
    for i in range(17):
        for j in range(len(v)):
            if i == v[j].perfume:
                aux[i] += v[j].importe
    print(f'El total del importe del perfume {z} es: ${aux[z]}\n')

def show(v):
    flag = False
    for i in range(len(v)):
        if v[i].perfume > 4 and v[i].perfume < 13 and v[i].tipo != 'C':
            write(v[i])
            flag = True
    if not flag:
        print('No se encuentran coincidencias')

def factura(v):
    num = int(input('Por favor introduzca un numero de factura: '))
    val = float(input('Por favor introduzca un monto: '))
    flag = False
    for i in range(len(v)):
        if v[i].num == num and v[i].importe < val:
            write(v[i])
            flag = True
            break
    if not flag:
        print('No se encontraron resultados')

def principal():
    op = int(input('Elija una opcion:\n1-Cargar datos(obligatorio)\n2-Mostrar trabajos con trabajadores > 3\n3-Tipos de trabajos\n4-Trabajos mas paga'
                   '\n5-Comparar\n'))
    v = 0
    flag = True
    while flag:
        while op > 5 or op <= 0:
            op = int(input('Elija una opcion:\n1-Cargar datos(obligatorio)\n2-Mostrar trabajos con trabajadores > 3\n3-Tipos de trabajos\n4-Trabajos mas paga'
                   '\n5-Comparar\n'))
        else:
            while op != 1 and v == 0:
                print('Tiene que cargar los datos antes de continuar')
                op = int(input('Por favor seleccione una opcion: '))
            else:
                if op == 1:
                    n = int(input('Introduzca una cantidad de datos a procesar: '))
                    n = validate(n)
                    v = [None] * n
                    for i in range(n):
                        v[i] = Ventas(azar()[0], azar()[1], azar()[2], azar()[3], azar()[4])
                    op = int(input('Por favor seleccione una opcion: '))
                elif op == 2:
                    sort(v)
                    op = int(input('Por favor seleccione una opcion: '))
                elif op == 3:
                    importe(v)
                    op = int(input('Por favor seleccione una opcion: '))
                elif op == 4:
                    show(v)
                    op = int(input('Por favor seleccione una opcion: '))
                elif op == 5:
                    factura(v)
                    op = int(input('Por favor seleccione una opcion: '))

if __name__ == '__main__':
    principal()
