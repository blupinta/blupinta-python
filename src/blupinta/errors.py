"""What Blupinta's API answers when it says no: one error for every refusal, with the API's own code
(``not_found``, ``conflict``, ``rate_limited``...), the problems it lists for a request it can't take, the server's id
for its own failure and, when it asked to slow down, how long to wait."""

from __future__ import annotations

import json

import httpx


class BlupintaError(Exception):
    """A refusal of the API, or a request that never reached it (``code`` ``network``)."""

    def __init__(
        self,
        status: int,
        code: str,
        problems: list[str] | None = None,
        error_id: str | None = None,
        retry_after: int | None = None,
    ) -> None:
        self.status = status
        self.code = code
        self.problems = problems or []
        self.error_id = error_id
        self.retry_after = retry_after
        super().__init__(f"{code}: {'; '.join(self.problems)}" if self.problems else code)


def error_of(status: int, content: bytes, headers: httpx.Headers) -> BlupintaError:
    """The error a refused answer stands for, read from its body and headers."""
    try:
        body = json.loads(content)
    except ValueError:
        body = {}
    if not isinstance(body, dict):
        body = {}
    problems = body.get("problems")
    retry_after = headers.get("retry-after")
    return BlupintaError(
        status,
        body["error"] if isinstance(body.get("error"), str) else "server_error",
        [p for p in problems if isinstance(p, str)] if isinstance(problems, list) else [],
        body["errorId"] if isinstance(body.get("errorId"), str) else None,
        int(retry_after) if retry_after and retry_after.isdigit() else None,
    )
