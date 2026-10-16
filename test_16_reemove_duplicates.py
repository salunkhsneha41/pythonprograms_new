import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_16_remove_duplicates.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
assert module.remove_duplicates([5, 5, 5]) == [5]

print("All test cases passed.")