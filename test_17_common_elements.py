import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_17_common_elements.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert set(module.common_elements([1, 2, 3], [2, 3, 4])) == {2, 3}
assert set(module.common_elements([1, 5], [2, 3])) == set()

print("All test cases passed.")