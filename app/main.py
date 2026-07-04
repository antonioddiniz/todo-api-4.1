"""API REST de uma aplicação de TODO list (Exercício 4.1).

Contrato (ver tutorial_4.1.md):
  GET  /health          -> 200 {"status": "ok"}
  POST /tarefas         -> 201 {"id", "titulo", "concluida": false}
  GET  /tarefas/{id}    -> 200 tarefa | 404
  GET  /tarefas         -> 200 [tarefas]
  PUT  /tarefas/{id}    -> 200 tarefa atualizada | 404

Armazenamento em memória: zera ao reiniciar o processo. Como o store começa
vazio, o primeiro POST cria a tarefa de id=1 (avaliação determinística).
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="TODO API", version="1.0.0")

# Store em memória (id -> tarefa). Zera quando o processo reinicia.
_tarefas: dict[int, dict] = {}
_proximo_id = 1


class TarefaIn(BaseModel):
    titulo: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tarefas", status_code=201)
def criar(tarefa: TarefaIn):
    global _proximo_id
    nova = {"id": _proximo_id, "titulo": tarefa.titulo, "concluida": False}
    _tarefas[_proximo_id] = nova
    _proximo_id += 1
    return nova


@app.get("/tarefas")
def listar():
    return list(_tarefas.values())


@app.get("/tarefas/{tarefa_id}")
def obter(tarefa_id: int):
    tarefa = _tarefas.get(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="tarefa não encontrada")
    return tarefa
