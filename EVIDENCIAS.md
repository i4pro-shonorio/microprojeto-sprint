# Evidências do Microprojeto TODO CLI

## 1. Objetivo
Construir um microprojeto de CLI para gerenciamento de tarefas persistidas em JSON, adicionando cores, notificação opcional por email (SendGrid) e testes de casos extremos. Meta: execução ponta a ponta com testes aprovados.

## 2. Linha do Tempo (Sessões Principais)
- Criação de `main.py` inicial (comentário descritivo)
- Scaffold de módulos: `models.py`, `storage.py`, `cli.py`
- Entrada principal atualizada executando a CLI
- Adição de recursos: cores (`colorama`), envio opcional de email (API HTTP SendGrid)
- Testes de borda: descrição vazia, ID inexistente, JSON corrompido
- Refatoração (extração de `utils.py`)
- Criação de `README.md`
- Execução local: criação de venv, instalação dependências, comandos de fluxo, testes
- Geração deste relatório de evidências

## 3. Estrutura do Projeto (arquivos relevantes)
```
main.py
todo_app/
  __init__.py
  cli.py
  models.py
  storage.py
  utils.py
tests/
  test_edge_cases.py
requirements.txt
README.md
EVIDENCIAS.md
```

## 4. Contagem de Linhas (arquivos de código)
| Arquivo | Linhas |
|---------|--------|
| main.py | 6 |
| todo_app/cli.py | 101 |
| todo_app/models.py | 32 |
| todo_app/storage.py | 25 |
| todo_app/utils.py | 51 |
| tests/test_edge_cases.py | 38 |
| TOTAL | 253 |

Observação: Contagem inclui apenas arquivos de código do projeto (excluindo dependências e arquivos gerados em cache).

## 5. Execução de Comandos (Fluxo Real)
### 5.1 Lista inicial (sem tarefas)
```
Nenhuma tarefa.
```
### 5.2 Adicionar tarefa
```
Adicionada tarefa 1: Primeira tarefa
```
### 5.3 Concluir tarefa
```
Tarefa 1 concluída.
```
### 5.4 Listar novamente
```
  1 [✔] Primeira tarefa
```

## 6. Execução de Testes
Comando:
```
pytest -q
```
Saída:
```
...                                                                                                            [100%]
3 passed in ~1.2s
```
Resultado: 3 testes passaram (casos de borda validados).

## 7. Recursos Implementados
- CRUD básico (add, list, done, delete)
- Persistência local em `tasks.json`
- Tratamento de JSON corrompido
- Validação de descrição vazia
- Output com cores (degrada graciosamente se `colorama` ausente)
- Notificação opcional via SendGrid (variáveis de ambiente: `SENDGRID_API_KEY`, `SENDGRID_FROM`, `SENDGRID_TO`)
- Testes de borda automatizados com `pytest`
- Refatoração para módulo utilitário (`utils.py`)

## 8. Variáveis de Ambiente (Email)
```
SENDGRID_API_KEY=<chave>
SENDGRID_FROM=<email_origem>
SENDGRID_TO=<email_destino>
```
Se ausentes, a função de envio é ignorada sem interromper o fluxo principal.

## 9. Critério de Qualidade
Arquitetura simples, módulos separados e testes de casos de borda para validar comportamento em cenários anômalos.

## 10. Possíveis Extensões Futuras
- Prioridade e data de vencimento
- Edição de descrição (`edit <id> <nova descrição>`)
- Exportação CSV / Markdown
- Relatório de produtividade (tarefas concluídas por período)

## 11. Conclusão
Projeto cumpre objetivos: aplicativo funcional, testes aprovados, documentação entregue e evidências registradas neste arquivo.

---
Relatório consolidado do microprojeto.
