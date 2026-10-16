import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "code_02_largest_of_three.py"

spec = importlib.util.spec_from_file_location("largest_of_three", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_of_three(10, 25, 15) == 25
assert module.largest_of_three(5, 2, 1) == 5
assert module.largest_of_three(3, 8, 12) == 12

print("All test cases passed.")