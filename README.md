# TODO CLI (Microprojeto Sprint)

Aplicativo de linha de comando simples para gerenciar tarefas persistidas em `tasks.json`.

## Funcionalidades
- Adicionar, listar, concluir e remover tarefas
- Persistência em JSON no diretório atual
- Saída colorida (verde: sucesso, vermelho: erro, ciano: informativo) usando `colorama` (fallback silencioso se não instalado)
- Notificação opcional por e-mail via API SendGrid (sem dependência externa) quando tarefa é criada ou concluída

## Requisitos
- Python 3.10+
- (Opcional) Conta SendGrid e chave de API

## Instalação
Crie e ative um ambiente virtual (opcional, mas recomendado) e instale dependências mínimas.

```bash
pip install colorama pytest
```

(O envio de e-mail não precisa de instalação extra.)

## Uso

```bash
python main.py add "Estudar testes"
python main.py list
python main.py done 1
python main.py delete 1
```

Saída exemplo:
```
$ python main.py add "Escrever README"
Adicionada tarefa 1: Escrever README
$ python main.py list
  1 [✗] Escrever README
$ python main.py done 1
Tarefa 1 concluída.
```

## Email (SendGrid Opcional)
Defina variáveis de ambiente antes de executar:

```bash
set SENDGRID_API_KEY=SUACHAVE
set SENDGRID_FROM=seu-email@exemplo.com
set SENDGRID_TO=destinatario@exemplo.com
```
(Em Linux/macOS use `export`.)

Quando configurado, o app tenta enviar e imprime o status (não falha caso dê erro).

## Testes

Três casos de borda com `pytest`:
- Descrição vazia
- ID inexistente ao concluir
- Arquivo JSON corrompido

Executar:
```bash
pytest -q
```

## Estrutura
```
main.py
todo_app/
  cli.py
  models.py
  storage.py
  utils.py
tests/
  test_edge_cases.py
```

## Metas de Qualidade
- Simples, legível, funções pequenas
- Falhas de email não interrompem o fluxo principal

## Próximos Passos Sugeridos
- Acrescentar prioridade / data limite
- Comando para editar descrição
- Geração de relatório (ex: CSV)

---
Documento final do microprojeto.
