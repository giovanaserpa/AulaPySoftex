#Herança única
class Mamifero:
    def __init__(self, especie, habitat):
        self.especie = especie
        self.habitat = habitat

    def __str__(self):
        return f"O mamífero da espécie {self.especie}, pode ser localizado no {self.habitat}"
    def movimentar(self):
        print("Caminhando")
    def amamentar(self):
        print("alimentando o filhote")

class Cachorro(Mamifero):
    def __init__(self, especie, habitat, raca):
        super().__init__(especie, habitat)
        self.raca = raca 
    def correr_moto(self):
        print("O cachorro esta correndo atrás da moto")
    def __str__(self):
        return f"{super().__str__()} da raça {self.raca}"
dog01= Cachorro("canis familiaris", "rua dos bobos", "caramelo")
print(dog01)
dog01.movimentar()
dog01.correr_moto()
dog01.amamentar()

#herança hierárquica
class Gato(Mamifero):
    def __init__(self, especie, habitat, raca, cor_olho):
        super().__init__(especie, habitat)
        self.raca = raca
        self.cor_olho = cor_olho
    def __str__(self):
        return f"O mamífero da espécie {self.especie}, pode ser localizado no {self.habitat}, com os olhos na cor {self.cor_olho}"
    def arranhar(self):
        print("O gato está arranhando o sofá")

cat01 = Gato("felinis", "cama da vó", "siamês", "azul")
print(cat01)
cat01.arranhar()

#Herança múltipla
class Voadores:
    def movimentar(self):
        print("Voando")

class Morcego(Mamifero,Voadores):
    ...

zubat = Morcego("desmodus", "pe de jambo")
print(zubat)
zubat.movimentar()
