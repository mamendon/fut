import json
from pathlib import Path

class TestCase:
    def __init__(self, name, input_path, expected_path):
        self.name = name
        self.input_path = Path(input_path)
        self.expected_path = Path(expected_path)
        self.result_path = None  # Será preenchido após execução

    def load_input(self):
        with open(self.input_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def load_expected(self):
        with open(self.expected_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def __repr__(self):
        return f"<TestCase name={self.name}>"
