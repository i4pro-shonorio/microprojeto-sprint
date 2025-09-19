from __future__ import annotations
import argparse
from typing import List
from .storage import Storage
from .models import Task
from .utils import COLOR_OK, COLOR_ERR, COLOR_INFO, maybe_send_email



def get_next_id(tasks: List[Task]) -> int:
    return (max((t.id for t in tasks), default=0) + 1) if tasks else 1


def cmd_add(args, storage: Storage):
    if not args.description.strip():
        print(COLOR_ERR + "Descrição não pode ser vazia.")
        return 1
    tasks = storage.load()
    task = Task.new(id=get_next_id(tasks), description=args.description.strip())
    tasks.append(task)
    storage.save(tasks)
    print(COLOR_OK + f"Adicionada tarefa {task.id}: {task.description}")
    info = maybe_send_email(
        subject=f"Nova tarefa #{task.id}", body=f"Descrição: {task.description}"
    )
    if info:
        print(COLOR_INFO + info)
    return 0


def cmd_list(args, storage: Storage):
    tasks = storage.load()
    if not tasks:
        print(COLOR_INFO + "Nenhuma tarefa.")
        return 0
    for t in tasks:
        status = "✔" if t.completed else "✗"
        color = COLOR_OK if t.completed else ""
        print(color + f"{t.id:3} [{status}] {t.description}")
    return 0


def cmd_done(args, storage: Storage):
    tasks = storage.load()
    for t in tasks:
        if t.id == args.id:
            if t.completed:
                print(COLOR_INFO + "Já estava concluída.")
            else:
                t.mark_done()
                storage.save(tasks)
                print(COLOR_OK + f"Tarefa {t.id} concluída.")
                info = maybe_send_email(
                    subject=f"Tarefa concluída #{t.id}", body=t.description
                )
                if info:
                    print(COLOR_INFO + info)
            return 0
    print(COLOR_ERR + "ID não encontrado.")
    return 1


def cmd_delete(args, storage: Storage):
    tasks = storage.load()
    before = len(tasks)
    tasks = [t for t in tasks if t.id != args.id]
    if len(tasks) == before:
        print(COLOR_ERR + "ID não encontrado.")
        return 1
    storage.save(tasks)
    print(COLOR_OK + f"Tarefa {args.id} removida.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="todo", description="Gerenciador simples de tarefas")
    sub = p.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Adicionar tarefa")
    p_add.add_argument("description", help="Descrição da tarefa")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="Listar tarefas")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="Marcar tarefa como concluída")
    p_done.add_argument("id", type=int)
    p_done.set_defaults(func=cmd_done)

    p_delete = sub.add_parser("delete", help="Remover tarefa")
    p_delete.add_argument("id", type=int)
    p_delete.set_defaults(func=cmd_delete)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    storage = Storage()
    return args.func(args, storage)
