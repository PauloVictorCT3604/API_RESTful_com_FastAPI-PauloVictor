from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI()

ARQUIVO_DADOS = "pecas.json"

class Peca(BaseModel):
    id: int
    referencia: str
    nome_fabricante: str
    nome_peca: str
    veiculos_aplicaveis: Optional[List[str]] = None
    preco: float
    quantidade: int

pecas = []

def carregar_pecas():
    global pecas
    try:
        with open(ARQUIVO_DADOS, "r") as arquivo:
            pecas = [Peca(**dados) for dados in json.load(arquivo)]
        pecas.sort(key=lambda p: p.id)
    except FileNotFoundError:
        pecas = []

def salvar_pecas():
    pecas.sort(key=lambda p: p.id)
    with open(ARQUIVO_DADOS, "w") as arquivo:
        json.dump([peca.dict() for peca in pecas], arquivo, indent=4)

carregar_pecas()

def encontrar_indice_peca(id_peca: int):
    for indice, peca in enumerate(pecas):
        if peca.id == id_peca:
            return indice
    return None

@app.get("/pecas", response_model=List[Peca])
def listar_pecas():
    pecas.sort(key=lambda p: p.id)
    return pecas

@app.get("/pecas/{id_peca}", response_model=Peca)
def obter_peca(id_peca: int):
    indice = encontrar_indice_peca(id_peca)
    if indice is None:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    return pecas[indice]

@app.post("/pecas", response_model=Peca)
def adicionar_peca(peca: Peca):
    if any(peca_existente.id == peca.id for peca_existente in pecas):
        raise HTTPException(status_code=400, detail="Peça com este ID já existe")
    pecas.append(peca)
    salvar_pecas() 
    return peca

@app.put("/pecas/{id_peca}", response_model=Peca)
def atualizar_peca(id_peca: int, peca_atualizada: Peca):
    indice = encontrar_indice_peca(id_peca)
    if indice is None:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    if id_peca != peca_atualizada.id:
        raise HTTPException(status_code=400, detail="Não é possível alterar o ID da peça")
    pecas[indice] = peca_atualizada
    salvar_pecas()
    return peca_atualizada

@app.delete("/pecas/{id_peca}", response_model=dict)
def deletar_peca(id_peca: int):
    indice = encontrar_indice_peca(id_peca)
    if indice is None:
        raise HTTPException(status_code=404, detail="Peça não encontrada")
    peca_removida = pecas.pop(indice)
    salvar_pecas()
    return {"mensagem": "Peça deletada com sucesso", "peca": peca_removida}
