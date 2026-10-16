import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_15_second_largest.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.second_largest([10, 20, 5, 8]) == 10
assert module.second_largest([1, 5, 3, 4]) == 4
assert module.second_largest([10, 10, 8, 6]) == 8

print("All test cases passed.")