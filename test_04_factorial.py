import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_04_factorial.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.factorial(5) == 120
assert module.factorial(0) == 1
assert module.factorial(3) == 6

print("All test cases passed.")