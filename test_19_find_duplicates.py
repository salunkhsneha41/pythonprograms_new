import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_19_find_duplicates.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert set(module.find_duplicates([1, 2, 2, 3, 4, 4])) == {2, 4}
assert module.find_duplicates([1, 2, 3]) == []

print("All test cases passed.") 