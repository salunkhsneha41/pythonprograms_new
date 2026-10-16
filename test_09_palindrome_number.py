import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_09_palindrome_number.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome(121) is True
assert module.is_palindrome(123) is False
assert module.is_palindrome(1221) is True

print("All test cases passed.")