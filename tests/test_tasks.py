from fastapi.testclient import TestClient
import app as appmod

client = TestClient(appmod.app)

def test_create_and_get_task():
    r = client.post("/tasks", params={"titulo": "Primeira tarefa"})
    assert r.status_code == 201
    task = r.json()
    assert task["id"] == 1
    assert task["status"] == "A Fazer"

    r2 = client.get("/tasks/1")
    assert r2.status_code == 200
    assert r2.json()["titulo"] == "Primeira tarefa"

def test_update_status_validation_and_delete():
    client.post("/tasks", params={"titulo": "T2"})
    ok = client.put("/tasks/2", params={"status": "Em Progresso"})
    assert ok.status_code == 200

    bad = client.put("/tasks/2", params={"status": "Doing"})
    # FastAPI/Pydantic deve barrar por padrão (422)
    assert bad.status_code == 422

    r = client.delete("/tasks/2")
    assert r.status_code == 204

    r2 = client.get("/tasks/2")
    assert r2.status_code == 404
    
def test_create_task_with_priority():
    r = client.post("/tasks", params={"titulo": "Com prioridade", "prioridade": "Alta"})
    assert r.status_code == 201
    t = r.json()
    assert t["prioridade"] == "Alta"

def test_update_priority():
    r = client.put("/tasks/1", params={"prioridade": "Baixa"})
    assert r.status_code == 200
    t = r.json()
    assert t["prioridade"] == "Baixa"
