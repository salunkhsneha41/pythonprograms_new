import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_12_reverse_string.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_string("Python") == "nohtyP"
assert module.reverse_string("hello") == "olleh"

print("All test cases passed.")