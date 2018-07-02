def contarVasosLevantados(lista, search):
   izq = 0
   der = len(lista) - 1
   cont=0
   while True:
       if der < izq:
           break
       mid = (izq + der) // 2
       print("levantar vaso ", mid, ":", lista[mid])
       cont=cont + 1
       if search == lista[mid]:
           break
       elif search < lista[mid]:
           izq = mid + 1
       elif search > lista[mid]:
           der = mid - 1
   return cont

bolitasStr=input().split(",")
search=int(input())
bolitasInt = [int(i) for i in bolitasStr]
print(contarVasosLevantados(bolitasInt, search))
