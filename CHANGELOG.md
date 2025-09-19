# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato segue (livremente) as recomendações do Keep a Changelog e versionamento SemVer.

## [0.1.0] - 2025-09-19
### Adicionado
- CLI de tarefas (add, list, done, delete) com persistência em JSON.
- Modelo `Task` com timestamps ISO.
- Saída colorida opcional (usa colorama se disponível).
- Notificação de e-mail opcional via SendGrid (quando variáveis de ambiente configuradas).
- Tratamento de arquivo JSON corrompido.
- Testes de borda (3 cenários) usando pytest.
- Documentação (`README.md`) e evidências (`EVIDENCIAS.md`).
- Licença MIT.

### Refatorado
- Extração de utilidades (cores + envio de e-mail) para `todo_app/utils.py`.

### Segurança / Robustez
- Fallback seguro quando `colorama` não está instalado.
- Exceção clara em caso de JSON inválido.

[0.1.0]: https://github.com/i4pro-shonorio/microprojeto-sprint/releases/tag/v0.1.0