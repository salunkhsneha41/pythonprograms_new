 import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_18_missing_number.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.missing_number([1, 2, 3, 5], 5) == 4
assert module.missing_number([1, 2, 4, 5], 5) == 3

print("All test cases passed.")