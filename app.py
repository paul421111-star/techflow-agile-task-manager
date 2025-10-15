from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="TechFlow Agile Task Manager")

class Task(BaseModel):
    id: int
    titulo: str = Field(min_length=1)
    descricao: Optional[str] = None
    status: str = Field(pattern="^(A Fazer|Em Progresso|Concluído)$")
    prioridade: str = Field(
        default="Média",
        pattern="^(Alta|Média|Baixa)$"
    )

_db: List[Task] = []
_seq = 1

@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return _db

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(
    titulo: str,
    descricao: Optional[str] = None,
    prioridade: str = "Média"
):
    global _seq
    task = Task(
        id=_seq,
        titulo=titulo,
        descricao=descricao,
        status="A Fazer",
        prioridade=prioridade
    )
    _seq += 1
    _db.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for t in _db:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task não encontrada")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    titulo: Optional[str] = None,
    descricao: Optional[str] = None,
    status: Optional[str] = None,
    prioridade: Optional[str] = None
):
    for i, t in enumerate(_db):
        if t.id == task_id:
            data = t.dict()
            if titulo is not None:
                data["titulo"] = titulo
            if descricao is not None:
                data["descricao"] = descricao
            if status is not None:
                data["status"] = status
            if prioridade is not None:
                data["prioridade"] = prioridade
            new_t = Task(**data)
            _db[i] = new_t
            return new_t
    raise HTTPException(status_code=404, detail="Task não encontrada")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, t in enumerate(_db):
        if t.id == task_id:
            del _db[i]
            return
    raise HTTPException(status_code=404, detail="Task não encontrada")
