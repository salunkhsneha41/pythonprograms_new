import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_13_palindrome_string.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_string("madam") is True
assert module.is_palindrome_string("hello") is False
assert module.is_palindrome_string("Level") is True

print("All test cases passed.")