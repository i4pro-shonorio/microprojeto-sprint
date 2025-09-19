"""Aplicativo CLI para gerenciar uma lista de tarefas persistida em JSON."""

from todo_app.cli import main as cli_main

if __name__ == "__main__":  # ponto de entrada
	raise SystemExit(cli_main())
