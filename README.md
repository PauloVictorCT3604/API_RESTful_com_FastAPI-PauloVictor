# Casa de Peças do Paulin 🛜

Este é um projeto simples utilizando FastAPI para gerenciar um estoque de peças automotivas. Ele oferece funcionalidades básicas de CRUD e é um excelente ponto de partida para aprender sobre FastAPI e desenvolvimento de APIs RESTful.

---

## Funcionalidades ✨

- 📚 Listar todas as peças.
- 🔍 Obter detalhes de uma peça por ID.
- ➕ Adicionar uma nova peça ao estoque.
- 🖋️ Atualizar os dados de uma peça existente.
- ❌ Deletar uma peça do estoque.

---

## Endpoints 🌐

### 1. Listar Todas as Peças 📚
**GET** `/pecas`

Resposta:
```json
[
    {
        "id": 1,
        "referencia": "MB108",
        "nome_fabricante": "Mombesani",
        "nome_peca": "Base do motor",
        "veiculos_aplicaveis": ["Cobalt"],
        "preco": 100.0,
        "quantidade": 2
    },
    ...
]
```

### 2. Obter Peça por ID 🔍
**GET** `/pecas/{id_peca}`

Resposta (caso encontrada):
```json
{
    "id": 1,
    "referencia": "MB108",
    "nome_fabricante": "Mombesani",
    "nome_peca": "Base do motor",
    "veiculos_aplicaveis": ["Cobalt"],
    "preco": 100.0,
    "quantidade": 2
}
```

### 3. Adicionar Nova Peça ➕
**POST** `/pecas`

Dados no corpo da requisição:
```json
{
    "id": 4,
    "referencia": "HG45665",
    "nome_fabricante": "Nakata",
    "nome_peca": "Amortecedor TS",
    "veiculos_aplicaveis": ["Palio"],
    "preco": 50.0,
    "quantidade": 6
}
```

Resposta:
```json
{
    "id": 4,
    "referencia": "HG45665",
    "nome_fabricante": "Nakata",
    "nome_peca": "Amortecedor TS",
    "veiculos_aplicaveis": ["Palio"],
    "preco": 50.0,
    "quantidade": 6
}
```

### 4. Atualizar Dados de uma Peça 🖋️
**PUT** `/pecas/{id_peca}`

Dados no corpo da requisição:
```json
{
    "id": 2,
    "referencia": "MB589",
    "nome_fabricante": "Mombesani",
    "nome_peca": "Bucha estabilizadora",
    "veiculos_aplicaveis": ["Celta", "Agile"],
    "preco": 25.0,
    "quantidade": 10
}
```

Resposta:
```json
{
    "id": 2,
    "referencia": "MB589",
    "nome_fabricante": "Mombesani",
    "nome_peca": "Bucha estabilizadora",
    "veiculos_aplicaveis": ["Celta", "Agile"],
    "preco": 25.0,
    "quantidade": 10
}
```

### 5. Deletar uma Peça ❌
**DELETE** `/pecas/{id_peca}`

Resposta:
```json
{
    "mensagem": "Peça deletada com sucesso",
    "peca": {
        "id": 4,
        "referencia": "HG45665",
        "nome_fabricante": "Nakata",
        "nome_peca": "Amortecedor TS",
        "veiculos_aplicaveis": ["Palio"],
        "preco": 50.0,
        "quantidade": 6
    }
}
```

---

## Como Executar 🚀

### Requisitos
- Python 3.9 ou superior.
- Gerenciador de dependências `pip`.

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o servidor de desenvolvimento:
   ```bash
   uvicorn main:app --reload
   ```

4. Acesse as documentações da API no navegador:
   - **Swagger**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Importação no Postman 📬

Utilize o arquivo `CasaDePecasDoPaulin.postman_collection.json` para importar a coleção de rotas no Postman e testar os endpoints com facilidade.

---

## Licença 🔒

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

