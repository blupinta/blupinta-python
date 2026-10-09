"""The examples the guide shows: they compile, and every name they take from the package is there."""

import ast
import importlib
from pathlib import Path

EXAMPLES = Path(__file__).parent.parent / "examples"


def test_every_example_compiles_and_imports_what_exists():
    for example in EXAMPLES.glob("*.py"):
        tree = ast.parse(example.read_text(), filename=str(example))
        compile(tree, str(example), "exec")
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                module = importlib.import_module(node.module)
                for alias in node.names:
                    assert hasattr(module, alias.name), f"{example.name}: {node.module} has no {alias.name}"
