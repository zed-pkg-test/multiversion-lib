"""Python 3 line of multiversion-lib.

Type hints and f-strings: syntax that is a hard SyntaxError on 2.7, which is
why this cannot be one artifact serving both lines.
"""

LANGUAGE = "python"
RUNTIME_LINE = "python3"


def greet(who: str) -> str:
    return f"hello {who} from multiversion-lib/python3"
