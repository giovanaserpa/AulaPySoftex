estoque = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}
estoque["pera"] = 12
estoque.pop("banana") 
print("Itens do estoque:", list(estoque.keys()))