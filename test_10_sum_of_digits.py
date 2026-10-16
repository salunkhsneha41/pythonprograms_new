import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_10_sum_of_digits.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.sum_of_digits(1234) == 10
assert module.sum_of_digits(555) == 15
assert module.sum_of_digits(0) == 0

print("All test cases passed.")