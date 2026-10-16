import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "01_even_odd.py"

spec = importlib.util.spec_from_file_location("even_odd", program_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_even_odd(10) == "Even"
assert module.check_even_odd(7) == "Odd"

print("All test cases passed.")