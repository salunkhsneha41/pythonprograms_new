 import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_07_primes_in_range.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.primes_in_range(1, 10) == [2, 3, 5, 7]
assert module.primes_in_range(10, 20) == [11, 13, 17, 19]

print("All test cases passed.")