import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Code" / "code_20_word_frequency.py"
spec = importlib.util.spec_from_file_location("program", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}

assert module.word_frequency("Python python code") == {
    "python": 2,
    "code": 1
}

print("All test cases passed.") 