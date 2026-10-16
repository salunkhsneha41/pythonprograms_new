import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_05_fibonacci_series.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
assert module.fibonacci_series(3) == [0, 1, 1]
assert module.fibonacci_series(1) == [0]

print("All test cases passed.")