# TechFlow Agile Task Manager

Sistema fictício para acompanhar fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar desempenho da equipe de uma startup de logística.

## 🎯 Objetivo
- Demonstrar gestão ágil com GitHub (Issues/Projects/Kanban)  
- Implementar um CRUD simples de tarefas (API)  
- Garantir qualidade com testes automatizados e CI (GitHub Actions)

## 📌 Escopo (Versão 1)
- API de tarefas: criar, listar, detalhar, atualizar, excluir  
- Campos: `id`, `titulo`, `descricao`, `status` (A Fazer | Em Progresso | Concluído)

## 🧭 Metodologia
- Kanban no GitHub Projects (colunas: A Fazer, Em Progresso, Concluído)  
- Commits frequentes e descritivos  
- Testes automatizados com Pytest + integração contínua via GitHub Actions

---

## 🚀 Como Rodar Localmente

```bash
python -m venv .venv
# Ativar ambiente virtual:
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app:app --reload
