from __future__ import annotations
import os
from typing import Optional

try:
    from colorama import Fore, init as colorama_init
    colorama_init(autoreset=True)
    COLOR_OK = Fore.GREEN
    COLOR_ERR = Fore.RED
    COLOR_INFO = Fore.CYAN
except Exception:  # fallback se não instalado
    COLOR_OK = COLOR_ERR = COLOR_INFO = ""
    def colorama_init(*a, **k):  # type: ignore
        pass

SENDGRID_API_KEY_ENV = "SENDGRID_API_KEY"

def maybe_send_email(subject: str, body: str) -> Optional[str]:
    api_key = os.getenv(SENDGRID_API_KEY_ENV)
    to_addr = os.getenv("SENDGRID_TO")
    from_addr = os.getenv("SENDGRID_FROM")
    if not api_key or not to_addr or not from_addr:
        return None
    try:
        import json, urllib.request
        data = {
            "personalizations": [{"to": [{"email": to_addr}]}],
            "from": {"email": from_addr},
            "subject": subject,
            "content": [{"type": "text/plain", "value": body}],
        }
        req = urllib.request.Request(
            url="https://api.sendgrid.com/v3/mail/send",
            method="POST",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            data=json.dumps(data).encode("utf-8"),
        )
        with urllib.request.urlopen(req, timeout=10) as resp:  # nosec B310
            return f"SendGrid status: {resp.status}"
    except Exception as e:
        return f"Falha email: {e}"

__all__ = [
    "COLOR_OK",
    "COLOR_ERR",
    "COLOR_INFO",
    "maybe_send_email",
]
