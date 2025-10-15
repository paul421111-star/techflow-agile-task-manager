# TechFlow Agile Task Manager

Sistema fictício para acompanhar fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar desempenho da equipe de uma startup de logística.

## 🎯 Objetivo
- Demonstrar gestão ágil com GitHub (Issues/Projects/Kanban)  
- Implementar um CRUD simples de tarefas (API)  
- Garantir qualidade com testes automatizados e CI (GitHub Actions)

## 📌 Escopo (Versão 2)
- API de tarefas: criar, listar, detalhar, atualizar, excluir  
- Campos:
  - `id`: identificador único da tarefa
  - `titulo`: título da tarefa
  - `descricao`: detalhes adicionais (opcional)
  - `status`: A Fazer | Em Progresso | Concluído
  - `prioridade`: Alta | Média | Baixa ✅ *(novo campo adicionado na mudança de escopo)*

## 🧭 Metodologia
- Kanban no GitHub Projects (colunas: A Fazer, Em Progresso, Concluído)  
- Commits frequentes e descritivos  
- Testes automatizados com Pytest + integração contínua via GitHub Actions

- ## ✨ Mudanças de Escopo
- [x] Adicionado campo `prioridade` ao modelo `Task`  
- Atualizados endpoints de criação e atualização para suportar o novo campo  
- Testes automatizados ajustados para cobrir prioridade  
- Documentação atualizada para refletir a alteração


----

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
