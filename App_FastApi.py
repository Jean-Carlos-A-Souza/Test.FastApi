from fastapi import FastAPI, HTTPException

app = FastAPI()

sorteios = {
    1: {"id": 1, "item": "Tracker Premier", "preco":125.000, "cor": "Azul", "ano": 2022, "marca":"Chevrolet", "descricao":"Carro novo na cor azul com interna na cor bege com abamento em plastico, mais com algumas firulas interesantes, motor 1.2 turbo, anda bem e confiavel." },
    2: {"id": 2, "item": "Nova Ranger", "preco":250.000, "cor": "Prata", "ano": 2024, "marca":"Ford", "descricao":"Carro novo na cor prata com interna na cor bege com abamento em plastico, mais com algumas firulas interesantes, motor 2.0 turbo diesel, forte e confiavel." },
    3: {"id": 3, "item": "Nova S10", "preco":225.000, "cor": "Branco", "ano": 2024, "marca":"Chevrolet", "descricao":"Carro novo na cor branco com interna na cor bege com abamento em plastico, mais com algumas firulas interesantes, motor 2.0 turbo diesel, forte e confiavel." },
    4: {"id": 4, "item": "Onix Premier", "preco":125.000, "cor": "Branco", "ano": 2023, "marca":"Chevrolet", "descricao":"Carro semi-novo na cor branco com interna na cor bege com abamento em plastico, com acabamento razoavel, motor 1.0 turbo, economico e anda razoavelmente bem." },
    5: {"id": 5, "item": "Nissan Sentra", "preco":95.000, "cor": "Preto", "ano": 2024, "marca":"Nissan","descricao":"Carro novo na cor preta com interna na cor branca com abamento em plastico, com bom acabamento, motor 1.6 turbo, economico e anda bem." },
    6: {"id": 6, "item": "C4 Cactus", "preco":90.000, "cor": "Prata", "ano": 2022, "marca":"Citroen","descricao":"Carro semi-novo na cor prata com interna na cor preta com abamento em plastico, com bom acabamento, motor 1.6 turbo, economico e anda bem." },
    7: {"id": 7, "item": "Dodge Ram", "preco":325.000, "cor": "Branco Perola", "ano": 2022, "marca":"RAM", "descricao":"Carro novo na cor branco perola com interna na cor laranja de couro sintetico, com acabamentos dos mais luxuosos, motor bruto que puxa tudo que tiver, carroceria grande." },
}

usuarios = {
   1: {"user": "jean@gmail.com", "senha": "1", "id": 1},
   2: {"user": "jeansouza@gmail.com", "senha": "12", "id": 2},
   3: {"user": "j@gmail.com", "senha": "123", "id": 3}
}

@app.get("/todos")
def todos_sorteios():
  return (sorteios)

@app.get("/sorteio/{id_sorteio}")
def busca_sorteio(id_sorteio: int):
  if id_sorteio not in sorteios:
        raise HTTPException(status_code=404, detail="Item não encontrado")
  return sorteios[id_sorteio]

@app.get("/usuarios")
def home_user():
  return (usuarios)


@app.get("/")
def home():
  return ('Bem Vindo ao teste')