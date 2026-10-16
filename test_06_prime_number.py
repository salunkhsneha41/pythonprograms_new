import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_06_prime_number.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_prime(7) is True
assert module.is_prime(2) is True
assert module.is_prime(10) is False
assert module.is_prime(1) is False

print("All test cases passed.")