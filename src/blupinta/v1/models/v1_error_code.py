from enum import Enum


class V1ErrorCode(str, Enum):
    BLOCKING_PROBLEMS = "blocking_problems"
    CONFLICT = "conflict"
    FORBIDDEN = "forbidden"
    INVALID_HOME = "invalid_home"
    INVALID_INPUT = "invalid_input"
    NOT_FOUND = "not_found"
    RATE_LIMITED = "rate_limited"
    SERVER_ERROR = "server_error"
    UNAUTHENTICATED = "unauthenticated"
    UNSUPPORTED_FILE = "unsupported_file"

    def __str__(self) -> str:
        return str(self.value)
