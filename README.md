# Python14
Python semana 14
def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j][1]>alist[j+1][1]:
                aux=alist[j]
                alist[j]=alist[j+1]
                alist[j+1]=aux
    return alist

def construir_list_hackerrank():
    alumnos =[]
    for _ in range(int(input())):
        nombre = input()
        nota = (int(input()))
        alumnos.append([nombre, nota])
    return alumnos
alumnos = construir_list_hackerrank()
AlmunosOrdenado = bubbleSort(alumnos)
for i in range(len(AlmunosOrdenado)):
    print(AlmunosOrdenado[i][0],AlmunosOrdenado[i][1])
