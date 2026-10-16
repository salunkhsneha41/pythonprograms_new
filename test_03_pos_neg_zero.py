import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_03_pos_neg_zero.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_number(10) == "Positive"
assert module.check_number(-5) == "Negative"
assert module.check_number(0) == "Zero"

print("All test cases passed.")