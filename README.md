# TODO API — Exercício 4.1

API REST mínima que serve de backend para uma aplicação de lista de tarefas
(*TODO list*). Armazenamento em memória, exposta em `http://localhost:8000`.

**Aluno:** Antonio Diniz · **Disciplina:** IDP-TD 2026

## Contrato

| Método | Rota | Corpo | Resposta |
|--------|------|-------|----------|
| GET | `/health` | — | `200 {"status":"ok"}` |
| POST | `/tarefas` | `{"titulo":"<str>"}` | `201 {"id","titulo","concluida":false}` |
| GET | `/tarefas/{id}` | — | `200` a tarefa · `404` se não existe |
| GET | `/tarefas` | — | `200 [ ...tarefas... ]` |
| PUT | `/tarefas/{id}` | `{"titulo":"<str>","concluida":<bool>}` | `200` atualizada · `404` |

O `id` autoincrementa a partir de `1`. O store zera ao reiniciar o processo.

## Como rodar

```bash
pip install -r requirements.txt
uvicorn app.main:app --port 8000
```

Testar:

```bash
curl -s http://localhost:8000/health
curl -s -X POST http://localhost:8000/tarefas \
  -H "Content-Type: application/json" -d '{"titulo":"estudar APIs"}'
curl -s http://localhost:8000/tarefas/1
```

## Estrutura

```
app/
  __init__.py
  main.py            # implementação da API (FastAPI)
requirements.txt     # fastapi, uvicorn
README.md
.autograde-exercise  # 4.1
```
