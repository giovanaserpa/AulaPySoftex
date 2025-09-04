#for i in range(5):
#    print(i)
#count = 0
#while True:
#    print('Dentro do while')
#    count+=1
#    if count ==4:
#        break

#Listas#

#lista = []
#print(type(lista)) 

#frutas = ["morango", "banana","coco","limão"]
#print(frutas)

#Adicionando elementos
#frutas.insert(1,"maca")
#print(frutas)
#insert define onde vai adicionar na lista
#append insere no final da lista
#frutas.append("kiwi")
#print(frutas)

#frutas_vermelhas = ["morango","uva","amora","framboesa"]
#frutas+=frutas_vermelhas
#print(frutas)

#Remover elementos
#print("Removendo elementos")
#print(frutas.count("morango"))
#frutas.remove("morango")
#print(frutas)

#print("Primeiro pop")
#frutas.pop()
#print(frutas)

#print("Segundo pop")
#frutas.pop(4)
#print(frutas)

#del frutas [5]
#print(frutas)

###Cópia de lista
print("-----------------")
frutas = ["morango", "banana","coco","limão"]
frutas2 = frutas[:]
frutas2 = frutas.copy()
print(frutas2)
print(id(frutas2))
print(id(frutas))

#frutas.clear()
#print(frutas)

frutas.sort()
print(frutas)
