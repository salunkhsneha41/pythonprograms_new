import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_08_reverse_number.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_number(12345) == 54321
assert module.reverse_number(100) == 1
assert module.reverse_number(987) == 789

print("All test cases passed.")