# TODO CLI (Microprojeto Sprint)

![CI](https://github.com/i4pro-shonorio/microprojeto-sprint/actions/workflows/tests.yml/badge.svg)

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

## Integração Contínua
A pipeline GitHub Actions (`.github/workflows/tests.yml`) executa a suíte de testes em Python 3.10, 3.11 e 3.12 a cada push ou pull request para `main`.

## Changelog
Ver `CHANGELOG.md` para histórico detalhado. Primeira versão: v0.1.0.

## Metas de Qualidade
- Simples, legível, funções pequenas
- Falhas de email não interrompem o fluxo principal
- Testes de borda garantem comportamento previsível

## Roadmap Curto
- Prioridade / data limite
- Comando para editar descrição
- Geração de relatório (ex: CSV)
- Mais testes (cobrir editar quando implementado)

## Licença
Distribuído sob a licença MIT. Veja `LICENSE`.

---
Documento final do microprojeto.
