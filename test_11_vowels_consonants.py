
import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_11_vowels_consonants.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.count_vowels_consonants("Hello") == (2, 3)
assert module.count_vowels_consonants("Python") == (1, 5)

print("All test cases passed.")