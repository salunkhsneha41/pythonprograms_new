import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_14_char_frequency.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.character_frequency("hello") == {
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}
print("All test cases passed.") 
 