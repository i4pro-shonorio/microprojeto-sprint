import json
import os
import subprocess
import sys
from pathlib import Path

PY = sys.executable
ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "main.py"
TASKS = ROOT / "tasks.json"


def run_cli(*args):
    cmd = [PY, str(MAIN), *args]
    return subprocess.run(cmd, capture_output=True, text=True)


def setup_function(function):
    if TASKS.exists():
        TASKS.unlink()


def test_add_empty_description():
    r = run_cli("add", "   ")
    assert r.returncode == 1
    assert "Descrição não pode ser vazia" in r.stdout


def test_done_nonexistent():
    r = run_cli("done", "999")
    assert r.returncode == 1
    assert "ID não encontrado" in r.stdout


def test_corrupted_json():
    TASKS.write_text("{not valid json}", encoding="utf-8")
    r = run_cli("list")
    assert r.returncode != 0 or "Arquivo JSON corrompido" in r.stdout or "Arquivo JSON corrompido" in r.stderr
